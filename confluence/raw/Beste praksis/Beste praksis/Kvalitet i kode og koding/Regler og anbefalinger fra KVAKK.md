---
tags:
  - git
  - kvakk
---

# Regler og anbefalinger fra KVAKK

Status: <mark style="background: #baf3db;">I BRUK</mark>

> [!IMPORTANT]
> Dette er en samleside som viser alle KVAKK-regler og KVAKK-anbefalinger. De er gruppert etter temaene de er tatt fram under og bør ses i sammenheng med mer utfyllende tekst og veiledninger for hvert tema. Temaene er [Versjonskontroll med Git](Versjonskontroll%20med%20Git.md), [Generelle kodeprinsipper](Generelle%20kodeprinsipper.md), [Gjenbruk](Gjenbruk.md) og [Test og kodekvalitet](Test%20og%20kodekvalitet.md).
>
> Se også definisjon av ordene “regel” og “anbefaling” på [Kvalitet i kode og koding](../Kvalitet%20i%20kode%20og%20koding.md).

**Innholdsfortegnelse**

## Regler og anbefalinger for versjonskontroll med Git

### R-001 Regel: All produksjonskode skal være under versjonskontroll i GitHub.

<details>
<summary>Hvorfor</summary>

- Tilnærmet all profesjonell programvare og åpen kildekode programvare utvikles med versjonskontroll på kildekoden. Det er en anerkjent beste praksis. Det gjelder også andre statistikkbyråer som for eksempel SSB Nederland, som har akkurat det samme kravet.
- DM har vedtatt at SSB skal følge ISO 27001/27002, og der kreves det versjonskontroll for alle programvareoppdateringer. Git er det desidert mest brukte verktøyet for versjonskontroll av kildekode.
- For å sikre reproduserbarhet og ha kontroll på endringer. I dokumentet “Datatilstander i SSB” brukes begrepet etterprøvbarhet og det sier “…produsere statistikk på en slik måte at ettertiden eller en uavhengig instans med tilgang til dataene og vår dokumentasjon vil komme til samme statistiske resultater som oss selv.”
- Sikkerhet. Koden på GitHub skannes for sårbarheter og man får varsel hvis sårbarheter finnes.
- Effektivt verktøy for deling og samarbeid om kildekode. Det å lese og kommentere på hverandres kode er en av de beste måtene å øke kodekvaliteten på, og GitHub har en god funksjon for dette.
- Vedtatt av DM 31.01.2023

</details>

<details>
<summary>Hvordan</summary>

Beskrivelse av hvordan.

1. [Hvordan opprette GitHub-konto og bli medlem i SSB sin organisasjon der?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20opprette%20GitHub-konto%20og%20bli%20medlem%20i%20SSB%20sin%20organisasjon%20der_.md)
2. [Hvordan installere Git](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20installere%20Git.md)
3. [Hvordan konfigurere git (git config) etter SSB-standard?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20konfigurere%20git%20(git%20config)%20etter%20SSB-standard_.md)
4. [Hvordan opprette nytt GitHub-repo?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20opprette%20nytt%20GitHub-repo_.md)

</details>

### A-002 Anbefaling: All kildekode skal være under versjonskontroll i GitHub.

<details>
<summary>Hvorfor</summary>

- Samme begrunnelse som for regel R-001.

</details>

<details>
<summary>Hvordan</summary>

- Samme beskrivelse som for regel R-001.

</details>

### R-003 Regel: Kildekode i GitHub skal ikke inneholde ukrypterte passord eller hemmeligheter.

<details>
<summary>Hvorfor</summary>

- Hindre uautorisert tilgang til data og systemer.
- Hindre avsløring av sensitive parametre (konfidensialitetsmetoder).
- Vedtatt av DM 31.01.2023

</details>

<details>
<summary>Hvordan</summary>

- Har du behov for å ha tilgang på hemmeligheter i kildekoden så løser du det som beskrevet på [Hvordan håndtere hemmeligheter og passord i git?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20håndtere%20hemmeligheter%20og%20passord%20i%20git_.md)

</details>

### R-004 Regel: Git-klienter skal konfigureres slik at resultat fra kjøringer i Jupyter Notebooks ikke lagres på GitHub.

<details>
<summary>Hvorfor</summary>

- For å forhindre lekkasje av sensitive data.
- Krav fra [Risikovurdering av å gi tilgang til GitHub fra prod-sone](../../../Byråets%20IT-plattform/Byråets%20IT-plattform/Risikovurdering%20av%20å%20gi%20tilgang%20til%20GitHub%20fra%20prod-sone.md) i SSB.
- Vedtatt av DM 31.01.2023

</details>

<details>
<summary>Hvordan</summary>

[Hvordan konfigurere git (git config) etter SSB-standard?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20konfigurere%20git%20(git%20config)%20etter%20SSB-standard_.md)

</details>

### A-005 Anbefaling: Skill på kildekode og data.

Kildekode lagres i git/GitHub, mens data lagres i databaser eller filer uten for kildekoden.  
Unntak for mindre mengder testdata, for eksempel til enhetstesting, eller små eksempler.

<details>
<summary>Hvorfor</summary>

- Et godt arkitekturprinsipp, og git er ikke egnet for større mengder data.
- Gjør det lettere å ha repoene som åpen kildekode (ref. anbefaling A-011). Det er svært ofte dataene som er sensitive, ikke kildekoden.

</details>

<details>
<summary>Hvordan</summary>

- Ved å legge inn anbefalt `.gitignore`-fil i repoet, som beskrevet på [Hvordan konfigurere git (git config) etter SSB-standard?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20konfigurere%20git%20(git%20config)%20etter%20SSB-standard_.md) Den hindrer at du får sjekket inn data-filer i git-repoet.

</details>

### A-006 Anbefaling: Gjennomfør utviklingsaktiviteter på egne branches.

<details>
<summary>Hvorfor</summary>

- Gjør det mulig å jobbe upåvirket av andre kodeendringer i repoet.
- Muliggjør kodelesing med pull request mekanismen.

</details>

<details>
<summary>Hvordan</summary>

- [Hvordan er anbefalt git arbeidsflyt?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20er%20anbefalt%20git%20arbeidsflyt_.md)

</details>

### A-007 Anbefaling: Unngå langtlevende branches.

<details>
<summary>Hvorfor</summary>

- Det er god praksis å definere små oppgaver og avslutte/merge de tilhørende greinene innen rimelig tid. Det reduserer antall mergekonflikter og vanskegraden på dem.

</details>

<details>
<summary>Hvordan</summary>

- [Hvordan er anbefalt git arbeidsflyt?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20er%20anbefalt%20git%20arbeidsflyt_.md)

</details>

### A-008 Anbefaling: Oppdater utviklingsgrenen din med endringer fra hovedgrenen før pull request.

<details>
<summary>Hvorfor</summary>

- Da får du løst ut eventuelle mergekonflikter lokalt.
- Gir mulighet til å bruke grafisk mergeverktøy, noe som reduserer sannsynligheten for feil.

</details>

<details>
<summary>Hvordan</summary>

- [Hvordan er anbefalt git arbeidsflyt?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20er%20anbefalt%20git%20arbeidsflyt_.md)

</details>

### A-009 Anbefaling: Bruk pull request på all produksjonskode.

En *pull request*  er en forespørsel om å få noen andre til å se over og vurdere endringer du har gjort i koden før koden *merges*. Ofte kjøres det også automatiske tester på en *pull request*. Bruk også *pull request* om du jobber alene på et GitHub-repo, men da godkjenner du pull requestene selv.

<details>
<summary>Hvorfor</summary>

- Reduserer faren for feil: Pull requests hjelper til med å oppdage feil eller forbedringsmuligheter før endringene blir en del av den endelige koden.
- Læring og samarbeid: Det gir teammedlemmer en mulighet til å dele innsikt, stille spørsmål og lære av hverandre.
- Dokumentasjon: Hver pull request inneholder en beskrivelse av hva som er endret og hvorfor, slik at det blir enklere å forstå hva som har skjedd senere.
- Trygghet: I stedet for å endre noe direkte, gir en pull request en mulighet til å teste endringene i en kontrollert setting før de blir en del av det ferdige prosjektet

</details>

<details>
<summary>Hvordan</summary>

- Se beskrivelse på [Hvordan bruke pull request på GitHub?](Hvordan%20samarbeide%20om%20kode_/Bruk%20av%20pull%20requests/Hvordan%20bruke%20pull%20request%20på%20GitHub_.md)

</details>

### A-010 Anbefaling: Bruk et grafisk verktøy for å løse mergekonflikter.

<details>
<summary>Hvorfor</summary>

- Reduserer faren for å gjøre feil.

</details>

<details>
<summary>Hvordan</summary>

- [Hvordan løse en merge-konflikt?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20løse%20en%20merge-konflikt_.md)

</details>

### A-011 Anbefaling: Produksjonskode skal som standard være åpen kildekode. Det vil si at git-repoene skal være public.

Unntak: Noen unntak relatert til blant annet sikkerhet. Se beslutning lenket til nedenfor. Repoer migrert fra Bitbucket på bakken skal som standard være internal, begrunnet i sikkerhet. Er man usikker på om repoet inneholder noe sensitivt, så ha det som internal.

Et repo som er åpen kildekode (public) skal tilfredstille [ADR0006 - Retningslinjer for åpen kildekode i SSB](Versjonskontroll%20med%20Git/ADR0006%20-%20Retningslinjer%20for%20åpen%20kildekode%20i%20SSB.md).

<details>
<summary>Hvorfor</summary>

- Se beslutning seksjon for IT-arkitektur: [ADR0006 - Retningslinjer for åpen kildekode i SSB](Versjonskontroll%20med%20Git/ADR0006%20-%20Retningslinjer%20for%20åpen%20kildekode%20i%20SSB.md)
- Offentlighetsloven [gir rett til innsyn i ikke-sensitiv produksjonskode](#). En god og enkel måte å sikre dette på er å dele kildekoden offentlig på GitHub.

</details>

<details>
<summary>Hvordan</summary>

- [Hvordan opprette nytt GitHub-repo?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20opprette%20nytt%20GitHub-repo_.md)
- [ADR0006 - Retningslinjer for åpen kildekode i SSB](Versjonskontroll%20med%20Git/ADR0006%20-%20Retningslinjer%20for%20åpen%20kildekode%20i%20SSB.md)

</details>

### A-012 Anbefaling: Skriv kildekode, api-dokumentasjon og commit-meldinger på engelsk.

Unntak: Ikke oversett elementer til engelsk der hvor det er brukt norsk språk på for eksempel navn på kolonner i databaser, felter i eksterne API’er osv.

<details>
<summary>Hvorfor</summary>

- Se beslutning seksjon for IT-arkitektur: [ADR0003 - Språk i teknisk dokumentasjon og kode](Regler%20og%20anbefalinger%20fra%20KVAKK/ADR0003%20-%20Språk%20i%20teknisk%20dokumentasjon%20og%20kode.md)

</details>

<details>
<summary>Hvordan</summary>

- [Eksempel på språk i kode med eksterne norske navn](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Eksempel%20på%20språk%20i%20kode%20med%20eksterne%20norske%20navn.md)
- [Eksempel på commit-melding](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20er%20anbefalt%20git%20arbeidsflyt_/Eksempel%20på%20commit-melding.md)

</details>

### A-013 Anbefaling: Hvis bruk av Jira som oppgaveverkøy: Bruk Jira-ID som prefiks i commit-meldinger og navn på branches.

<details>
<summary>Hvorfor</summary>

- Gir endringskontroll ved automatisk sporing av kodeendringer i tilhørende JIRA-sak.

</details>

<details>
<summary>Hvordan</summary>

- Eks: “`git commit -m"DAPLA-312: Add validation`", "`git checkout -b DAPLA-312-My-task`"
- [Eksempel på commit-melding](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20er%20anbefalt%20git%20arbeidsflyt_/Eksempel%20på%20commit-melding.md)

</details>

## Generelle kodeprinsipper

### A-020 Anbefaling: Del opp prosessen i trinn.

<details>
<summary>Hvorfor</summary>

For de fleste formål bør prosessen deles i velavgrensede trinn, fordi det gjør det lettere både å planlegge, gjennomføre, og kontrollere.

For statistikkproduksjoner av samme type bør trinnene være noenlunde de samme, fordi det gjør det lettere å gjenbruke gode løsninger på tvers i organisasjonen.

</details>

<details>
<summary>Hvordan</summary>

Lag en plan før du begynner å programmere, gjerne med illustrasjoner.

Undersøk hva som er gjort av lignende ting før, og hvilke deler som eventuelt kan gjenbrukes.

Planleggingen skjer gjerne i en annen rekkefølge enn det som skjer i selve prosessen.   
Begynn med slutten (!), etter det tar du starten, og tilslutt planlegger du midten:

1. Konsentrer deg først om å finne ut hva prosessen skal lage – “ferdig vare”.
2. Etter det, kan du begynne å finne fram til mulige datakilder – “råvare”.
3. Finn så ut hvilke trinn som må gjøres for å komme fra “råvare” til “ferdig vare”.

**Generelle anbefalinger:**

- Undersøk om andre har laget lignende prosesser, eller noen trinn av prosessen.
- Bruk velprøvde framgangsmåter så langt som mulig.
- Hvordan dele opp i trinn? Her er noen typiske kriterier:
- Lag et nytt trinn når:

  - Data overføres, f.eks. fra et system eller plattform til et annet.
  - Data fra ulike kilder kobles sammen, f.eks. ulike register, skjemadata, osv.
  - Data endres betydelig, som filtrering, splitting, beregning, osv.
  - Manuelle oppgaver, som å vurdere mulige feil, endre grenseverdier, redigere data, osv.

> [!IMPORTANT]
> **Mer hjelp for statistikkproduksjon her:**
>
> Byrånettet linker til mer hjelp og informasjon om hvordan statistikkproduksjon skal organiseres:
>
> - <https://ssbno.sharepoint.com/sites/Statistikkproduksjonogpublisering>
> - <https://ssbno.sharepoint.com/sites/Metodikkistatistikkproduksjonen>

</details>

### A-021 Anbefaling: Kontroller data for hvert trinn.

<details>
<summary>Hvorfor</summary>

Trinnvise kontroller gjør det lettere å redusere feil og mangler i data, enn om man tar alle kontrollene tilslutt.

</details>

<details>
<summary>Hvordan</summary>

**Generelle anbefalinger:**

- Forebygg feil så mye som mulig.
- Når forebyggelse ikke er mulig:

  - kontroller data så tidlig som mulig.
  - rett feil i data så tidlig som mulig.
- Bruk vanlige måter og innebygde løsninger så langt som mulig, for eksempel:

  - Bestem **typer** av data (f.eks. ikke tillat bokstaver der det skal lagres tall),
  - Bestem **restriksjoner** for data (f.eks. ikke tillat missing eller dubletter i en koblingsnøkkel).
- Etter hvert trinn, kontroller data:

  - **form** (filer, variabler, records)
  - **innhold** (verdier, tall, tekst).
- Bruk velprøvde framgangsmåter så langt som mulig, både med hensyn til statistisk metode, og med hensyn til det aktuelle programmeringsspråk.

> [!IMPORTANT]
> **Mer hjelp for statistikkproduksjon her:**
>
> - [Dataeditering i statistikkproduksjon - informasjonsside](https://ssbno.sharepoint.com/sites/Statistikkproduksjonogpublisering/SitePages/Dataeditering.aspx)
> - [Datarevisjon - Kontroll, gransking og retting av data (notat)](https://www.ssb.no/a/histstat/ssh/ssh_84.pdf)

</details>

### A-022 Anbefaling: Hold orden på data for hvert trinn.

<details>
<summary>Hvorfor</summary>

God orden er viktig for kvalitet, effektivitet, og sikkerhet.

Å holde orden betyr både å lage nye data på en ryddig måte, å ta godt vare på data underveis, å rydde opp i data når det trengs, og å slette data som ikke skal lagres.

</details>

<details>
<summary>Hvordan</summary>

**Generelle anbefalinger:**

- Hold orden på data fra ulike kilder som brukes til hvert trinn (input).
- Hold orden på data som lages i hvert trinn (output).
- Hold orden på ulike versjoner av samme type data.
- Forebygg utilsiktet sletting av data.
- Forebygg utilsiktet lagring av data.

> [!IMPORTANT]
> **Mer hjelp for statistikkproduksjon her:**
>
> For statistikkproduksjon er det ekstra viktig å ha gode rutiner for å lage, ta vare på, rydde i, og slette data. Statistikksystemene er i ferd med å flytte, og mer informasjon om dette er under utvikling:
>
> - <https://manual.dapla.ssb.no/statistikkproduksjon.html>

</details>

### A-023 Anbefaling: Sørg for at output er reproduserbart

<details>
<summary>Hvorfor</summary>

Det er viktig å kunne reprodusere output/statistikk og kvalitetssikre disse i ettertid

</details>

<details>
<summary>Hvordan</summary>

- Versjonskontroll på data og hvilken versjon av data som er brukt.

  - Git bidrar til å holde alle versjoner av koden arkivert og sikre at man kan finne igjen ulike iterasjoner. Det gjør også deling av kode enkelt.
  - Det er viktig å dokumentere hvilke datasett som benyttes for å lage publiserte tall slik at man senere kan se hvordan tallene ble laget.
- Gjør færrest mulig manuelle endringer. Der du må gjøre manuelle endringer, sørg for god dokumentasjon og loggføring av endringer. Se A-025.
- Hvis du bruker pseudo-random funksjoner, sørg for at «seed» som brukes er tilgjengelig i ettertid.

</details>

### A-024 Anbefaling: Ha færrest mulig manuelle steg

<details>
<summary>Hvorfor</summary>

Manuelle steg introduserer feilkilder som er vanskelige å oppdage i ettertid.

</details>

<details>
<summary>Hvordan</summary>

Finn og bruk verktøy med maskinelle løsninger på de manuelle prosessene

</details>

### A-025 Anbefaling: Dokumenter manuelle steg/endringer som blir gjort

<details>
<summary>Hvorfor</summary>

For å kunne kvalitetssikre produksjonsløp og reprodusere output data så er det nødvendig at manuelle steg er godt dokumentert.

</details>

<details>
<summary>Hvordan</summary>

Dokumentasjon av manuelle steg i et produksjonsløp bør gjøres kodenært, det vil si at dokumentasjonen ligger tilgjengelig nær der kildekoden ligger.

Dokumentasjonen kan for eksempel være i markdown og versjonshåndteres i Git / Github sammen med den tilhørende kildekoden.

</details>

### A-026 Anbefaling: Skill mellom utvikling og produksjon

<details>
<summary>Hvorfor</summary>

Det er viktig at produksjonskoden holdes stabil og uten feil. Om man holder utvikling i et eget miljø reduserer man risikoen for at man med et uhell påvirker produksjonsløpet

</details>

<details>
<summary>Hvordan</summary>

Det finnes flere måter å skille mellom utvikling og produksjon når man lager kildekode.

1. Bruk av Git og Github. Versjonskontrollsystemer, som Git, er vanlige verktøy i programvareutvikling og lar utviklere administrere koden og holde oversikt over endringer som skal over til produksjon.  
   Se relevante anbefalinger om bruk av Git:

   - [Regler og anbefalinger fra KVAKK](Regler%20og%20anbefalinger%20fra%20KVAKK.md)
   - [Regler og anbefalinger fra KVAKK](Regler%20og%20anbefalinger%20fra%20KVAKK.md)
   - [Regler og anbefalinger fra KVAKK](Regler%20og%20anbefalinger%20fra%20KVAKK.md)
2. Skill mellom utviklingsmiljø og produksjonsmiljø der det er mulig.  
   **Utviklingsmiljøet** er der du jobber med koden, tester og eksperimenterer med nye funksjoner.  
   **Produksjonsmiljøet** er der den faktiske koden/produksjonsløpet kjører og lager statistikk til publisering.

   - På bakken vil et eksempel på et slikt skille være å utvikle på DB1T mens produksjon kjører på DB1P.

</details>

### A-027 Anbefaling: Lag tester for viktige punkter i koden

<details>
<summary>Hvorfor</summary>

Tester i koden gjør det enklere å oppdage feil, sparer tid ved feilsøking og gjør koden lettere å forstå for andre. Det gjør det enklere og sikrere å endre koden senere.

</details>

<details>
<summary>Hvordan</summary>

Hva som er et viktig punkt i koden må avgjøres basert på faglig skjønn og en risikovurdering av produksjonsløpet.

Det er flere ulike typer tester man kan lage:

- **Enhetstest**: Dette er tester som typisk tester logikken til funksjon. Man sender inn data til funksjonen og tester om resultatet er som forventet.

  - Eksempel: Hvis du har kode som skal legge sammen to tall, så kan du gi den 5 og 10 som test-tall og sjekke at svaret blir 15.
- **Integrasjonstest**: Her tester man at et sett av funksjoner eller delsystemer sammen fører til forventet resultat.
- **Systemtest/ende-til-ende test**: Her tester man hele systemet/produksjonsløpet. Man sender data inn i systemet og sjekker at systemet gjør det man forventer.

Det vil komme konkrete beskrivelser og eksempler på hvordan man kan lage tester i R og Python.

</details>

### A-028 Anbefaling: Velg verktøy som utfører den statistiske metoden som er ønsket av den ansvarlige.

Den ansvarlige er ofte den statistikkansvarlige.

<details>
<summary>Hvorfor</summary>

Når jobben som skal gjøres inkluderer en statistisk metode, så er metodevalget avgjørende for kvaliteten på sluttresultatet. Valg av metode bør være gjennomtenkt og verktøyet må velges i tråd med dette.

Eksempel: Ikke bare google etter algoritme for sesongjustering, men velg et verktøy som implementerer Eurostats anbefaling for sesongjustering, og som er den SSB skal følge.

</details>

<details>
<summary>Hvordan</summary>

Sjekk alltid først om du kan gjenbruke en løsning som allerede finnes i standardspråket du benytter. Mange ganger må det gjøres avveiinger mellom metodevalg, ytelse og enkel programmering. Hva som allerede er tilgjengelig er essensielt ved slike avveiinger. Ta gjerne en titt på [Valg av programmeringsspråk for statistiske metoder](https://ssbno.sharepoint.com/sites/Internedokumenter/Delte%20dokumenter/Interne%20dokumenter%202021/2021-15%20Valg%20av%20programmeringsspr%C3%A5k%20for%20statistiske%20metoder%20.pdf?isSPOFile=1).

</details>

### A-029 Anbefaling: Bruk verktøy som tilbyr ferdiglagde komponenter for hele eller deler av jobben

<details>
<summary>Hvorfor</summary>

Gjenbruk er svært fordelaktig fordi man unngår feil og unødvendig arbeid og fordi behovet for vedlikehold reduseres.

</details>

<details>
<summary>Hvordan</summary>

Undersøk om du kan gjenbruke en løsning som fins i språket du behersker best. Det kan godt hende at den endelige løsningen bør bli kombinasjon av språk eller at det gjøres kall til et selvstendig program. Se mer på [Gjenbruk 26.01.23](../../../Team%20Utviklingsmetodikk/Team%20Utviklingsmetodikk/Workshops/Gjenbruk%2026.01.23.md).

</details>

### A-030 Anbefaling: Bruk verktøy som bidrar til oversiktlig programkode

<details>
<summary>Hvorfor</summary>

Oversiktlig programkode gjør det enkel for både deg selv og andre å sette seg inn i koden senere. Dette forenkler vedlikeholdet og er dermed ressursbesparende.

</details>

<details>
<summary>Hvordan</summary>

Velg et programmeringsspråk som gjør det mulig for deg å lage oversiktlig programkode. Bruk standarder og tilleggsverktøy som hjelper deg i dette arbeidet. Eksempel: Verktøy for automatisk formattering av kode. Se også [Hold det enkelt](Generelle%20kodeprinsipper/Hold%20det%20enkelt.md)

</details>

### A-031 Anbefaling: Velg verktøy som gjør at programmet kjører raskt uten å sløse med dataressurser

<details>
<summary>Hvorfor</summary>

Dataressurser som minne og kjøretid er en kostnad. Venting er også en arbeidskostnad.

</details>

<details>
<summary>Hvordan</summary>

Dette er noe man skal tenke på dersom kjøretid og/eller minnebruk er av et visst omfang. Undersøk om det fins ferdige løsninger som gjøre jobben effektivt. Tenk på om du selv kan bidra til effektiv programkjøring. Det fins verktøy som er til hjelp for å finne flaskehalsene.  
Det kan være en avveining mellom minnebruk og kjøretid, for eksempel ved å bruk mer minne kan man redusere kjøretid.

</details>

### A-032 Anbefaling: Velg velprøvde og trygge verktøy

<details>
<summary>Hvorfor</summary>

Velprøvde verktøy gir større trygghet for at alt fungerer som det skal. Trygghet i form av IT-sikkerhet bør være en selvfølge.

</details>

<details>
<summary>Hvordan</summary>

Se mer på SSBs [Godkjentliste for statistikkproduksjon på Dapla](../../../Arkitektur/Arkitektur/Valg%20av%20teknologi/Godkjentliste%20for%20statistikkproduksjon%20på%20Dapla.md)

</details>

### A-033 Anbefaling: Del opp koden din.

<details>
<summary>Hvorfor</summary>

Bryt opp koden i mindre funksjoner som gjør hver enkelt funksjon liten og lett å forstå.

Kode består ofte av ulike deler/moduler, som har hver sin egen struktur. Alle disse delene bør være lett å forstå og ha dokumentasjon som introduksjon. Derfor er det viktig å ha et tydelig skille mellom de ulike delene:

- kildekode
- tests
- konfigurasjonsfiler
- dokumentasjon

</details>

<details>
<summary>Hvordan</summary>

Følg råd og anbefalinger for språket du bruker (f.eks. [Python på DAPLA](https://manual.dapla.ssb.no/jobbe-med-kode.html)).

Det kan være lurt å lage en gjenbrukbar pakke med kode som brukes ofte (se [Gjenbruk 26.01.23](../../../Team%20Utviklingsmetodikk/Team%20Utviklingsmetodikk/Workshops/Gjenbruk%2026.01.23.md) og [Hvordan legge ut fellesfunksjoner som et PyPI-bibliotek?](../../../Arne%20Sørli/Oversikt/Hvordan%20legge%20ut%20fellesfunksjoner%20som%20et%20PyPI-bibliotek_.md)).

</details>

### A-034 Anbefaling: Bruk enkle konstruksjoner i koden.

<details>
<summary>Hvorfor</summary>

Komplisert kode kan være vanskelig forstå og vedlikeholde, både for forfatteren selv og andre som skal bruke den eller bidra til den. I de fleste tilfellene vil man kunne omskrive komplekse konstruksjoner i koden til flere enkle som er lettere å forstå. Målet skal være at koden er forståelig uten ekstra dokumentasjon. For eksempel, de følgende to funksjonen `common_elements1` og `common_elements2` gir en liste over felleselementer i to lister, mens `common_elements2`er både raskere og har enklere struktur:

```py
def common_elements1(list1, list2):
    result = []
    for x in list1:
        for y in list2:
            if x == y and x not in result:
                result.append(x)
    return result
    
def common_elements2(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))
```

</details>

<details>
<summary>Hvordan</summary>

- Del opp lange uttrykk over flere linjer, dersom språket tillater dette.
- Begrens antall parametere til en funksjon. Se om man kan bryte opp en funksjon med mange parametere til flere funksjoner eller objekter.
- Bruk kommentarer bare der det virkelig er nødvendig. Kommentarer blir fort utdatert, så de skal bare benyttes der det er nødvendig for å forstå koden. En kommentar bør svare på spørsmålet "hva" eller “hvorfor”, ikke "hvordan"

</details>

### A-035 Anbefaling: Velg beskrivende navn.

<details>
<summary>Hvorfor</summary>

For å sikre enkel forståelse av kode, bør det være tydelig fra navnet hvilken rolle en variable, klasse, funksjon, etc. har. I tillegg vil et enhetlig format for navn føre til lettere kodeforståelse. For eksempel, begge av de følgende Python funksjonene regner ut fakultet av et gitt tall, men `factorial` er enklere å lese og forstå uten dokumentasjon enn `f`.

```py
f = lambda x: 1 if x <= 1 else x * f(x - 1)

def factorial(number: int) -> int:
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)
```

</details>

<details>
<summary>Hvordan</summary>

- Vær konsistent i bruken av små- og storbokstaver og bruk av spesialtegn (slik som “-”, “.” og “\_”).
- Unngå å bruke altfor lange eller korte variabelnavn. Hold det så kort som mulig, men så langt som nødvendig.
- Hold deg til[ADR0003 - Språk i teknisk dokumentasjon og kode](Regler%20og%20anbefalinger%20fra%20KVAKK/ADR0003%20-%20Språk%20i%20teknisk%20dokumentasjon%20og%20kode.md) når det gjelder navngivning.
- Bruk anerkjente navnekonvensjoner der dette finnes. For eksempel:

  ```py
  # følger klassiske Python konvensjoner
  import pandas as pd

  # følger ikke konvensjoner, kan føre til forvirring hos andre
  import pandas as pan
  ```
- Bruk programmeringsspråkets anbefalte navnestandard ([navngivning i R](https://style.tidyverse.org/syntax.html#object-names), [navngivning i Python](https://peps.python.org/pep-0008/#naming-conventions)).

</details>

### A-036 Anbefaling: Bruk et standardisert og lesbart kodeformat.

<details>
<summary>Hvorfor</summary>

Lesbarhet av kode skal ikke undervurderes. Det er mye enklere for andre å sette seg inn i, begynne å bruke og bidra til eksisterende kode dersom det følger etablerte formateringspraksis.

</details>

<details>
<summary>Hvordan</summary>

De aller fleste programmeringsspråk har beste praksis anbefalinger for hvordan kode skal formatteres, og SSB har anbefalinger på hvordan disse skal brukes ([anbefalinger for R](https://wiki.ssb.no/display/s880/Veiledning+til+R+programmering+i+SSB), [PEP8 for Python](https://peps.python.org/pep-0008/)). De aller fleste IDE'er (for eksempel RStudio, Visual Studio Code) har støtte for automatisk formattering av kode i henhold til disse reglene.

</details>

### A-037 Anbefaling: Skriv dokumentasjon (bare) der det trengs.

<details>
<summary>Hvorfor</summary>

Dokumentasjon kan hjelpe andre sette seg inn i koden og dens bruk. Samtidig må dokumentasjonen bli vedlikeholdt sammen med koden: hvis kodens oppførsel endrer seg, må dokumentasjonen bli oppdatert. Av denne grunnen er det viktig å dokumentere nok til å hjelpe andre sette seg inn i koden, men ikke så mye at det fører til unødvendig vedlikeholdsarbeid.

</details>

<details>
<summary>Hvordan</summary>

Det er viktig å skille mellom teknisk dokumentasjon og brukerdokumentasjon: teknisk dokumentasjon dreier seg om alt knyttet til utvikling og vedlikehold av koden, mens brukerdokumentasjon handler om hvordan man kan komme i gang med å bruke koden.

**Teknisk dokumentasjon**

- Det er et vanlig problem at dokumentasjon fort blir utdatert mens utviklingen pågår. Derfor bør man holde ekstern dokumentasjon til et minimum: dokumentér bare det som er nødvendig for å forstå koden. Ikke bruk dokumentasjon for å beskrive noe som kan forklares ved god kodestruktur og tydelig navngivning (se eksempelet i A-034: Velg beskrivende navn).
- Temaer som kan dokumenteres er: API’er, installering, beskrivelse av "rest points"
- Skriv alltid en "kom i gang" beskrivelse av koden

**Brukerdokumentasjon**

- koden bør bli utviklet slik at en bruker kan forstå mye av programvaren uten å måtte lese dokumentasjonen.
- Skriv kort og konsist.
- Bruk av skjermbilder kan være nyttig for brukere, men husk å oppdatere dem dersom noe forandrer seg.

</details>

## Gjenbruk

Python Package Index ([PyPI](https://pypi.org/)) er sted for publisering og nedlasting av python-biblioteker.  
The Comprehensive R Archive Network ([CRAN](https://cran.r-project.org/)) er tilsvarende for R-biblioteker, dvs. R-pakker.

### R-040 Regel: Alle biblioteker skal ha en eier

En eier skal være en seksjon eller annen organisatorisk enhet, ikke enkeltpersoner.

<details>
<summary>Hvorfor</summary>

- Biblioteker må vedlikeholdes og holdes oppdatert med blant annet sikkerhetsfikser. Da må noen være ansvarlig for dette.

</details>

<details>
<summary>Hvordan</summary>

- Eierskap må avklares når man skal opprette et bibliotek. I utgangspunktet er det naturlig at den/de som skrev koden opprinnelig er eier “You build it, you own it”, men annet eierskap kan avtales.
- Eier ansvarlig for vedlikehold av biblioteket.

</details>

### R-041 Regel: Bruk SSB-mal for PyPI-biblioteker når du skal lage et python-bibliotek

Python Package Index ([PyPI](https://pypi.org/)) er sted for publisering og nedlasting av python-biblioteker.

<details>
<summary>Hvorfor</summary>

- SSB har en mal for PyPI-biblioteker som følger god kodepraksis og dekker kravene og anbefalingene listet opp i Kvalitet i kode og koding (KVAKK). Den er satt opp med verktøy og sjekker for kodeanalyse, formattering, tester og dokumentasjon, samt at den har automatisk publisering til PyPI.
- Malen har mekanismer for oppdatering, slik at du lett kan oppdatere koden din med forbedringer som blir lagt til i malen.

</details>

<details>
<summary>Hvordan</summary>

- Se beskrivelse [Hvordan lage et python-bibliotek etter SSB standard?](Gjenbruk/Hvordan-beskrivelser%20for%20gjenbruk/Hvordan%20lage%20et%20python-bibliotek%20etter%20SSB%20standard_.md)

</details>

### R-042 Regel: Grensesnittet til biblioteket skal være dokumentert

Alle ikke-interne funksjoner og klasser skal være dokumentert. Alle argumenter og returverdier skal beskrives.

<details>
<summary>Hvorfor</summary>

- Det gjør det lettere for brukerne av biblioteket å forstå hva det gjør og bruke det riktig.

</details>

<details>
<summary>Hvordan</summary>

- I python: Som [docstring i koden](https://peps.python.org/pep-0257/#what-is-a-docstring) i google eller numpy-format. SSB PyPI-mal bruker docstrings i [google format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
- I R: Bruk [Roxygen2](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html) til dokumentasjon av funksjoner.

</details>

### R-043 Regel: Alle biblioteker skal ha tilhørende tester

<details>
<summary>Hvorfor</summary>

- For å sikre at funksjonene i biblioteket gjør det de er tenkt å gjøre. Det øker kodekvaliteten, reduserer faren for feil og gjør det tryggere å gjøre endringer.

</details>

<details>
<summary>Hvordan</summary>

- For python: Ved bruk av [pytest](https://docs.pytest.org/en/latest/). SSB PyPI mal er ferdig satt opp med pytest og har eksempler på bruk.
- For R: Ved bruk av [testthat](https://testthat.r-lib.org/).

</details>

### A-044 Anbefaling: Biblioteker og tilhørende kildekode bør være åpent tilgjengelig (public)

Python-biblioteker publiseres til [PyPI](https://pypi.org/). R-biblioteker, dvs. R-pakker, publiseres til [CRAN](https://cran.r-project.org/) eller public på GitHub. R-pakker anbefales publisert i første omgang på GitHub. Pakken bør vurderes publisert på CRAN,  hvis pakken har god nytteverdi eksternt og hvis man vil ta vedlikeholdsansvar etter [CRANs retningslinjer](https://cran.r-project.org/web/packages/policies.html).

<details>
<summary>Hvorfor</summary>

- Et bibliotek er ment å deles med andre og selve biblioteket ligger åpent tilgjengelig for hele verden på PyPI (Python) eller på CRAN (R). Da er det ingen grunn til at koden skal være skjult på GitHub.
- Se [ADR0006 - Retningslinjer for åpen kildekode i SSB](Versjonskontroll%20med%20Git/ADR0006%20-%20Retningslinjer%20for%20åpen%20kildekode%20i%20SSB.md)

</details>

<details>
<summary>Hvordan</summary>

- Sørg for at [ADR0006 - Retningslinjer for åpen kildekode i SSB](Versjonskontroll%20med%20Git/ADR0006%20-%20Retningslinjer%20for%20åpen%20kildekode%20i%20SSB.md) er oppfylt og følg beskrivelsen på[Hvordan opprette nytt GitHub-repo?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20opprette%20nytt%20GitHub-repo_.md) for å få repoet til å bli public. Som standard blir GitHub-repoer opprettet som internal.
- Hvis du tar utgangspunkt i SSB-mal for PyPI-biblioteker så er alle krav til åpen kildekode i SSB oppfylt.

</details>

### A-045 Anbefaling: Kildekode, dokumentasjon og navn på bibliotek skal være på engelsk

Norske egennavn som kortnavn på statistikk og andre innarbeidede begreper oversettes ikke.

<details>
<summary>Hvorfor</summary>

- Biblioteket er tilgjengelig for hele verden og det gjør at også ikke norsk-språklige kan ha nytte av biblioteket og har mulighet å bidra på det.
- Se [ADR0003 - Språk i teknisk dokumentasjon og kode](Regler%20og%20anbefalinger%20fra%20KVAKK/ADR0003%20-%20Språk%20i%20teknisk%20dokumentasjon%20og%20kode.md).

</details>

### A-046 Anbefaling: Før du oppretter et nytt bibliotek, sjekk om funksjonen du ønsker å dele kan legges til et eksisterende bibliotek

<details>
<summary>Hvorfor</summary>

- Det kan hende at den funksjonen eller det du ønsker å dele naturlig hører hjemme i et av de bibliotekene SSB allerede har. Da er det bedre å legge det til i det eksisterende biblioteket enn å opprette et nytt. Eksempel: La oss si at du har laget en funksjon `is_dapla()` for å sjekke om koden kjører på dapla. Den vil naturlig høre hjemme i biblioteket/repoet [dapla-toolbelt](https://github.com/statisticsnorway/dapla-toolbelt/tree/main#dapla-toolbelt).

</details>

<details>
<summary>Hvordan</summary>

Se kapittelet “[Hvordan lage et python-bibliotek etter SSB standard?](Gjenbruk/Hvordan-beskrivelser%20for%20gjenbruk/Hvordan%20lage%20et%20python-bibliotek%20etter%20SSB%20standard_.md)” i veiledningen for SSB PyPI-template. For R, sjekk funksjonalitet i [fellesR](https://github.com/statisticsnorway/fellesr) for å se om det passer inn der.

</details>

### A-047 Anbefaling: Alle public funksjoner og klasser i et python-bibliotek skal ha *type hint* på argumenter og returverdier

*Type hint* er en måte å angi hvilken type et argument, variabel eller returverdi har. For eksempel om det er et heltall eller tekststreng.

<details>
<summary>Hvorfor</summary>

- Bidrar til å finne og luke ut feil. Det finnes verktøy som kan sjekke om funksjoner blir kalt med riktige type parametre og gir feilmelding hvis det er feil type.
- For brukere av biblioteket: Gjør det lettere å forstå hva funksjonen forventer og hva den returnerer.

</details>

<details>
<summary>Hvordan</summary>

- Se [*type hints cheat sheet*](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).

</details>

### A-048 Anbefaling: Vær kritisk ved gjenbruk av eksterne biblioteker

<details>
<summary>Hvorfor</summary>

- Sikkerhet og vedlikehold. Biblioteker som er mye brukt og oppdateres regelmessig er uproblematisk, men et bibliotek med få brukere og som det er lenge siden er oppdatert bør man være kritisk til.

</details>

<details>
<summary>Hvordan</summary>

SSB har en [Godkjentliste for statistikkproduksjon på Dapla](../../../Arkitektur/Arkitektur/Valg%20av%20teknologi/Godkjentliste%20for%20statistikkproduksjon%20på%20Dapla.md). Finner du biblioteket der er det bare å ta det i bruk. Kodebiblioteker som er på [listen over SSB utviklede biblioteker](https://trygu.github.io/ssb-pypi-statistics/) er også greie å bruke. Hvis ikke må du sjekke litt nøyere.

Sjekk når biblioteket ble sist oppdatert, hvor mange stjerner og [nedlastinger](https://pypistats.org/) det har. Et bibliotek som er godt kjent, oppdateres hyppig og har mange stjerner og nedlastinger er uproblematisk. Men vær på vakt hvis det er lenge siden det er oppdatert og lite brukt. Alle pythonpakker som legges inn som avhengigheter i filer på GitHub-repoene til SSB, skannes for sårbarheter med verkøyet Dependabot, og man får advarsel hvis man har lagt inn en pakke med kjente sårbarheter.

</details>

### A-049 Anbefaling: Unngå duplisering av kode ved å skille ut til funksjoner

<details>
<summary>Hvorfor</summary>

- Mindre, enklere og bedre vedlikehold. Retting og forbedring skjer ett sted i stedet for flere steder.
- Lettere å teste og refaktorere (endre kode til bedre struktur uten å endre funksjonalitet)
- Bidrar til å generalisere koden, noe som letter gjenbruk.

</details>

<details>
<summary>Hvordan</summary>

- Verktøy for å sjekke duplisert kode: [SonarQube Cloud kodekvalitetsverktøy](Gjenbruk/Hvordan-beskrivelser%20for%20gjenbruk/SonarQube%20Cloud%20kodekvalitetsverktøy.md)
- [Hvordan automatisere Jupyter notebooks ved bruk av funksjoner?](Test%20og%20kodekvalitet/Hvordan-beskrivelser%20for%20test%20og%20kodekvalitet/Hvordan%20automatisere%20Jupyter%20notebooks%20ved%20bruk%20av%20funksjoner_.md)
- [God praksis ved gjenbruk i egen kode med funksjoner i Python og Jupyter Notebooks](Gjenbruk/Gjenbruk%20i%20egen%20kode/God%20praksis%20ved%20gjenbruk%20i%20egen%20kode%20med%20funksjoner%20i%20Python%20og%20Jupyter%20Notebooks.md)
- [Kodeeksempler på gjenbruk med Python](Gjenbruk/Gjenbruk%20i%20egen%20kode/Kodeeksempler%20på%20gjenbruk%20med%20Python.md)

</details>

### A-050 Anbefaling: Vær kritisk ved kopiering fra eksterne kilder

<details>
<summary>Hvorfor</summary>

- Det er viktig at man forstår koden man kopierer, slik at man kan vedlikeholde den selv på en god måte.

</details>

<details>
<summary>Hvordan</summary>

- [Anbefalinger ved kopiering av kode fra eksterne kilder](Gjenbruk/Gjenbruk%20ved%20kopiering/Anbefalinger%20ved%20kopiering%20av%20kode%20fra%20eksterne%20kilder.md)
- [Veileder for bruk av generativ kunstig intelligens i SSB](https://ssbno.sharepoint.com/sites/Megsomansatt/SitePages/Bruk-av-generativ-kunstig-intelligens.aspx?web=1)

</details>

### A-051 Anbefaling: Angi biblioteksavhengigheter med øvre versjonsgrense hvis du har lite tester

Hvis du har testdekning over 50% eller lager bibliotek så bør de angis uten øvre grense.

<details>
<summary>Hvorfor</summary>

- Nye hovedversjoner av et bibliotek inneholder av og til “breaking changes”, det vil si endringer som gjør at gammel kode ikke vil virke på samme måte med den nye versjonen. Uten god testdekning risikerer man å ikke fange opp dette.
- Man unngår at man får feil på grunn av ny versjon på et ubeleilig tidspunkt, for eksempel rett før publisering. Overgangen til ny versjon kan gjøres kontrollert på et tidspunkt som passer.

</details>

<details>
<summary>Hvordan</summary>

- Du får det automatisk hvis du legger til biblioteker med `poetry add` kommandoen.

  - Da settes det en øvre grense på hovedversjonen, det vil si det første tallet i versjonsnummeret
  - Eksempel: I filen pyproject.toml ser det ut slik: `"pandas (>=3.0.3,<4.0.0)"`

</details>

## Test og kodekvalitet

### A-060 Anbefaling: Bruk pytest som testrammeverk for python og testthat for R

<details>
<summary>Hvorfor</summary>

- Dette er de mest brukte testrammeverkene for python og R og er de KVAKK lager veiledninger for.

</details>

<details>
<summary>Hvordan</summary>

- [Eksempler på bruk av pytest](Test%20og%20kodekvalitet/Hvordan-beskrivelser%20for%20test%20og%20kodekvalitet/Eksempler%20på%20bruk%20av%20pytest.md)
- [Eksempler på enhetstester i R](Test%20og%20kodekvalitet/Hvordan-beskrivelser%20for%20test%20og%20kodekvalitet/Eksempler%20på%20enhetstester%20i%20R.md)

</details>

### R-061 Regel: All produksjonskode skal lagres i et format som støtter kodeanalyse

Det vil si at Jupyter Notebooks ikke skal lagres i \*.ipynb-format, men i .py- eller .R-format.

<details>
<summary>Hvorfor</summary>

- Kodeanalyseverktøy er til stor hjelp for sikre god kodekvalitet og redusere antall feil. For å kunne bruke dem må koden være lagret i et format som støttes av kodeanalyseverktøy.
- Se også [ADR-0020](https://adr.ssb.no/0020-lagringsformat-for-jupyter-notebooks/)

</details>

<details>
<summary>Hvordan</summary>

- [Hvordan lagre Jupyter notebooks i rent tekstformat?](../../../Avdelingen%20for%20IT/Avdelingen%20for%20IT%20Home/S703%20%20-%20IT%20Partner/Team%20tech%20coach/Veiledninger/Hvordan%20lagre%20Jupyter%20notebooks%20i%20rent%20tekstformat_.md)

</details>

### A-062 Anbefaling: All produksjonskode som ikke er skrevet R skal analyseres med SonarQube Cloud

Vil bli endret til regel etterhvert.

<details>
<summary>Hvorfor</summary>

- SonarQube Cloud er et godt kodeanalyseverktøy som er tilgjengelig for alle i SSB.
- Gir en sentralisert oversikt over kodekvalitetsstatus på produksjonskoden i SSB.
- Viser kvalitetsutvikling på GitHub-repoer over tid.

</details>

<details>
<summary>Hvordan</summary>

- [SonarQube Cloud kodekvalitetsverktøy](Gjenbruk/Hvordan-beskrivelser%20for%20gjenbruk/SonarQube%20Cloud%20kodekvalitetsverktøy.md)

</details>

### A-063 Anbefaling: Automatiser kjøring av flere Jupyter notebooks ved bruk av funksjoner

<details>
<summary>Hvorfor</summary>

- Det gir mye raskere kjøring enn ved bruk av for eksempel Papermill, samt mer modulær og testbar kode.

</details>

<details>
<summary>Hvordan</summary>

- [Hvordan automatisere Jupyter notebooks ved bruk av funksjoner?](Test%20og%20kodekvalitet/Hvordan-beskrivelser%20for%20test%20og%20kodekvalitet/Hvordan%20automatisere%20Jupyter%20notebooks%20ved%20bruk%20av%20funksjoner_.md)

</details>

### A-064 Anbefaling: Bruk verktøy for automatisk formattering av koden

For python brukes verktøyene black og isort, og navngiving bør følge [PEP8-navnekonvensjoner](https://peps.python.org/pep-0008/#naming-conventions).  
For R brukes verktøyet [styler](https://github.com/r-lib/styler)og bør følge [tidyverse style navnekonvensjoner.](https://style.tidyverse.org/tests.html)

<details>
<summary>Hvorfor</summary>

- Det sikrer en konsistent kodestil og gir færre merge-konflikter.

</details>

<details>
<summary>Hvordan</summary>

- [Hvordan formatere koden ved hjelp av verktøy?](Test%20og%20kodekvalitet/Hvordan-beskrivelser%20for%20test%20og%20kodekvalitet/Hvordan%20formatere%20koden%20ved%20hjelp%20av%20verktøy_.md)

</details>

### A-065 Anbefaling: Følg pythonstandard for navngiving av python-filer og tidyverse style for R

- Filnavn må starte med en liten bokstav (a-z). Tall er ikke tillatt som første tegn.
- Etter første tegn er følgende tillatt: Små bokstaver (a-z), tall (0-9) og understrek (\_).
- Det er ikke tillatt med norske tegn, bindestrek eller mellomrom i filnavn.

<details>
<summary>Hvorfor</summary>

- [PEP8](https://peps.python.org/pep-0008/#package-and-module-names) sier “…should have short, all-lowercase names. Underscores can be used in the module name if it improves readability.”
- For at import skal fungere må det som importeres være en [gyldig identifikator](https://docs.python.org/3/reference/lexical_analysis.html#identifiers). Hvis man for eksempel prøver å importere en fil som starter med tall så får man [denne feilen](https://gist.github.com/arneso-ssb/59546fc7aa7bd59789eb797dd50e351a).
- Sikre konsistent navngiving mellom python og R.

</details>

## Hvordan samarbeide om kode?

### A-070 Anbefaling: Vurder parprogrammering ved komplekse oppgaver, opplæring eller fare for personavhengighet

<details>
<summary>Hvorfor</summary>

- Kvalitetssikring av kode: Feil og logiske svakheter fanges ofte raskere opp, ettersom den som følger med, ser ting fra et litt annet perspektiv.
- Kunnskapsdeling og læring:Begge personene lærer av hverandre underveis, noe som bidrar til bedre forståelse av både kodebase og teknikker.
- Bedre samarbeid:Man får hyppige diskusjoner om løsningsstrategier og koding, noe som kan føre til mer gjennomtenkte løsninger.
- Forhindrer personavhengighet og flaskehalser: To personer blir like godt kjent med koden, så ikke alt ansvar hviler på én enkelt person. I tillegg er parprogrammering en god løsning hvis man opplever at pull requester er en flaskehals, siden man da er koden ferdig reviewet i det jobben er ferdig.

</details>

<details>
<summary>Hvordan</summary>

- <https://statistics-norway.atlassian.net/wiki/x/AoA6DAE>

</details>

### A-071 Anbefaling: Unngå å jobbe alene på et repo. Legg alltid til minst to admins på steder som GitHub, PyPi.

<details>
<summary>Hvorfor</summary>

- For å redusere sårbarhet og unngå avhengighet av enkeltpersoner.

</details>

<details>
<summary>Hvordan</summary>

- GitHub: [Hvordan opprette nytt GitHub-repo?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20opprette%20nytt%20GitHub-repo_.md)

</details>

### A-072 Anbefaling: Bruk gruppene data-admins og developers for tilgangsstyring på GitHub-repoer

For GitHub-repoer som gjelder Dapla-team, gi daplateamets data-admins gruppe admin-tilgang til repoet og daplateamets developers-gruppe skrivetilgang.

<details>
<summary>Hvorfor</summary>

- Da unngår man å måtte legge til og slette enkeltpersoner på hvert enkelt repo. Det holder at en person legges til på dapla-teamet, og så får personen automatisk tilgang til alle repoer som teamet har tilgang til.

</details>

<details>
<summary>Hvordan</summary>

- [Hvordan opprette nytt GitHub-repo?](Versjonskontroll%20med%20Git/Hvordan-beskrivelser/Hvordan%20opprette%20nytt%20GitHub-repo_.md)

</details>
