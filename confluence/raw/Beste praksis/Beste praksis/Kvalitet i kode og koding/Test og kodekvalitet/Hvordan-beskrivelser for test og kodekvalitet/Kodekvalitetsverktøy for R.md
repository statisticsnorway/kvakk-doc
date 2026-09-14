
# Kodekvalitetsverktøy for R

| <mark style="background: #ffffff;">&nbsp;</mark>   |
|----------------------------------------------------|

## Introduksjon

Mens SonarCloud brukes i SSB for analyse av Python kode i projekter, er den foreløpig ikke tilgjengelig for R. Men det finnes andre verktøy som kan benyttes for å analysere kvaliteten av R-kode. Følgende er tre pakker vi anbefaler å bruke.

- `styler` for formattering (se veiledning her: [Hvordan formatere koden ved hjelp av verktøy?](Hvordan%20formatere%20koden%20ved%20hjelp%20av%20verktøy_.md) )
- `lintr` for å sjekke kode for potensielle feil og forbedringsmuligheter.
- `covr`for å kontrollere dekning av testene

## Linting med `lintr`

`lintr` er en R-pakke som brukes for å kjøre **linting**, som innebærer å automatisk sjekke kode for potensielle feil og forbedringsmuligheter. Den hjelper deg med å opprettholde en konsistent kodestil og forbedre lesbarheten i prosjektet ditt.

Når du bruker `lintr` i et R-prosjekt, kan du oppdage problemer som ubrukte variabler, lange linjer eller feil bruk av operatorer, og få forslag til hvordan du kan forbedre koden. `lintr` inkluderer funksjoner for kompleksitetsanalyse som lar deg måle og overvåke kodekompleksitet, slik at du kan identifisere og forbedre kompliserte eller ineffektive kodebiter. Dette gjøre det lettere å vedlikehold koden din.

> [!IMPORTANT]
> `lintr` endrer ikke koden din når du bruker pakken; den er kun ment å gjøre deg oppmerksom på forbedringsmuligheter.

### Bruk

For å bruke `lintr` i prosjektet ditt, kan du installere og ta i bruk pakken:

```java
renv::install("lintr")
library(lintr)
```

For å få en analyse av prosjektet ditt kjøre du

```java
lintr::lint_dir()
```

Da få du en liste av mulige problemer i koden din som du kan jobbe videre med.

Se <https://lintr.r-lib.org/articles/lintr.html> for mer informasjon om bruk av `lintr`.

### Automatisering med GitHub Actions

For å sette opp automatisk linting av R-prosjektet ditt med GitHub Actions, kan du bruke `usethis`-pakken:

I R, kjør følgende kommando for å opprette en GitHub Actions workflow for linting:

```java
usethis::use_github_action("lint-project")
```

Dette oppretter en workflow-fil i `.github/workflows`-mappen i prosjektet ditt, som typisk heter `lint-project.yaml`.

> [!IMPORTANT]
> Hvis du ønsker kun å få varsler om mulige feil ved lint kjøring og at det ikke sendes en feilmelding kan du åpne lint-project.yaml fil og sjekk at det står:
>
> `LINTR_ERROR_ON_LINT: false`

Commit og push den nye filen til GitHub-repositoriet ditt. Workflowen vil nå automatisk kjøre linting på koden din hver gang du pusher endringer eller oppretter en pull request, og hjelpe deg med å opprettholde en god kodestil.

## Test dekning med `covr`

![covr.png](../../../../attachments/556d76e7-1072-4c72-8111-7db8abe579c4.png)

`covr` er en R-pakke som brukes til å måle **testdekning** i prosjekter. Testdekning refererer til hvor stor andel av koden som dekkes av enhetstester. `covr` hjelper deg med å se hvilke deler av koden som ikke er testet, slik at du kan forbedre testene dine og sikre at koden fungerer som forventet.

### Bruk

Sett opp testing av kode med pakken `testthat` før du kjøre analyse av testdekning. Dette kan du gjøre ved å følge [Eksempler på enhetstester i R](Eksempler%20på%20enhetstester%20i%20R.md)

For å analysere dekning i et prosjekt med hjelp av `covr` må du installere pakken fra CRAN:

```java
renv::install("covr")
```

Deretter kan du kjøre analyse av testdekning til et prosjekt med:

```java
rapport <- covr::package_coverage()
```

Dette vil gi deg en oversikt over hvor mye av koden i hele prosjektmappen som er dekket av tester, og hvor det mangler dekning. Her lagre vi rapport til et objekt for å analysere videre om ønskelig.

Det kan være nyttig å se på hvilke linjer er ikke testet. Du kan se dette ved å kjøre

```java
covr::zero_coverage(rapport)
```

[Kodekvalitetsverktøy for R](Kodekvalitetsverktøy%20for%20R.md)
