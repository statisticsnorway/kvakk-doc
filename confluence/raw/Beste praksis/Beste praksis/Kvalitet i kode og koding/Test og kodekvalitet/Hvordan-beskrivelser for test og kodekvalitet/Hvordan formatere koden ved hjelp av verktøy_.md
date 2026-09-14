
# Hvordan formatere koden ved hjelp av verktøy?

Status: <mark style="background: #baf3db;">I BRUK</mark>

## Introduksjon

Det finnes en del verktøy som kan formatere koden din automatisk. Det gjør at koden blir mer konsistent, lesbar og følger språkets konvensjoner, og i tillegg sparer du tid og reduserer sannsynligheten for merge-konflikter. Derfor er det en [Page not accessible (ID: 3911745551)].

## Python

I python er tre hovedverktøy vi bruker for å sikre konsistent formattering av koden:

1. [black](https://black.readthedocs.io/en/stable/): Formaterer koden i henhold til [python stilguide (PEP8)](https://peps.python.org/pep-0008/) og python-konvensjoner.
2. [isort](https://pycqa.github.io/isort/): Sorterer importene dine alfabetisk i logiske blokker og en import per linje. Gir mindre sannsynlighet for merge-konflikter.
3. [pre-commit](https://pre-commit.com/): Et verktøy som brukes for å kjøre sjekker før du comitter, men inneholder også en del ferdigdefinerte sjekker, slik som at det ikke er blanke tegn på slutten av linja, at du ikke har lagt til store filer osv. Vi har en egen [pre-commit](../../../../../Avdelingen%20for%20IT/Avdelingen%20for%20IT%20Home/S703%20%20-%20IT%20Partner/Team%20tech%20coach/Veiledninger/Verktøy%20som%20brukes%20av%20SSB-mal%20for%20python-biblioteker/pre-commit.md) med mer informasjon om bruk av dette verktøyet.

### Konfigurasjon

Noen av verktøyene krever installasjon og konfigurasjon for å virke som de skal. Fra slutten av august 2024 vil de som oppretter nye repoer med `ssb-project` kommandoen få dette ferdig satt opp.

For andre, installer de nødvendige pakkene med kommandoene:

```bash
poetry add -G dev black -E jupyter
poetry add -G dev isort pre-commit pre-commit-hooks
```

Isort trenger litt oppsett: Kopier [følgende oppsett](https://github.com/statisticsnorway/tech-coach-examples/blob/main/pyproject.toml#L50-L57) inn i `pyproject.toml`-filen i ditt repo.

pre-commit: Opprett en fil som heter `.pre-commit-config.yaml` i rot-mappen på repoet ditt og kopier [følgende oppsett](https://raw.githubusercontent.com/statisticsnorway/ssb-project-template-stat/main/%7B%7Bcookiecutter.project_name%7D%7D/.pre-commit-config.yaml) inn i den.

### Bruk

Du kan kjøre verktøyene hver for seg, slik som dette (fra rot-mappen i repoet ditt):

```bash
poetry run black .
poetry run isort .
```

Eller du kan kjøre alle sjekkene samtidig med kommandoen:

```bash
poetry run pre-commit run --all-files
```

## R

![styler.png](../../../../attachments/1ea6d4a3-8852-437e-b8a4-5d205f391a72.png)

R pakken, [styler](https://github.com/r-lib/styler), hjelper med å formatere R-kode i henhold til spesifikke stilguide. Den lar deg automatisk rydde opp i koden din slik at den følger en konsekvent stil, som gjør koden lettere å lese og vedlikeholde. Pakken støtter flere forskjellige stil, men vi anbefaler alle i SSB til å bruke standarden fra *tidyverse*, som er default stil i pakken.

### Bruk

`styler` kan brukes til å formatere individuelle filer, hele prosjekter eller til og med spesifikke kodeblokker i R. For å ta i bruk pakken må du først installere det i prosjektet med

```java
renv::install("styler")
```

Etterpå kan du ta det i bruk pakken lokalt. For å kjøre styling for en fil:

```java
styler::style_file("<filnavn>")
```

Eller for å kjøre styling for et helt prosjekt kan du kjøre:

```java
styler::style_dir()
```

Se [denne bloggen om styler for mer detaljer om pakken](https://www.tidyverse.org/blog/2017/12/styler-1.0.0/).

### Automatisering med GitHub actions

Vi anbefaler at du setter opp GitHub Actions for å automatisere kjøring av `styler` når du pusher kode til GitHub. Dette kan enkelt gjøres med én kommando

```java
usethis::use_github_action("style")
```

Dette oppretter en ny GitHub Actions workflow som heter `style.yaml`. Commit og push den nye filen til GitHub, så vil alle R- og Rmd-filer automatisk formateres når de pushes til GitHub.

[Hvordan formatere koden ved hjelp av verktøy?](Hvordan%20formatere%20koden%20ved%20hjelp%20av%20verktøy_.md)
