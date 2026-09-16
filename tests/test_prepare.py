from pathlib import Path

from scripts.prepare import (
    convert_complex_tables,
    convert_callouts,
    enable_markdown_in_details,
    generated_destination,
    remove_escaped_emoji,
    remove_people,
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


def test_remove_people_removes_author_table_column() -> None:
    text = (
        "| Tittel | Forfatter | Endret |\n"
        "| --- | --- | --- |\n"
        "| [Side](side.md) | [Arne Sørli](/people/123?ref=confluence) | i dag |\n"
        "| [Annen](annen.md) | [Lisa Eriksen](https://statistics-norway.atlassian.net/people/456) | i går |\n"
    )

    assert remove_people(text) == (
        "| Tittel | Endret |\n"
        "| --- | --- |\n"
        "| [Side](side.md) | i dag |\n"
        "| [Annen](annen.md) | i går |\n"
    )


def test_remove_people_removes_standalone_link_and_name() -> None:
    text = "Kontakt [Ola Nordmann](/people/123) for hjelp.\n"

    assert remove_people(text) == "Kontakt  for hjelp.\n"


def test_remove_people_preserves_unrelated_table_and_links() -> None:
    text = "| Tittel | Eier |\n| --- | --- |\n| [Side](side.md) | Team |\n"

    assert remove_people(text) == text


def test_remove_escaped_emoji_from_headings_labels_and_links() -> None:
    text = (
        "## \\uD83D\\uDCCB\u00a0Relaterte artikler\n"
        "\\uD83D\\uDCD8\u00a0**Instruksjoner**\n"
        "[\\uD83D\\uDCCB\u00a0Relaterte artikler](#related)\n"
    )

    assert remove_escaped_emoji(text) == (
        "## Relaterte artikler\n"
        "**Instruksjoner**\n"
        "[Relaterte artikler](#related)\n"
    )


def test_remove_escaped_emoji_preserves_code_fences() -> None:
    text = "```text\n\\uD83D\\uDCCB clipboard\n```\n"

    assert remove_escaped_emoji(text) == text


def test_convert_complex_tables_restores_colspan_and_lists() -> None:
    text = (
        "| **Fordeler** | **Ulemper** |\n"
        "| --- | --- |\n"
        "| Intro | Intro |\n"
        "| - One <br>- Two | - Other <br>- [Link](page.md) |\n"
    )

    result = convert_complex_tables(text)

    assert '<td colspan="2">Intro</td>' in result
    assert "<ul>\n<li>One</li>\n<li>Two</li>\n</ul>" in result
    assert "<li>Other<ul>\n<li><a href=\"page.md\">Link</a></li>" in result


def test_convert_complex_tables_moves_full_cell_highlight_to_cell() -> None:
    text = (
        "| A | B |\n"
        "| --- | --- |\n"
        '| <mark style="background: #abf5d1;">**Heading**</mark> | '
        '<mark style="background: #abf5d1;">**Heading**</mark> |\n'
    )

    assert (
        '<td colspan="2" style="background: #abf5d1;"><strong>Heading</strong></td>'
        in convert_complex_tables(text)
    )


def test_convert_complex_tables_preserves_plain_markdown_table() -> None:
    text = "| A | B |\n| --- | --- |\n| One | Two |\n"

    assert convert_complex_tables(text) == text


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
