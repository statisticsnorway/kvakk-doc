# Assistant (Plan · GPT-5.6 Sol · 48.3s)

_Thinking:_



Yes, use **Material for MkDocs**, with three clearly separated layers:

1. Raw, committed Confluence export
2. Generated MkDocs input
3. Generated static website

The GitHub Actions workflow should build from the committed raw export and deploy through the GitHub Pages artifact API, not a branch.

**Recommended Structure**
```text
.
├── .github/
│   └── workflows/
│       ├── docs-check.yml
│       └── pages.yml
│
├── config/
│   └── cme.env.example
│
├── confluence/
│   └── raw/
│       ├── confluence-lock.json
│       └── ...                         # Unmodified CME output
│
├── docs/
│   ├── index.md                       # Optional repository-owned pages
│   ├── assets/
│   │   └── stylesheets/
│   │       └── extra.css
│   └── generated/                     # Generated from confluence/raw
│
├── scripts/
│   ├── export.py
│   └── prepare.py
│
├── tests/
│   └── test_prepare.py                # Add only when transformations warrant it
│
├── .gitignore
├── .python-version
├── mkdocs.yml
├── pyproject.toml
├── README.md
└── uv.lock
```

MkDocs generates:

```text
site/
```

`site/` should be ignored and never committed.

## Directory Roles

### `confluence/raw/`

Store the complete, unmodified CME export here, including:

- Exported Markdown
- Attachments
- `confluence-lock.json`

Commit this directory to Git.

That allows:

- Pull requests to show content changes from Confluence
- GitHub Actions to build without Confluence credentials
- Builds to remain reproducible
- The website to be rebuilt from any historical commit
- Export and publication to remain separate security boundaries

Do not manually edit anything under `confluence/raw/`. Treat it as imported source data.

I would not put this under `docs/`, because MkDocs would otherwise consider raw pages publishable content.

### `docs/generated/`

This is the normalized MkDocs input produced by `scripts/prepare.py`.

The preparation step should:

- Delete and recreate `docs/generated/`
- Select the desired exported page subtree
- Flatten redundant CME directory levels
- Rename the root document to `index.md` if appropriate
- Copy attachments into a predictable location
- Rewrite relative attachment links
- Rewrite Confluence-relative `/wiki/...` links to absolute URLs
- Convert supported Confluence/GitHub callouts to Material admonitions
- Report inaccessible pages and links outside the export
- Avoid changing prose

Whether `docs/generated/` should be committed is a tradeoff. I recommend **not committing it** initially. It is deterministic build output and should be created both locally and in CI.

Add it to `.gitignore`:

```gitignore
site/
docs/generated/
```

### `docs/`

Reserve this for actual MkDocs input.

Repository-maintained content can live directly under `docs/`, for example:

```text
docs/
├── index.md
├── about.md
├── assets/
└── generated/
```

There are two reasonable homepage choices:

- `docs/index.md` is a short repository-owned landing page linking into the generated documentation.
- `scripts/prepare.py` generates `docs/index.md` directly from the Confluence root page.

I recommend the first option. A small repository-owned landing page gives you control over the public homepage without modifying exported content.

### `scripts/`

Use Python scripts rather than shell scripts for path handling. The export contains spaces, Norwegian characters, URL encoding, and deeply nested paths, all of which are easier to handle safely with `pathlib`.

Recommended responsibilities:

```text
scripts/export.py
```

- Establish CME’s non-secret settings through environment variables
- Run `cme pages-with-descendants`
- Always target `confluence/raw/`
- Contain the canonical Confluence page URL
- Avoid manipulating the resulting files

```text
scripts/prepare.py
```

- Read only from `confluence/raw/`
- Recreate `docs/generated/`
- Normalize the export
- Validate links
- Fail on structural problems

Avoid a large general-purpose build script. `uv run mkdocs ...` is already the appropriate interface for serving and building.


## uv Setup

Use this as a non-package uv project with locked tool dependencies. This is preferable to putting version numbers directly in repeated `uvx` commands because local development and CI then use exactly the same dependency graph.

Commands become:

```bash
uv sync
uv run mkdocs serve
uv run mkdocs build --strict
uv run python scripts/export.py
uv run python scripts/prepare.py
```

The Pages build does not need CME because it builds from the committed export.


## MkDocs Configuration

Keep `mkdocs.yml` in the repository root. That is the conventional location and makes commands short:

```bash
uv run mkdocs serve
uv run mkdocs build --strict
```

Suggested starting point:

```yaml
site_name: Kvalitet i kode og koding
site_language: nb

docs_dir: docs
site_dir: site

theme:
  name: material
  language: nb
  features:
    - navigation.indexes
    - navigation.sections
    - navigation.top
    - search.highlight
    - content.code.copy

plugins:
  - search

markdown_extensions:
  - admonition
  - attr_list
  - tables
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.highlight
  - pymdownx.superfences

extra_css:
  - assets/stylesheets/extra.css

nav:
  - Hjem: index.md
  - Dokumentasjon: generated/index.md
```

Use an explicit `nav` only for the important top-level sections. Do not manually list dozens of descendant pages unless their order needs editorial control.

## Local Workflow

### Initial setup

```bash
uv sync
```

### Update from Confluence

```bash
uv run python scripts/export.py
uv run python scripts/prepare.py
uv run mkdocs build --strict
git diff
```

Commit only:

- Changes under `confluence/raw/`
- Repository-owned pages under `docs/`
- Configuration or preparation changes

Do not commit:

- `docs/generated/`
- `site/`
- CME credentials
- `.env`

### Preview

```bash
uv run python scripts/prepare.py
uv run mkdocs serve
```

### Validate exactly as CI does

```bash
uv sync
uv run python scripts/prepare.py
uv run mkdocs build --strict
```

## GitHub Actions

Use GitHub’s artifact-based Pages deployment:

```text
.github/workflows/pages.yml
```

The workflow should:

1. Check out the repository.
2. Install uv using `astral-sh/setup-uv`.
3. Install the pinned Python version.
4. Run `uv sync --locked`.
5. Run `uv run python scripts/prepare.py`.
6. Run `uv run mkdocs build --strict`.
7. Upload `site/` with `actions/upload-pages-artifact`.
8. Deploy with `actions/deploy-pages`.

The relevant structure is:

```yaml
name: Publish documentation

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read

concurrency:
  group: github-pages
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read

    steps:
      - uses: actions/checkout@v4

      - uses: astral-sh/setup-uv@v6
        with:
          enable-cache: true

      - run: uv python install

      - run: uv sync --locked

      - run: uv run python scripts/prepare.py

      - run: uv run mkdocs build --strict

      - uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    needs: build
    runs-on: ubuntu-latest

    permissions:
      pages: write
      id-token: write

    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Deploy
        id: deployment
        uses: actions/deploy-pages@v4
```

For a production repository, pin actions to full commit SHAs, with the release version in a comment. Dependabot can keep those pins updated.

In GitHub, configure:

```text
Settings → Pages → Build and deployment → Source → GitHub Actions
```

This does not create or use a `gh-pages` branch.

## Separate Pull Request Validation

Add:

```text
.github/workflows/docs-check.yml
```

Run it for pull requests affecting:

```text
confluence/raw/**
docs/**
scripts/**
mkdocs.yml
pyproject.toml
uv.lock
```

It should perform the same preparation and strict build, but not deploy. This catches:

- Broken internal links
- Missing attachments
- Invalid front matter
- Preparation regressions
- MkDocs warnings promoted to errors

## Recommended Data Flow

```text
Confluence
    │
    │ uv run python scripts/export.py
    ▼
confluence/raw/             committed source snapshot
    │
    │ uv run python scripts/prepare.py
    ▼
docs/generated/             ignored deterministic output
    │
    │ uv run mkdocs build --strict
    ▼
site/                       ignored static output
    │
    │ upload-pages-artifact
    ▼
GitHub Pages                artifact deployment, no branch
```

The key design decision is to commit the raw export but regenerate both `docs/generated/` and `site/`. This preserves provenance, keeps generated transformations out of reviews, avoids Confluence credentials in GitHub Actions, and makes the published result reproducible from the repository.

---

