
# Eksempler på enhetstester i R

Testing er en essensiell del av utviklingsprosessen for å sikre at koden fungerer som forventet. I R er [testthat](https://testthat.r-lib.org/) et populært verktøy for å skrive og kjøre tester. Denne introduksjonen vil guide deg gjennom hvordan du setter opp testing i et R-prosjekt ved hjelp av [testthat](https://testthat.r-lib.org/) og [usethis](https://usethis.r-lib.org/index.html).

#### Steg 1: Installere `testthat` og `usethis`

Først må du installere `testthat` og `usethis` dersom du ikke allerede har gjort det. Dette kan gjøres ved å kjøre følgende kommandoer i R:

```java
renv::install("testthat")
renv::install("usethis")
```

#### Steg 2: Sett opp testing struktur

Med `usethis` kan du enkelt sette opp strukturen for testing i prosjektet ditt. Kjør følgende kommando i ditt prosjekt for å konfigurere `testthat`:

```java
usethis::use_testthat()
```

Dette vil opprette en `tests`-mappe i prosjektet ditt med en undermappe kalt `testthat`, samt en testfil som heter `testthat.R`.

```java
my_project\
├── src/
│   ├── __init__.py
│   ├── examples/
│   │   ├── __init__.py
│   │   └── example1.py
├── tests/
│   ├── testthat/
│   │   ├── test-example.R
│   └── testthat.R
└── README.md
```

#### Steg 3: Skrive tester

Nå kan du begynne å skrive tester for funksjonene dine. Her er en eksempel funksjon `add_floats`:

```java
add_floats <- function(x, y){
  x + y
}
```

Lag en ny testfil i `tests/testthat`-mappen. En vanlig konvensjon er å navngi testfilene som `test-<funksjonsnavn>.R`. For eksempel, hvis du tester `add_floats`, kan du opprette en fil som heter `test-add_floats.R`.

Inne i denne filen kan du skrive tester ved å bruke `test_that` funksjonen. Her er et eksempel:

```java
library(testthat) 

test_that("add_floats summere korrekt", { 
  result <- add_floats(2, 3) 
  expect_equal(result, 5) 
  
  result <- add_floats(-1, 1) 
  expect_equal(result, 0) 
  })
```

#### Steg 4: Kjøre tester manuelt

For å kjøre alle testene i prosjektet ditt, kan du bruke følgende kommando:

```java
testthat::test_dir("tests/testthat")
```

Alternativt, i RStudio, kan du klikke på "Build" fanen og deretter "Test Package" hvis du har et pakkeprosjekt.

#### Steg 5: Sette opp automatisk testing med GitHub Actions

Hvis prosjektet er organisert som en pakke kan `usethis` også sette opp GitHub Actions for deg. Dette vil automatisk sjekke pakken og alle tester hver gang en pull request til main branch opprettes. Dette kan settes opp med følgende kommando:

```java
usethis::use_github_action("check-standard")
```

Denne kommandoen oppretter en GitHub Actions workflow som kjører testene dine automatisk. Den lager en `.github/workflows/R-CMD-check.yaml` fil med oppsett for å kjøre `R CMD check`.

Commit og push endringer til github. Husk at du må har en PAT som har workflow priveldges for å kunne pushe dette til github.
