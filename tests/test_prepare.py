from pathlib import Path

from scripts.prepare import convert_callouts, rewrite_links


def test_convert_callouts_preserves_multiline_content() -> None:
    text = "> [!IMPORTANT]\n> First\n>\n> - second\n\nOrdinary\n"

    assert convert_callouts(text) == (
        "!!! important\n    First\n    \n    - second\n\nOrdinary\n"
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
