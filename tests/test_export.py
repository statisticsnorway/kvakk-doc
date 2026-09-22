import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from scripts.export import export_fingerprint
from scripts.export import update_export_timestamp


def test_export_fingerprint_ignores_last_export_timestamp(tmp_path: Path) -> None:
    lock_path = tmp_path / "confluence-lock.json"
    lock_path.write_text(
        json.dumps({"last_export": "first", "pages": {"1": {"version": 1}}}),
        encoding="utf-8",
    )
    before = export_fingerprint(tmp_path, lock_path)
    lock_path.write_text(
        json.dumps({"last_export": "second", "pages": {"1": {"version": 1}}}),
        encoding="utf-8",
    )

    assert export_fingerprint(tmp_path, lock_path) == before


def test_export_fingerprint_detects_export_changes(tmp_path: Path) -> None:
    page = tmp_path / "page.md"
    page.write_text("before\n", encoding="utf-8")
    before = export_fingerprint(tmp_path, tmp_path / "confluence-lock.json")
    page.write_text("after\n", encoding="utf-8")

    assert export_fingerprint(tmp_path, tmp_path / "confluence-lock.json") != before


def test_update_export_timestamp_replaces_only_timestamp_line(tmp_path: Path) -> None:
    index_path = tmp_path / "index.md"
    index_path.write_text(
        "# Heading\n\nOther text.\n\nSist eksportert fra Confluence: 2025-01-01 10:00\n",
        encoding="utf-8",
    )

    update_export_timestamp(
        index_path, datetime(2026, 9, 17, 12, 34, tzinfo=ZoneInfo("Europe/Oslo"))
    )

    assert index_path.read_text(encoding="utf-8") == (
        "# Heading\n\nOther text.\n\nSist eksportert fra Confluence: 2026-09-17 12:34\n"
    )


def test_update_export_timestamp_appends_missing_line(tmp_path: Path) -> None:
    index_path = tmp_path / "index.md"
    index_path.write_text("# Heading\n", encoding="utf-8")

    update_export_timestamp(
        index_path, datetime(2026, 1, 2, 3, 4, tzinfo=ZoneInfo("Europe/Oslo"))
    )

    assert index_path.read_text(encoding="utf-8") == (
        "# Heading\n\nSist eksportert fra Confluence: 2026-01-02 03:04\n"
    )
