---
tags:
  - github-actions
  - test
  - github
  - howto-kvakk
---

# Hvordan automatisere tester med GitHub Actions?

Status: <mark style="background: #baf3db;">I BRUK</mark>

## Hva er GitHub Actions?

GitHub Actions er et system på GitHub som lar deg automatisere oppgaver relatert til koden din. Tenk på det som et verktøy som automatisk kan kjøre skript eller kommandoer når noe skjer i GitHub-repoet ditt, for eksempel at du oppretter en *pull request*, merger en *branch* eller lignende.

Det virker ved at du oppretter en mappe, `.github/workflows/` i GitHub-repoet ditt. I mappen oppretter du arbeidsflyt-filer i [yaml-format](https://simple.wikipedia.org/wiki/YAML), og som beskriver hva hvert enkelt steg skal gjøre.

En GitHub Actions arbeidsflyt består typisk av følgende deler:

1. Et punkt som sier hvilken hendelse eller hva som skal gjøre at arbeidsflyten kjøres. For eksempel en *pull request*, en *push*, et bestemt klokkeslett osv.
2. Informasjon om på hva slags og hvilken versjon av operativsystem arbeidsflyten skal kjøres (Linux, Windows, Mac).
3. En eller flere jobber, som igjen består av en eller flere steg. Typiske steg for en jobb er:

   1. Installer nødvendige verktøy som “maskinen” din må ha. I utgangspunktet får du en tilnærmet blank maskin, så ting som R og python osv. må installeres.
   2. Klon ut koden fra GitHub-repoet ditt.
   3. Installer pakkene som koden din er avhengig av (poetry install).
   4. Kjør de kommandoene du vil kjøre for å sjekke eller teste koden din. For eksempel pytest.

Det finnes ferdige GitHub Actions for en rekke vanlige steg, slik som å clone ut repo, installere python osv., og disse kan vi gjenbruke som vist nedenfor. For R er det automatisk oppsett av GitHub actions og nødvendige filer med hjelp av `usethis`.

For flere detaljer og oversikt, se<https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions>

## GitHub Actions og testing for Python

Repoet tech-coach-examples inneholder et eksempel på en arbeidsflyt som gjør testing med pytest, i arbeidsflyten [tests.yml](https://github.com/statisticsnorway/tech-coach-examples/blob/main/.github/workflows/tests.yml). Dette eksemplet vil komme med automatisk når man lager nye repoer med `ssb-project` fra høsten 2024. Her er noen utdrag og forklaringer:

```java
name: Tests

on:
  push:
    branches:
      - main
      - master
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest
```

Linje 3-9 sier når arbeidsflyten skal kjøres. I dette tilfellet når noe *pushes* til *branchene* main eller master, enten direkte eller som følge av en merge, og i tillegg også på hver *pull request*.

Linje 12 sier denne arbeidsflyten skal kjøres på linux (den siste versjonen av ubuntu-distribusjonen).

```java
jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - name: Check out the repository
        uses: actions/checkout@v4

      - name: Install Poetry
        run: |
          pipx install poetry
          poetry --version

      - name: Set up Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"
          cache: "poetry"

      - name: Install dependencies
        run: poetry install --no-root

      - name: Run tests
        run: poetry run pytest -v --cov --cov-report=term-missing --cov-report=xml
```

På de enkelte stegene så ser vi på linje 6-7 og linje 14-18 eksempel på gjenbruk av en eksisterende GitHub Actions for å clone ut et repo og installere python.

Linje 9-12 og linje 24 viser hvordan vi kan kjøre egne kommandoer.

## GitHub Actions og testing for R

Vi anbefaler at du bruker `testthat` for å sette opp og kjøre tester i R lokalt. Se [Eksempler på enhetstester i R](Eksempler%20på%20enhetstester%20i%20R.md) for hjelp til oppsett.

Deretter kan du **opprette en workflow** for å automatisk kjøre R testene dine hver gang du pusher til GitHub ved å bruke `usethis`:

```java
usethis::use_github_action("check-standard")
```

Dette oppretter en GitHub Actions workflow som kjører testene dine automatisk ved hver push.

**Commit og push** den nye workflow-filen (`R-CMD-check.yaml`) til GitHub. Nå vil testene dine kjøre automatisk hver gang du pusher kode.

Dette sikrer at koden din testes kontinuerlig og at feil oppdages tidlig!
