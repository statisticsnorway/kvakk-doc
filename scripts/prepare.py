#!/usr/bin/env python3

import json
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlsplit
from urllib.parse import urlunsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "confluence" / "raw"
GENERATED_DIR = ROOT / "docs" / "generated"
LOCK_PATH = RAW_DIR / "confluence-lock.json"
NAVIGATION_PATH = ROOT / "config" / "navigation.json"
ROOT_PAGE_ID = "3261497397"
ATTACHMENTS_DIR = GENERATED_DIR / "assets" / "attachments"

CALLOUT = re.compile(r"^(?P<indent>\s*)> \[!(?P<kind>IMPORTANT|WARNING)\]\s*$")
INACCESSIBLE = re.compile(r"Page not accessible \(ID: (?P<id>\d+)\)")
WIKI_TEXT = re.compile(r"\[\[[^]]+\]\]")
DETAILS = re.compile(r"^(?P<indent>\s*)<details>\s*$", flags=re.MULTILINE)
PEOPLE_LINK = re.compile(
    r"\[[^\]\n]*\]\("
    r"(?:https://statistics-norway\.atlassian\.net)?/(?:wiki/)?people/[^)\n]*"
    r"\)"
)
TABLE_SEPARATOR = re.compile(r"^:?-{3,}:?$")
ESCAPED_EMOJI = re.compile(
    r"\\uD[89AB][0-9A-F]{2}\\uD[C-F][0-9A-F]{2}[\t \u00a0]*",
    flags=re.IGNORECASE,
)
LINE_BREAK = re.compile(r"\s*<br\s*/?>\s*", flags=re.IGNORECASE)
FULL_MARK = re.compile(
    r'^<mark\s+style="background:\s*(?P<color>#[0-9a-fA-F]{6});?">'
    r"(?P<body>.*)</mark>$",
    flags=re.DOTALL,
)


def safe_source_path(relative_path: str) -> Path:
    """Resolve an export path while keeping it inside the raw directory.

    Args:
        relative_path: Path relative to the raw export directory.

    Returns:
        The resolved source path.

    Raises:
        SystemExit: If the path escapes the raw export directory.
    """
    path = (RAW_DIR / relative_path).resolve()
    if not path.is_relative_to(RAW_DIR.resolve()):
        raise SystemExit(f"Export path leaves {RAW_DIR}: {relative_path}")
    return path


def generated_destination(
    source: Path,
    root_source: Path,
    descendant_root: Path,
    generated_dir: Path = GENERATED_DIR,
) -> Path:
    """Map a raw page to its generated documentation path.

    Args:
        source: Raw Markdown page path.
        root_source: Root page of the selected export.
        descendant_root: Directory containing exported descendants.
        generated_dir: Destination documentation directory.

    Returns:
        The generated page path.

    """
    if source == root_source:
        return generated_dir / "index.md"

    relative = source.relative_to(descendant_root)
    if source.with_suffix("").is_dir():
        return generated_dir / relative.with_suffix("") / "index.md"
    return generated_dir / relative


def load_root_navigation() -> list[str]:
    """Load the configured top-level navigation order.

    Returns:
        Ordered section names.

    Raises:
        SystemExit: If the navigation configuration is missing or invalid.
    """
    try:
        config = json.loads(NAVIGATION_PATH.read_text(encoding="utf-8"))
        navigation = config["root"]
    except (OSError, json.JSONDecodeError, KeyError) as error:
        raise SystemExit(f"Invalid navigation config: {error}") from error
    if not isinstance(navigation, list) or not all(
        isinstance(item, str) and item for item in navigation
    ):
        raise SystemExit(
            "Navigation config 'root' must be a list of non-empty strings."
        )
    return navigation


def render_navigation(items: list[str]) -> str:
    """Render section names as an awesome-nav configuration.

    Needed to get a custom order ofthe elements in the left menu.

    Args:
        items: Ordered section names.

    Returns:
        YAML navigation content.
    """
    entries = ["  - index.md", *(f"  - {json.dumps(item)}" for item in items)]
    return "nav:\n" + "\n".join(entries) + "\nappend_unmatched: true\n"


def load_export() -> tuple[str, dict[Path, Path], dict[Path, Path]]:
    """Load and validate the exported page and attachment mappings.

    Returns:
        The Confluence origin, page map, and attachment map.

    Raises:
        SystemExit: If the lockfile or any referenced export file is invalid.
        ValueError: If the lockfile version or organization count is unsupported.
    """
    try:
        lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
        if lock["lockfile_version"] != 2:
            raise ValueError("unsupported lockfile version")
        orgs = lock["orgs"]
        if len(orgs) != 1:
            raise ValueError("expected exactly one Confluence organization")
        origin, org = next(iter(orgs.items()))
        pages = org["spaces"]["BEST"]["pages"]
        root_page = pages[ROOT_PAGE_ID]
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        raise SystemExit(f"Invalid Confluence lockfile: {error}") from error

    root_source = safe_source_path(root_page["export_path"])
    descendant_root = root_source.with_suffix("")
    page_map: dict[Path, Path] = {}
    attachment_map: dict[Path, Path] = {}

    for page in pages.values():
        source = safe_source_path(page["export_path"])
        if not source.is_file() or source.suffix != ".md":
            raise SystemExit(f"Missing exported page: {source.relative_to(ROOT)}")
        if source != root_source and not source.is_relative_to(descendant_root):
            continue
        destination = generated_destination(source, root_source, descendant_root)
        if destination in page_map.values():
            raise SystemExit(
                f"Generated page collision: {destination.relative_to(ROOT)}"
            )
        page_map[source] = destination

        for attachment in page.get("attachments", {}).values():
            attachment_source = safe_source_path(attachment["path"])
            if not attachment_source.is_file():
                raise SystemExit(
                    f"Missing exported attachment: {attachment_source.relative_to(ROOT)}"
                )
            destination = ATTACHMENTS_DIR / attachment_source.name
            previous = next(
                (
                    path
                    for path, target in attachment_map.items()
                    if target == destination
                ),
                None,
            )
            if previous is not None and previous != attachment_source:
                raise SystemExit(
                    f"Generated attachment collision: {destination.relative_to(ROOT)}"
                )
            attachment_map[attachment_source] = destination

    if root_source not in page_map:
        raise SystemExit(f"Root page {ROOT_PAGE_ID} is outside the selected export")
    return origin.rstrip("/"), page_map, attachment_map


def convert_callouts(text: str) -> str:
    """Convert exported GitHub-style callouts to admonitions.

    Args:
        text: Exported Markdown content.

    Returns:
        Markdown with compatible admonition syntax.
    """
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        match = CALLOUT.match(line.rstrip("\r\n"))
        if match is None:
            output.append(line)
            index += 1
            continue

        indent = match["indent"]
        output.append(f"{indent}!!! {match['kind'].lower()}\n")
        index += 1
        while index < len(lines):
            quoted = re.match(rf"^{re.escape(indent)}> ?(.*?)(\r?\n)?$", lines[index])
            if quoted is None:
                break
            body = quoted.group(1)
            newline = quoted.group(2) or "\n"
            output.append(f"{indent}    {body}{newline}")
            index += 1
    return "".join(output)


def enable_markdown_in_details(text: str) -> str:
    """Enable Markdown parsing in exported details elements.

    Args:
        text: Exported Markdown content.

    Returns:
        Markdown with annotated details elements.
    """
    return DETAILS.sub(r'\g<indent><details markdown="1">', text)


def split_table_row(line: str) -> list[str] | None:
    """Split a Markdown table row into stripped cells.

    Args:
        line: Potential Markdown table row.

    Returns:
        Cell content, or ``None`` when the line is not a complete table row.
    """
    stripped = line.rstrip("\r\n").strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def remove_people(text: str) -> str:
    """Remove Confluence people links and table columns containing them.

    Args:
        text: Exported Markdown content.

    Returns:
        Markdown without people names or profile links.
    """
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    index = 0
    while index < len(lines):
        header = split_table_row(lines[index])
        separator = (
            split_table_row(lines[index + 1]) if index + 1 < len(lines) else None
        )
        if (
            header is None
            or separator is None
            or len(header) != len(separator)
            or not all(TABLE_SEPARATOR.fullmatch(cell) for cell in separator)
        ):
            output.append(lines[index])
            index += 1
            continue

        table: list[tuple[list[str], str, str]] = []
        while index < len(lines):
            cells = split_table_row(lines[index])
            if cells is None or len(cells) != len(header):
                break
            newline = "\r\n" if lines[index].endswith("\r\n") else "\n"
            table.append((cells, newline, lines[index]))
            index += 1

        removed = {
            column
            for cells, _, _ in table
            for column, cell in enumerate(cells)
            if PEOPLE_LINK.search(cell)
        }
        if not removed:
            output.extend(raw for _, _, raw in table)
            continue
        output.extend(
            "| "
            + " | ".join(
                cell for column, cell in enumerate(cells) if column not in removed
            )
            + " |"
            + newline
            for cells, newline, _ in table
        )

    return PEOPLE_LINK.sub("", "".join(output))


def remove_escaped_emoji(text: str) -> str:
    """Remove exported UTF-16 emoji escapes outside code fences.

    Args:
        text: Exported Markdown content.

    Returns:
        Markdown without malformed emoji escape text.
    """
    output: list[str] = []
    in_fence = False
    fence = ""
    for line in text.splitlines(keepends=True):
        fence_match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence_match:
            marker = fence_match.group(1)
            if not in_fence:
                in_fence, fence = True, marker[0]
            elif marker[0] == fence:
                in_fence = False
            output.append(line)
            continue
        output.append(line if in_fence else ESCAPED_EMOJI.sub("", line))
    return "".join(output)


def render_table_cell(cell: str) -> tuple[str, str]:
    """Render exported table-cell Markdown as HTML.

    Args:
        cell: Exported cell content.

    Returns:
        Rendered HTML and any cell-level style attribute.
    """
    style = ""
    mark = FULL_MARK.fullmatch(cell.strip())
    if mark:
        style = f' style="background: {mark["color"]};"'
        cell = mark["body"]

    parts = [part.strip() for part in LINE_BREAK.split(cell) if part.strip()]
    if any(part.startswith("- ") for part in parts):
        items: list[str] = []
        has_parent = False
        for part in parts:
            content = part[2:].strip() if part.startswith("- ") else part
            if (not part.startswith("- ") or content.startswith("[")) and has_parent:
                items.append(f"    - {content}")
            else:
                items.append(f"- {content}")
                has_parent = True
        cell = "\n".join(items)

    rendered = markdown.markdown(cell).strip()
    if rendered.startswith("<p>") and rendered.endswith("</p>"):
        rendered = rendered[3:-4]
    return rendered, style


def convert_complex_tables(text: str) -> str:
    """Restore lists and column spans in flattened Confluence tables.

    Args:
        text: Exported Markdown content.

    Returns:
        Markdown with complex tables represented as semantic HTML.
    """
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    index = 0
    while index < len(lines):
        header = split_table_row(lines[index])
        separator = (
            split_table_row(lines[index + 1]) if index + 1 < len(lines) else None
        )
        if (
            header is None
            or separator is None
            or len(header) != len(separator)
            or not all(TABLE_SEPARATOR.fullmatch(cell) for cell in separator)
        ):
            output.append(lines[index])
            index += 1
            continue

        rows: list[list[str]] = []
        cursor = index + 2
        while cursor < len(lines):
            cells = split_table_row(lines[cursor])
            if cells is None or len(cells) != len(header):
                break
            rows.append(cells)
            cursor += 1

        is_complex = any(
            len(set(row)) == 1 or any(LINE_BREAK.search(cell) for cell in row)
            for row in rows
        )
        if not is_complex:
            output.extend(lines[index:cursor])
            index = cursor
            continue

        output.extend(["<table>\n", "  <thead>\n", "    <tr>\n"])
        for cell in header:
            rendered, style = render_table_cell(cell)
            output.append(f"      <th{style}>{rendered}</th>\n")
        output.extend(["    </tr>\n", "  </thead>\n", "  <tbody>\n"])
        for row in rows:
            output.append("    <tr>\n")
            cells = [row[0]] if len(set(row)) == 1 else row
            for cell in cells:
                rendered, style = render_table_cell(cell)
                colspan = f' colspan="{len(row)}"' if len(cells) == 1 else ""
                output.append(f"      <td{colspan}{style}>{rendered}</td>\n")
            output.append("    </tr>\n")
        output.extend(["  </tbody>\n", "</table>\n"])
        index = cursor
    return "".join(output)


def split_destination(destination: str) -> tuple[str, str]:
    """Separate a Markdown link target from its optional suffix.

    Args:
        destination: Raw Markdown link destination.

    Returns:
        The URL target and trailing title or whitespace.
    """
    if destination.startswith("<") and ">" in destination:
        end = destination.index(">")
        return destination[1:end], destination[end + 1 :]
    match = re.match(r"(\S+)(.*)", destination, flags=re.DOTALL)
    return (match.group(1), match.group(2)) if match else (destination, "")


def relative_url(source: Path, destination: Path) -> str:
    """Build an encoded relative URL between generated files.

    Args:
        source: Generated page containing the link.
        destination: Generated link target.

    Returns:
        A percent-encoded relative URL.
    """
    return quote(
        Path(os.path.relpath(destination, source.parent)).as_posix(),
        safe="/._-~",
    )


def external_search_url(origin: str, raw_target: str) -> str:
    """Build a Confluence search URL for a page outside the export.

    Args:
        origin: Confluence instance origin.
        raw_target: Original relative page target.

    Returns:
        A Confluence search URL based on the target title.
    """
    title = Path(unquote(urlsplit(raw_target).path)).stem.replace("_", "?")
    return f"{origin}/wiki/search?text={quote(title)}"


def rewrite_target(
    target: str,
    source: Path,
    destination: Path,
    origin: str,
    page_map: dict[Path, Path],
    attachment_map: dict[Path, Path],
    diagnostics: list[str],
    line_number: int,
) -> str:
    """Rewrite one link target for the generated documentation tree.

    Args:
        target: Original link target.
        source: Raw page containing the link.
        destination: Generated page containing the rewritten link.
        origin: Confluence instance origin.
        page_map: Raw-to-generated page mapping.
        attachment_map: Raw-to-generated attachment mapping.
        diagnostics: Collection receiving link warnings.
        line_number: Source line containing the link.

    Returns:
        The rewritten link target.
    """
    if not target or target.startswith(("#", "mailto:", "tel:", "data:")):
        return target
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return target
    if parsed.path.startswith("/"):
        return f"{origin}{target}"

    resolved = (source.parent / unquote(parsed.path)).resolve()
    mapped = page_map.get(resolved) or attachment_map.get(resolved)
    if mapped is not None:
        path = (
            "./"
            if mapped == destination and destination.name == "index.md"
            else relative_url(destination, mapped)
        )
        return urlunsplit(("", "", path, parsed.query, parsed.fragment))

    if parsed.path.lower().endswith(".md"):
        diagnostics.append(
            f"{source.relative_to(ROOT)}:{line_number}: link outside export: {target}"
        )
        return external_search_url(origin, target)
    return target


def rewrite_links(
    text: str,
    source: Path,
    destination: Path,
    origin: str,
    page_map: dict[Path, Path],
    attachment_map: dict[Path, Path],
    diagnostics: list[str],
) -> str:
    """Rewrite Markdown links while preserving code spans and fences.

    Args:
        text: Exported Markdown content.
        source: Raw page containing the links.
        destination: Generated destination page.
        origin: Confluence instance origin.
        page_map: Raw-to-generated page mapping.
        attachment_map: Raw-to-generated attachment mapping.
        diagnostics: Collection receiving link warnings.

    Returns:
        Markdown with rewritten links.
    """
    output: list[str] = []
    in_fence = False
    fence = ""
    for line_number, line in enumerate(text.splitlines(keepends=True), 1):
        fence_match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence_match:
            marker = fence_match.group(1)
            if not in_fence:
                in_fence, fence = True, marker[0]
            elif marker[0] == fence:
                in_fence = False
            output.append(line)
            continue
        if in_fence:
            output.append(line)
            continue

        rewritten: list[str] = []
        index = 0
        code_ticks = 0
        while index < len(line):
            if line[index] == "`":
                end = index
                while end < len(line) and line[end] == "`":
                    end += 1
                ticks = end - index
                code_ticks = (
                    0
                    if code_ticks == ticks
                    else ticks
                    if code_ticks == 0
                    else code_ticks
                )
                rewritten.append(line[index:end])
                index = end
                continue
            if code_ticks or not line.startswith("](", index):
                rewritten.append(line[index])
                index += 1
                continue

            start = index + 2
            cursor = start
            depth = 0
            while cursor < len(line):
                character = line[cursor]
                if character == "\\":
                    cursor += 2
                    continue
                if character == "(":
                    depth += 1
                elif character == ")":
                    if depth == 0:
                        break
                    depth -= 1
                cursor += 1
            if cursor == len(line):
                rewritten.append(line[index])
                index += 1
                continue

            raw_destination = line[start:cursor]
            target, suffix = split_destination(raw_destination)
            new_target = rewrite_target(
                target,
                source,
                destination,
                origin,
                page_map,
                attachment_map,
                diagnostics,
                line_number,
            )
            rewritten.append(f"]({new_target}{suffix})")
            index = cursor + 1
        output.append("".join(rewritten))
    return "".join(output)


def report_source_artifacts(text: str, source: Path, diagnostics: list[str]) -> None:
    """Report unresolved artifacts found in exported content.

    Args:
        text: Exported Markdown content.
        source: Raw source page.
        diagnostics: Collection receiving warnings.
    """
    for line_number, line in enumerate(text.splitlines(), 1):
        for match in INACCESSIBLE.finditer(line):
            diagnostics.append(
                f"{source.relative_to(ROOT)}:{line_number}: inaccessible page {match['id']}"
            )
        for match in WIKI_TEXT.finditer(line):
            diagnostics.append(
                f"{source.relative_to(ROOT)}:{line_number}: unresolved text {match.group()}"
            )


def prepare() -> list[str]:
    """Regenerate site-ready documentation from the raw export.

    Returns:
        Warnings discovered while processing source content.

    Raises:
        SystemExit: If export metadata, files, or navigation are invalid.
    """
    origin, page_map, attachment_map = load_export()
    root_navigation = load_root_navigation()
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    GENERATED_DIR.mkdir(parents=True)

    diagnostics: list[str] = []
    for source, destination in sorted(
        page_map.items(), key=lambda item: item[1].as_posix()
    ):
        text = source.read_text(encoding="utf-8")
        report_source_artifacts(text, source, diagnostics)
        text = convert_callouts(text)
        text = enable_markdown_in_details(text)
        text = remove_people(text)
        text = remove_escaped_emoji(text)
        text = rewrite_links(
            text,
            source,
            destination,
            origin,
            page_map,
            attachment_map,
            diagnostics,
        )
        text = convert_complex_tables(text)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text.rstrip("\n") + "\n", encoding="utf-8")

    available_sections = {
        path.name for path in GENERATED_DIR.iterdir() if path.is_dir()
    }
    missing_sections = set(root_navigation) - available_sections
    if missing_sections:
        missing = ", ".join(sorted(missing_sections))
        raise SystemExit(f"Navigation config references missing sections: {missing}")
    (GENERATED_DIR / ".nav.yml").write_text(
        render_navigation(root_navigation), encoding="utf-8"
    )

    for source, destination in sorted(
        attachment_map.items(), key=lambda item: item[1].as_posix()
    ):
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)

    return diagnostics


def main() -> None:
    """Prepare documentation and print processing diagnostics."""
    diagnostics = prepare()
    for diagnostic in diagnostics:
        print(f"warning: {diagnostic}", file=sys.stderr)
    print(
        f"Prepared documentation in {GENERATED_DIR.relative_to(ROOT)} "
        f"with {len(diagnostics)} source warning(s)."
    )


if __name__ == "__main__":
    main()
