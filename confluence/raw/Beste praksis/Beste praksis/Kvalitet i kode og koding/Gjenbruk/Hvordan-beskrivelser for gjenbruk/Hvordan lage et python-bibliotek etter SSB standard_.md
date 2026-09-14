---
tags:
  - python
  - bibliotek
  - pypitemplate
  - pypi
---

# Hvordan lage et python-bibliotek etter SSB standard?

Status: <mark style="background: #baf3db;">I BRUK</mark>

> [!IMPORTANT]
> Tenk deg at du har en eller flere funksjoner som bør deles med andre som ikke jobber i det samme git-repoet som deg. Hvordan gjør du det etter god SSB-standard?
>
> Denne siden tar den gjennom denne prosessen, helt fram til at biblioteket er publisert på PyPI. Python Package Index ([PyPI](https://pypi.org/)) er sted for publisering og nedlasting av python-biblioteker. Kort fortalt går prosessen ut på å bruke en mal for SSB PyPI-biblioteker som vi har laget.

**Innholdsfortegnelse**

## Før du starter

Sjekk om de funksjonene du ønsker å dele kan passe å legge til i et av de SSB PyPI-bibliotekene vi allerede har. Ta kontakt med kontaktperson for biblioteket. Du finner en liste over noen sentrale egenutviklede biblioteker under [Godkjentliste for statistikkproduksjon på Dapla](../../../../../Arkitektur/Arkitektur/Valg%20av%20teknologi/Godkjentliste%20for%20statistikkproduksjon%20på%20Dapla.md). Se også [listen over SSB utviklede python og R-kodebiblioteker](https://trygu.github.io/ssb-pypi-statistics/).

Eller søk på [PyPI](https://pypi.org/) etter biblioteker med prefiks `ssb-`. Hvis det ikke passer i noen av de eksisterende bibliotekene, så lager du du et nytt bibliotek ved å lese videre i denne beskrivelsen.

Neste punkt er å velge et navn for git-repoet koden til biblioteket skal ligge i. I følge [navnstandard for GitHub-repoer](https://github.com/statisticsnorway/adr/blob/main/docs/0014-navnestandard-github-repoer.md) skal git-repo navn for fellesbiblioteker begynne med `ssb-`. Pass på at navnet er ledig ved å søke etter navnet på [GitHub](https://github.com/statisticsnorway/), [PyPI](https://pypi.org/) og [TestPyPI](https://test.pypi.org/).

### Krav til python biblioteker

Gruppen Kvalitet i kode og kode (KVAKK) har satt opp noen krav og anbefalinger til python-biblioteker som lages i SSB. Se [Regler og anbefalinger fra KVAKK](../../Regler%20og%20anbefalinger%20fra%20KVAKK.md). Det går på ting som navnestandard, kodekvalitetssjekker, dokumentasjon og testing. Malen nedenfor dekker alle disse retningslinjene.

### Opprett bruker på PyPI og TestPyPI

Du trenger å opprette en bruker på både PyPI og TestPyPI hvis du ikke har det fra før. Prosessen for å opprette en bruker er slik:

1. Åpne siden [PyPI](https://pypi.org/) eller [TestPyPI](https://test.pypi.org/) og velg *Register* oppe til høyre. Da vises det et skjema du skal fylle ut.
2. På *email address* anbefales det å oppgi SSB e-postadressen din. På *username* anbefales det å bruke GitHub brukernavnet ditt. Eksempel: ola.nordmann@ssb.no og olano-ssb. Fyll ut resten og klikk på *Create account*-knappen.
3. Du vil etter en stund få en e-post som ber deg om å verifisere e-postadressen din. Sjekk at avsender er [pypi.org](http://pypi.org) eller [test.pypi.org](http://test.pypi.org) og klikk på linken i e-posten for å verifisere e-postadressen.
4. Sett opp to-faktor autentisering for kontoen din:

   1. Klikk på login-navnet ditt oppe til høyre og velg *Account settings*.
   2. Scroll ned til overskriften *Two factor authentication* og klikk på knappen *Generate recovery codes*. Lagre kodene på et sikkert sted. Verifiser ved å oppgi en av kodene.
   3. Klikk på knappen *Add 2FA with authentication application*. Da får du opp en QR-kode. Åpne Microsoft Authenticator appen på telefonen din, klikk på pluss-tegnet øverst for å legge til en ny konto og velg “Annen konto”. Skann QR-koden med Microsfoft Authenticator appen og kontoen blir lagt til.
   4. I *verify application* feltet på nettsiden fyller du inn med koden fra den nye kontoen i Microsoft Authenticator. Etter det skal alt være i orden.
5. For PyPI: Send en e-post til [miles.winther@ssb.no](mailto:miles.winther@ssb.no) eller [arne.sorli@ssb.no](mailto:arne.sorli@ssb.no): Oppgi PyPI-brukernavnet ditt og be om at det blir lagt til organisasjonen statisticsnorway på PyPI.
6. Du vil etter en stund få en e-post som git deg en lenke til å akseptere invitasjonen til å bli med i organisasjonen statisticsnorway på PyPI. Sjekk at avsender er noreply@pypi.org og klikk på linken i e-posten for å godta invitasjonen.

### Sjekk rettighetene til ditt GitHub Personal Access Token (PAT)

Når du skal sende noe til GitHub så spør git om et passord, eller rettere sagt et token, for å autentisere deg. Dette tokenet trenger å ha *scope*: *repo* og *workflow.* Sjekk hvilke scope tokenet ditt har ved å logge inn på GitHub, klikk på ikonet ditt oppe til høyre, velg Settings, Developer settings (helt nederst til venstre), Personal access tokens og Tokens(classic).

Hvis tokenet ditt mangler et av scopene så oppdater tokenet ved å klikke på tokenet (blå tekst), legg til aktuelle scope og klikk på “*Update token*”-knappen nederst.

### Video

Video som viser del 1, før du starter:



## Mal for SSB PyPI-biblioteker

Vi har tatt utgangspunkt i en mal for python-biblioteker, basert på [artikkelserien Hypermodern Python](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769), og tilpasset den til bruk i SSB. Den dekker alle krav og anbefalinger som er nevnt ovenfor.

Malen heter `ssb-pypitemplate` og den er godt dokumentert på [dokumentasjonssiden til malen](https://statisticsnorway.github.io/ssb-pypitemplate/). Kort fortalt kjører man en kommando og svarer på en del spørsmål, og så setter den opp et ferdige filer til deg lokalt der du kjører. I tillegg er det noen steg med å få koden inn på GitHub, konfigurere repoet, og opprette en bruker på PyPI hvis du ikke har det fra før, men dette kommer vi tilbake til.

Malen er generell og kan brukes hvor som helst. Det er litt enklere hvis man kjører den på DaplaLab siden der er noen av verktøyene allerede installert. Denne beskrivelsen tar utgangspunkt at du kjører kommandoene på DaplaLab.

I utgangspunktet følger vi beskrivelsen i [QuickStart Guide](https://statisticsnorway.github.io/ssb-pypitemplate/quickstart.html). Detaljene er beskrevet i [User Guide](https://statisticsnorway.github.io/ssb-pypitemplate/guide.html).

### Opprett lokal instans av mal

1. På DaplaLab er alle verktøyene ferdig installert. På lokal PC eller andre steder må du installere noen ekstra verktøy som beskrevet i [beskrevet i QuickStart Guide](https://statisticsnorway.github.io/ssb-pypitemplate/quickstart.html#requirements). Hvis du ikke har brukt verktøyet pipx før, så må du i tillegg kjøre følgende kommando: `pipx ensurepath` Og deretter lukke terminalvinduet og åpne det på nytt. Dette for at pipx-installerte verktøy skal ligge i *path*.
2. Finn ut hva som er siste release av `ssb-pypitemplate` og noter det. Det finner du på [release-siden til ssb-pypitemplate](https://github.com/statisticsnorway/ssb-pypitemplate/releases/). Eksempel: 2026.5.27.
3. Hvis du ikke vil opprette et GitHub-repo under statisticsnorway ennå, men bare vil teste litt lokalt eller med repo under din egen GitHub-bruker: Kjør kommandoen og svar på spørsmålene som [beskrevet under Creating a project](https://statisticsnorway.github.io/ssb-pypitemplate/quickstart.html#creating-a-project). Detaljer om spørsmålene finner du under punkt 5.
4. Hvis du ønsker å opprette et GitHub-repo under statisticsnorway samtidig er det enklere å bruke `ssb-project`. La oss si at du vil lage et bibliotek for tidsserier og har bestemt deg for at det skal hete ssb-timeseries, at siste release av ssb-pypitemplate er 2026.5.27, og at GitHub-tokenet ditt er “blablabla”. Da er kommandoen:

   ```bash
   ssb-project create ssb-timeseries --template-git-url https://github.com/statisticsnorway/ssb-pypitemplate.git --checkout=2026.5.27 --no-kernel --github --github-token='blablabla'
   ```

   Husk å erstatte “ssb-timeseries” med navnet på ditt bibliotek.
5. Mange av spørsmålene har ferdig utfylte standardverdier som man bare kan godta (for de som ikke er nevnt nedenfor). Kommentarer og forklaringer til noen av spørsmålene:

   1. `Project description:` Kort beskrivelse av hva som skal ligge i repoet.
   2. `project_name:` Dette er navnet på GitHub-repoet. Det skal begynne med `ssb-`, i følge [navnstandarden](https://github.com/statisticsnorway/adr/blob/main/docs/0014-navnestandard-github-repoer.md).
   3. `package_name`: Her vil systemet foreslå navn ut fra GitHub-reponavnet. Pakker i python kan ikke inneholde bindestrek, så den er erstattet med understrek. Du kan vurderer å fjerne `ssb_` som prefiks i pakkenavnet, men da bør du sjekke at det ikke finnes noen pakke med samme navn på PyPI eller TestPyPI.
   4. `friendly_name`: Dette er det navnet som brukes i dokumentasjonen. Kan gjerne inneholde mellomrom.
   5. `author:` I denne sammenhengen betyr det kontaktperson for PyPI-biblioteket, ikke nødvendigvis den som har skrevet koden. Eksempel: “Arne Sørli”.
   6. `github_organization`: Behold standardvalget hvis det skal være et repo under statisticsnorway på GitHub. Men du kan også teste ut ting under din egen GitHub-bruker, og da angir du i stedet GitHub brukernavnet ditt her. Eksempel: arneso-ssb.
   7. `development_status`: Det varierer med hvor moden koden er, men ofte velger man “`4 - Beta`" når man oppretter et nytt bibliotek.
   8. `code_quality_level`: Her er det definert tre nivå: High, Medium og Low, og Medium er standardvalget. Nivået angir hvilke krav som settes til kodekvaliteten for at endringer skal godkjennes. Nivå High sjekker veldig mye og har krav til 80% testdekning, mens nivå Low bare sjekker de mest essensielle tingene og har kun krav til 20% testdekning.
   9. `dependency_manager_tool`: Standard er poetry. På repoer som tilhører IT-avdelingen er uv et alternativ.
   10. `maintainer department`: Seksjonsnummer til den seksjonen som skal eie biblioteket.
6. Hvis du får advarsel om at git configurasjonen ikke er riktig, så svar “n” på spørsmålet om å resette konfigurasjonen.

### Lokal sjekk

Sjekk at alt virker lokalt ved å installere det virtuelle miljøet til biblioteket og kjøre testene som beskrevet i [Quickstart Guide](https://statisticsnorway.github.io/ssb-pypitemplate/quickstart.html#installing-the-environment). Der brukes verktøyet [nox](https://nox.thea.codes/en/stable/) til å kjøre en rekke tester på koden og kodedokumentasjonen, samt at man installerer sjekker som kjøres før hver gang man comitter.

Kort fortalt:

1. Åpne et terminalvindu og gå til katalogen hvor repoet ligger.
2. Kjør kommandoen `poetry install`
3. Kjør kommandoen `nox`

### Konfigurering av GitHub-repo

> [!IMPORTANT]
> Målet er at konfigureringen av GitHub-repoet skal kunne settes opp automatisk av `ssb-project`, men vi er ikke helt der ennå for public repoer.

1. Det settes en del krav til hvordan et public GitHub repo i SSB skal være konfigurert. se [ADR0006](https://github.com/statisticsnorway/adr/blob/main/docs/0006-aapen-kildekode-i-ssb.md#kriterier-for-%C3%A5pen-kildekode). Sørg for at disse er oppfylt. Se beskrivelse av [Hvordan opprette nytt GitHub-repo?](../../Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20opprette%20nytt%20GitHub-repo_.md) for detaljer, og legg til hvem som skal ha tilgang til repoet (beskrivelse på forrige lenke).
2. Send en e-post til [sikkerhetssenter@ssb.no](mailto:sikkerhetssenter@ssb.no) og be om at repoet gjøres public.
3. Etter at repoet er public, gjennomfør resterende konfigurasjon som beskrevet på siden [Hvordan konfigurere et public GitHub-repo for biblioteker?](../../Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20konfigurere%20et%20public%20GitHub-repo%20for%20biblioteker_.md).

### Oppsett av PyPI og TestPyPI

Nye releaser av biblioteket publiseres automatisk til PyPI og TestPyPI fra GitHub-repoet ved hjelp av GitHub Actions. Autentisering gjøres med en metode som kalles *Trusted Publiser*, og den settes opp som [beskrevet i QuickStart Guide](https://statisticsnorway.github.io/ssb-pypitemplate/quickstart.html#pypi).

### Oppsett av SonarQube Cloud

Se [beskrivelse i Quick Start Guide](https://statisticsnorway.github.io/ssb-pypitemplate/quickstart.html#sonarcloud).

Det er for tiden en feil i SonarQube Cloud som gjør at du må opprette et sonar token manuelt når du skal sette opp GitHub actions som analysemetode. Følg beskrivelsen her: [Hvordan opprette Sonar token manuelt?](SonarQube%20Cloud%20kodekvalitetsverktøy/Hvordan%20opprette%20Sonar%20token%20manuelt_.md)

I tillegg anbefales det å endre *Quality Profile* og *Quality Gate* for prosjektet i SonarQube Cloud for å gjøre sjekkene bedre tilpasset ssb-biblioteker.

Logg inn i SonarQube Cloud, gå til prosjektet ditt, og velg *Administration* nede til venstre. Der velger du så *Quality Profiles*, skroller ned til du finner Python og setter den til *Sonar way*. Standard *quality profile* for python er Jupyter, og den har fjernet en del sjekker vi ønsker å ha for biblioteker. Endre den til *Sonar way.*

Standard *Quality Gate* kan være litt for streng for det vi har satt som standard i malen. Den krever blant annet 80% testdekning på ny kode. Du kan endre den til ssb-lib-medium. Det gjør du ved å logge inn i SonarQube Cloud, gå til prosjektet ditt, og velg *Administration* nede til venstre. Der velger du så *Quality Gate* og skroller ned i listen til du finner ssb-lib-medium og velger den.

### Video

Video som viser del 2, bruk av malen:



## Egen kode

### Legg inn egen kode

Eksempel: La oss si at du har en funksjon som sjekker om et tall er et primtall, og ønsker å legge den inn i biblioteket. Funksjonen du har kan se ut noe som dette:

```py
from math import sqrt

def is_prime(number):
    if number <= 1:
        return False
    return all(number % i != 0 for i in range(2, int(sqrt(number)) + 1))

```

Funksjoner og klasser du vil ha i biblioteket legges inn under katalogen `src/<pakkenavn>/`, eksempel: `src/ssb_libtest1/` Der finnes det allerede en fil, `functions.py`, som du kan legge inn funksjonen i. Eller du kan lage en ny fil hvis du ønsker det, men i eksempelet har vi brukt `functions.py`. Lagre fila.

### Test og fiks

For å sjekke alt virker som det skal med den nye koden, at den er riktig formattert, overholder krav osv. så kjør følgende kommando i et terminalvindu, fra rotkatalogen på repoet:

```bash
nox
```

Da vil du se at det rapporteres to feil: Verktøyet `ruff` sier i fra at koden mangler grenesnittdokumentasjon, og verktøyet `mypy` sier i fra at koden mangler *type hint*. Begge deler ting som er listet opp under krav og anbefaling for biblioteker, se: [Regler og anbefalinger fra KVAKK](../../Regler%20og%20anbefalinger%20fra%20KVAKK.md)og [Regler og anbefalinger fra KVAKK](../../Regler%20og%20anbefalinger%20fra%20KVAKK.md) Se hvordan-beskrivelsen under disse reglene og anbefalingene for hvordan du kan fikse dette.

Erstatt koden med den som er vist nedenfor, så løses problemene.

```py
from math import sqrt


def is_prime(number: int) -> bool:
    """Check if the given number is a prime number.

    Args:
        number: The number to check.

    Returns:
        True if the number is a prime number. False otherwise.
    """
    if number <= 1:
        return False
    return all(number % i != 0 for i in range(2, int(sqrt(number)) + 1))
```

Kjør `nox` på nytt og sjekk at ingenting feiler. Deretter oppretter du en ny branch for endringene (hvis du ikke alt har gjort det), legg til de endrede filene i git, comitter og pusher til GitHub:

```java
git switch -c is-prime-function
git add -u
git commit -m"Add function is_prime"
git push
```

### Pull request og merge

Logg inn på repoet på GitHub og opprett en pull-request.

Tips:

- Vent med å legge til *Reviewers* til du ser at alle sjekker er “grønne”. Noen av testene kjøres først når du oppretter en pull-request, slik som kjøring med forskjellige python-versjoner, plattformer og SonarQube Cloud. Det er greit å sjekke at alt dette går gjennom før du ber noen se på koden, slik at de slipper å se på den flere ganger.
- Legg til Labels på pull-requesten som sier noe om hva slags type endringer det er snakk om, for eksempel om det er bug, dokumentasjon, ny funksjonalitet eller lignende. Det gjør at at pull requestene blir gruppert fint i automatisk generert release notes.

Når pull requesten er godkjent, så merger du den og sletter branchen. Biblioteket blir da publisert til TestPyPI og dokumentasjonen til GitHub Pages. Linken til dokumentasjonen er: `statisticsnorway.github.io/<repo name>` Sjekk at dokumentasjon og biblioteksiden på TestPyPI ser ut som forventet.

### Lag en release

Se beskrivelse om [releasing](https://statisticsnorway.github.io/ssb-pypitemplate/quickstart.html#releasing) i Quickstart Guide. Kort fortalt er det så enkelt som å endre versjonsnummeret i `pyproject.toml`. Da detekterer en GitHub action at det er snakk om en ny release. Den tagger releasen og lager en release på GitHub med automatisk generert release notes, og publiserer biblioteket til PyPI istedenfor TestPyPI.

Stå på en oppdatert main-*branch* og kjør kommandoer ala dette:

```bash
git switch main
git pull
git switch -c release
poetry version patch          # eller endre versjonsnummeret i pyproject.toml manuelt
git add -u
git commit -m"Release 0.0.1"  # eller det versjonnummeret du ønsker
git push
```

Deretter pull-request og merge som beskrevet ovenfor. Da blir biblioteket publisert på PyPI.

### Overføring til statisticsnorway-organisasjon på PyPI

Biblioteket skal nå overføres til statisticsnorway-organisasjonen på PyPI. Det gjør du slik:

1. Logg inn på PyPI og klikk på profilen din oppe til høyre og velg *Your Projects*.
2. Klikk på *Manage* på det biblioteket du vil overføre til statisticsnorway-organisasjonen på PyPI.
3. Klikk på Collaborators i menyen til venstre, og nederst på siden inviterer du enten Arne Sørli eller Miles Winther, PyPI-brukernavn arneso-ssb eller mmwinther, med rollen *owner* på repoet.
4. De vil motta en e-post og så legge repoet til statisticsnorway på PyPI.

### Video

Video som viser del 3, legge inn egen kode i malen:



## Veien videre

Vi har laget noen sider som samler veiledninger og nyttige tips og triks om de verktøyene som brukes mest av SSB-malen for python-biblioteker, se [Verktøy som brukes av SSB-mal for python-biblioteker](../../../../../Avdelingen%20for%20IT/Avdelingen%20for%20IT%20Home/S703%20%20-%20IT%20Partner/Team%20tech%20coach/Veiledninger/Verktøy%20som%20brukes%20av%20SSB-mal%20for%20python-biblioteker.md)

Se også [User Guide](https://statisticsnorway.github.io/ssb-pypitemplate/guide.html) for malen.

### Hjelp

Hvis du ønsker å migrere et eksisterende python-bibliotek til den nye malen, så kan tech-coachene på seksjon IT-partner hjelpe deg med det. Ta kontakt på e-post <mailto:it-partner@ssb.no>.

Har du flere spørsmål eller noe du trenger hjelp til angående malen, så kan medlemmene i støtteteamet/hjelpekorpset på din avdeling hjelpe deg, eller du kan ta kontakt med tech-coachene på seksjon IT-partner som nevnt ovenfor.
