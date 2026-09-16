from pathlib import Path

from scripts.prepare import (
    convert_callouts,
    enable_markdown_in_details,
    generated_destination,
    render_navigation,
    rewrite_links,
)


def test_convert_callouts_preserves_multiline_content() -> None:
    text = "> [!IMPORTANT]\n> First\n>\n> - second\n\nOrdinary\n"

    assert convert_callouts(text) == (
        "!!! important\n    First\n    \n    - second\n\nOrdinary\n"
    )


def test_enable_markdown_in_details_marks_exported_blocks() -> None:
    text = (
        "<details>\n<summary>Hvorfor</summary>\n\n- first\n- second\n\n</details>\n"
    )

    assert enable_markdown_in_details(text) == (
        '<details markdown="1">\n'
        "<summary>Hvorfor</summary>\n\n- first\n- second\n\n</details>\n"
    )


def test_enable_markdown_in_details_leaves_existing_attributes_unchanged() -> None:
    text = '<details class="example">\ncontent\n</details>\n'

    assert enable_markdown_in_details(text) == text


def test_generated_destination_uses_index_for_pages_with_children(
    tmp_path: Path,
) -> None:
    descendant_root = tmp_path / "raw" / "Root"
    source = descendant_root / "Parent.md"
    source.parent.mkdir(parents=True)
    source.touch()
    source.with_suffix("").mkdir()

    assert generated_destination(
        source,
        tmp_path / "raw" / "Root.md",
        descendant_root,
        tmp_path / "generated",
    ) == tmp_path / "generated" / "Parent" / "index.md"


def test_generated_destination_keeps_leaf_filename(tmp_path: Path) -> None:
    descendant_root = tmp_path / "raw" / "Root"
    source = descendant_root / "Leaf.md"

    assert generated_destination(
        source,
        tmp_path / "raw" / "Root.md",
        descendant_root,
        tmp_path / "generated",
    ) == tmp_path / "generated" / "Leaf.md"


def test_render_navigation_preserves_configured_order() -> None:
    assert render_navigation(["Rules", "Version control", "Collaboration?"]) == (
        "nav:\n"
        "  - index.md\n"
        '  - "Rules"\n'
        '  - "Version control"\n'
        '  - "Collaboration?"\n'
        "append_unmatched: true\n"
    )


def test_rewrite_links_handles_parentheses_and_skips_code(tmp_path: Path) -> None:
    source = tmp_path / "raw" / "source.md"
    target = tmp_path / "raw" / "A (B).md"
    destination = tmp_path / "generated" / "source.md"
    target_destination = tmp_path / "generated" / "A (B).md"
    diagnostics: list[str] = []
    text = "[page](A%20(B).md) and `[code](A%20(B).md)`\n"

    result = rewrite_links(
        text,
        source,
        destination,
        "https://example.atlassian.net",
        {target.resolve(): target_destination},
        {},
        diagnostics,
    )

    assert result == "[page](A%20%28B%29.md) and `[code](A%20(B).md)`\n"
    assert diagnostics == []


def test_rewrite_links_absolutizes_confluence_paths(tmp_path: Path) -> None:
    source = tmp_path / "raw" / "source.md"
    destination = tmp_path / "generated" / "source.md"

    result = rewrite_links(
        "[space](/wiki/spaces/TEST)\n",
        source,
        destination,
        "https://example.atlassian.net",
        {},
        {},
        [],
    )

    assert result == "[space](https://example.atlassian.net/wiki/spaces/TEST)\n"
