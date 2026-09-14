
# Bruk av pull requests

Status: <mark style="background: #baf3db;">I BRUK</mark>

[Bruk av pull requests](Bruk%20av%20pull%20requests.md)  
[Bruk av pull requests](Bruk%20av%20pull%20requests.md)  
[Bruk av pull requests](Bruk%20av%20pull%20requests.md)  
[Hvordan bruke pull request på GitHub?](Bruk%20av%20pull%20requests/Hvordan%20bruke%20pull%20request%20på%20GitHub_.md)

## Hva er en pull request?

> [!IMPORTANT]
> En *pull request* (ofte forkortet til PR) er en forespørsel om å få noen andre til å se over og vurdere endringer du har gjort i koden. Det tilsvarer å sende et dokument til kollegene dine for gjennomgang før det publiseres eller tas i bruk. I stedet for tekst i et Word-dokument, handler det her om kode.

## Hvordan fungerer en pull request, i korte trekk?

1. Du gjør endringer i et "utkast" av koden, ofte kalt en *branch,* som er separat fra main branchen av repoet.
2. Når du er ferdig med endringene, oppretter du en pull request for å be andre om å sjekke arbeidet ditt.

   1. Det kjøres automatiserte tester og sjekk av kodekvalitet når man oppretter en pull request, hvis repoet er konfigurert for det. Det gjelder blant annet statistikk-repoer opprettet etter august 2024, eller som er oppdatert med endringer fra statistikkrepomalen.
3. Andre personer på teamet kan reviewe koden:

   1. Lese gjennom koden for å se om alt gir mening.
   2. Kommentere hvis noe må forbedres eller forklares.
   3. Stille spørsmål hvis noe er uklart
4. Når alle er enige om at endringene er gode, blir de slått sammen (merge) med main branchen av repoet.

## Hvorfor bør man bruke pull request?

1. **Kvalitetssikring**: Pull requests hjelper til med å oppdage feil eller forbedringsmuligheter før endringene blir en del av den endelige koden.
2. **Læring og samarbeid**: Det gir teammedlemmer en mulighet til å dele innsikt, stille spørsmål og lære av hverandre.
3. **Dokumentasjon**: Hver pull request inneholder en beskrivelse av hva som er endret og hvorfor, slik at det blir enklere å forstå hva som har skjedd senere.
4. **Trygghet**: I stedet for å endre noe direkte, gir en pull request en mulighet til å teste endringene i en kontrollert setting før de blir en del av det ferdige prosjektet.
