#!/usr/bin/env python3

import json
import os
import shutil
import subprocess
from pathlib import Path

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
DOTENV_PATH = ROOT / ".env"
CME_CONFIG_PATH = CONFIG_DIR / "cme.json"
EXPORT_CONFIG_PATH = CONFIG_DIR / "export.json"

type JsonObject = dict[str, object]


def required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(
            f"Missing {name}. Set it in {DOTENV_PATH.relative_to(ROOT)} "
            "or in the environment."
        )
    return value


def load_export_config() -> tuple[str, list[str]]:
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
    if not isinstance(urls, list) or not urls or not all(isinstance(url, str) for url in urls):
        raise SystemExit("Export config 'urls' must be a non-empty list of strings.")

    return command, urls


def main() -> None:
    load_dotenv(DOTENV_PATH, override=False)

    confluence_url = required_env("CONFLUENCE_URL").rstrip("/")
    auth = {
        "confluence": {
            confluence_url: {
                "username": required_env("CONFLUENCE_USERNAME"),
                "api_token": required_env("CONFLUENCE_API_TOKEN"),
                "cloud_id": required_env("CONFLUENCE_CLOUD_ID"),
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

    subprocess.run(
        [cme, command, *urls],
        cwd=ROOT,
        env=env,
        check=True,
    )


if __name__ == "__main__":
    main()
