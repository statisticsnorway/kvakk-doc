# kvakk-doc
Public documentation from the Quality in code and coding (KVAKK) group in Statistics Norway.
The content is exported from the Confluence [KVAKK]-pages at Statistics Norway.

The raw export from Confluence is stored in the directory `confluence/raw/`.

## How to export the pages from Confluence?

The export is done by using the open source [confluence-markdown-exporter] (cme) tool.

### Create a Confluence API-token

Create a Confluence API-token with the following scopes:

```
read:confluence-content.all
read:account
read:confluence-content.permission
read:confluence-content.summary
read:confluence-groups
read:confluence-props
read:confluence-space.summary
read:confluence-user
read:me
readonly:content.attachment:confluence
search:confluence
```

### Install and configure the export tool

```shell
uv sync
cp config/.env.example .env
```

On Windows PowerShell, create the environment file with:

```powershell
uv sync
Copy-Item config/.env.example .env
```

Add the Confluence username, API token, and Cloud ID to `.env`. This file
is ignored by Git. Environment variables set by the shell or CI take precedence
over values in the file.

The non-secret CME settings are stored in `config/cme.json`. The export command
and source URLs are stored in `config/export.json`.

### Export

Run this command from the root directory of the git-repo:

```shell
uv run python scripts/export.py
```


[confluence-markdown-exporter]: https://github.com/Spenhouet/confluence-markdown-exporter
[KVAKK]: https://statistics-norway.atlassian.net/wiki/spaces/BEST/pages/3261497397/Kvalitet+i+kode+og+koding
