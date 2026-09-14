---
tags:
  - sonarcloud
---

# SonarQube Cloud kodekvalitetsverktøy

Status: <mark style="background: #baf3db;">I BRUK</mark>

> [!IMPORTANT]
> [SonarQube Cloud](https://sonarclud.io/) er et kodekvalitetsverktøy som SSB har lisens på. Det het tidligere SonarCloud, men er akkurat det samme verktøyet. Denne siden beskriver hvordan du logger inn, setter opp analyse av et GitHub-repo og bruker analysene til å forbedre koden. SoanrCloud støtter Python, Java og [en rekke andre språk](https://docs.sonarcloud.io/advanced-setup/languages/overview/), men ikke R.

> [!WARNING]
> Vil du bruke SonarQube Cloud til å analysere Jupyter Notebooks, så må du lagre filene som rene .py-filer, og ikke i .ipynb-format. Det kan du gjøre ved hjelp av verktøyet jupytext, se beskrivelse [Hvordan lagre Jupyter notebooks i rent tekstformat?](../../../../../Avdelingen%20for%20IT/Avdelingen%20for%20IT%20Home/S703%20%20-%20IT%20Partner/Team%20tech%20coach/Veiledninger/Hvordan%20lagre%20Jupyter%20notebooks%20i%20rent%20tekstformat_.md).

**Innholdsfortegnelse**

## Login

Du trenger ikke å opprette noen bruker, bare logg inn med GitHub-kontoen din.

Se video:



## Hvordan sette opp analyse av et nytt GitHub-repo?

Du kan velge mellom to analysemetoder: Automatisk eller med GitHub Actions. De fleste klarer seg med automatisk, og det er det som er vist i videoen nedenfor. Det du mister med automatisk metode er at du ikke får informasjon om hvor mye og hvilke deler av koden som er dekket av tester og/eller kjøringer.

Se video:



## Hvordan bruke SonarQube Cloud-analyser til å forbedre koden?

Se video:



## Konfigurasjon og ekskludering av mapper

I noen tilfeller ønsker man å ekskludere enkelte mapper fra analyse eller fra duplikatsjekk. Det kan for eksempel være at man har en `experimental`-mappe hvor man bare tester ut ting, og som ikke er en del av produksjonskoden.

Det er to filer hvor dette kan angis, avhengig av om repoet ditt er satt opp med automatisk analyse (typisk for statistikk-repoer), eller analyse med GitHub actions (typisk for biblioteker).

- `.sonarcloud.properties`: Se [eksempel](https://github.com/statisticsnorway/tech-coach-demo/blob/main/.sonarcloud.properties).
- `sonar-project.properties`: Se [eksempel](https://github.com/statisticsnorway/ssb-pypitemplate-instance/blob/main/sonar-project.properties).

## Mer dokumentasjon

Dokumentasjonen til SonarQube Cloud finner du på lenken: <https://docs.sonarsource.com/sonarqube-cloud/>
