#!/usr/bin/env python3

import json
import os
import shutil
import subprocess
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from zoneinfo import ZoneInfo

import httpx
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
DOTENV_PATH = ROOT / ".env"
CME_CONFIG_PATH = CONFIG_DIR / "cme.json"
EXPORT_CONFIG_PATH = CONFIG_DIR / "export.json"
RAW_DIR = ROOT / "confluence" / "raw"
LOCK_PATH = RAW_DIR / "confluence-lock.json"
INDEX_PATH = ROOT / "docs" / "index.md"
TIMESTAMP_PREFIX = "Sist eksportert fra Confluence: "

type JsonObject = dict[str, object]


def required_env(name: str) -> str:
    """Read a required environment variable.

    Args:
        name: Environment variable name.

    Returns:
        The stripped environment variable value.

    Raises:
        SystemExit: If the variable is missing or empty.
    """
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(
            f"Missing {name}. Set it in {DOTENV_PATH.relative_to(ROOT)} "
            "or in the environment."
        )
    return value


def get_cloud_id(confluence_url: str) -> str:
    """Discover the Confluence Cloud tenant ID.

    Args:
        confluence_url: Base URL of the Confluence instance.

    Returns:
        The tenant's Cloud ID.

    Raises:
        SystemExit: If tenant discovery fails or returns no Cloud ID.
    """
    tenant_info_url = f"{confluence_url}/_edge/tenant_info"
    try:
        response = httpx.get(
            tenant_info_url,
            headers={"Accept": "application/json", "User-Agent": "kvakk-doc-export"},
            timeout=10,
        )
        response.raise_for_status()
        tenant_info: object = response.json()
    except (httpx.HTTPError, json.JSONDecodeError) as error:
        raise SystemExit(
            f"Could not discover the Confluence Cloud ID from {tenant_info_url}: "
            f"{error}"
        ) from error

    if not isinstance(tenant_info, dict) or not isinstance(
        cloud_id := tenant_info.get("cloudId"), str
    ):
        raise SystemExit(f"No Confluence Cloud ID was returned by {tenant_info_url}.")
    return cloud_id


def load_export_config() -> tuple[str, list[str]]:
    """Load and validate the export command and source URLs.

    Returns:
        The configured command and Confluence URLs.

    Raises:
        SystemExit: If the export configuration is missing or invalid.
    """
    try:
        config: JsonObject = json.loads(EXPORT_CONFIG_PATH.read_text(encoding="utf-8"))
        command = config["command"]
        urls = config["urls"]
    except (OSError, json.JSONDecodeError, KeyError) as error:
        raise SystemExit(f"Invalid export config: {error}") from error

    allowed_commands = {"pages", "pages-with-descendants", "spaces", "orgs"}
    if not isinstance(command, str) or command not in allowed_commands:
        choices = ", ".join(sorted(allowed_commands))
        raise SystemExit(f"Invalid export command. Expected one of: {choices}")
    if (
        not isinstance(urls, list)
        or not urls
        or not all(isinstance(url, str) for url in urls)
    ):
        raise SystemExit("Export config 'urls' must be a non-empty list of strings.")

    return command, urls


def export_fingerprint(
    export_dir: Path = RAW_DIR, lock_path: Path = LOCK_PATH
) -> dict[str, str]:
    """Fingerprint exported files while ignoring the lock timestamp.

    Args:
        export_dir: Root directory containing the Confluence export.
        lock_path: Export lockfile whose timestamp should be ignored.

    Returns:
        Content hashes keyed by paths relative to the export directory.

    Raises:
        OSError: If an exported file cannot be read.
        json.JSONDecodeError: If the lockfile is invalid JSON.
    """
    fingerprint: dict[str, str] = {}
    if not export_dir.exists():
        return fingerprint

    try:
        for path in sorted(item for item in export_dir.rglob("*") if item.is_file()):
            if path == lock_path:
                lock = json.loads(path.read_text(encoding="utf-8"))
                lock.pop("last_export", None)
                content = json.dumps(
                    lock, sort_keys=True, separators=(",", ":")
                ).encode()
            else:
                content = path.read_bytes()
            fingerprint[path.relative_to(export_dir).as_posix()] = sha256(
                content
            ).hexdigest()
    except (OSError, json.JSONDecodeError):
        raise
    return fingerprint


def update_export_timestamp(
    index_path: Path = INDEX_PATH, timestamp: datetime | None = None
) -> None:
    """Update the standalone export timestamp in the landing page.

    Args:
        index_path: Landing page to update.
        timestamp: Timestamp to write, defaulting to the current Oslo time.

    Raises:
        OSError: If the landing page cannot be read or written.
    """
    current = timestamp or datetime.now(ZoneInfo("Europe/Oslo"))
    replacement = f"{TIMESTAMP_PREFIX}{current.strftime('%Y-%m-%d %H:%M')}"
    try:
        lines = index_path.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines):
            if line.startswith(TIMESTAMP_PREFIX):
                lines[index] = replacement
                break
        else:
            if lines and lines[-1]:
                lines.append("")
            lines.append(replacement)
        index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError:
        raise


def main() -> None:
    """Export the configured Confluence content.

    Raises:
        SystemExit: If configuration, credentials, or the exporter are unavailable.
    """
    load_dotenv(DOTENV_PATH, override=False)

    confluence_url = required_env("CONFLUENCE_URL").rstrip("/")
    auth = {
        "confluence": {
            confluence_url: {
                "username": required_env("CONFLUENCE_USERNAME"),
                "api_token": required_env("CONFLUENCE_API_TOKEN"),
                "cloud_id": get_cloud_id(confluence_url),
            }
        }
    }
    command, urls = load_export_config()

    cme = shutil.which("cme")
    if cme is None:
        raise SystemExit("cme is not installed. Run the script with 'uv run'.")

    env = os.environ.copy()
    env["CME_CONFIG_PATH"] = str(CME_CONFIG_PATH)
    env["CME_AUTH"] = json.dumps(auth)

    before = export_fingerprint()
    subprocess.run(
        [cme, command, *urls],
        cwd=ROOT,
        env=env,
        check=True,
    )
    if export_fingerprint() != before:
        update_export_timestamp()


if __name__ == "__main__":
    main()
