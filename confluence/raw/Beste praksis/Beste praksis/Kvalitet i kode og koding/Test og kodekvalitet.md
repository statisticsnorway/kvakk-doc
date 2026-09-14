
# Test og kodekvalitet

Forvalter av siden: [KVAKK-gruppa](/wiki/spaces/KOD)

Status: <mark style="background: #baf3db;">I BRUK</mark>

[Regler og anbefalinger fra KVAKK](Regler%20og%20anbefalinger%20fra%20KVAKK.md)

[Hvordan-beskrivelser for test og kodekvalitet](Test%20og%20kodekvalitet/Hvordan-beskrivelser%20for%20test%20og%20kodekvalitet.md)

## Introduksjon

Tester og god kodekvalitet bidrar til at det blir færre feil og letter vedlikehold av koden. Det er mange former for testing, men her har vi hovedfokus på det som kalles enhetstesting. Det vil si å sjekke at en funksjon eller metode gjør det den er forventet å gjøre, at logikken i funksjonen er riktig.

Vi skiller på å teste at logikken i koden er riktig og det å teste at dataene er som forventet. Her ser vi kun på test av logikk.

Når man skal teste logikken i koden, kan man gjøre det på tre nivåer:

- Enhetstest, som er det laveste nivået og som går på test av hver enkelt funksjon. Hvis funksjonen kaller eksterne ting som databaser eller api’er, så simulerer man ofte responsen fra disse. Det kalles *mocking*.
- Integrasjonstest, hvor man tester at ting fungerer integrert sammen, for eksempel mot database eller api.
- Systemtest og ende-til-ende-test: At hele systemet fungerer sammen, for eksempel fra en bruker klikker på et valg på en webside til han ser et svar.

Hva gjør du hvis du har få funksjoner i koden din, men notebooks som kjører fra topp til bunn uten funksjoner? Det anbefales å dele opp koden i funksjoner, som beskrevet i anbefaling [Page not accessible (ID: 3569778806)] og [Page not accessible (ID: 3911745551)]. Du kan dele opp til funksjoner som du legger enten i samme notebook, i samme mappe, eller i felles mappe et annet sted i repoet. Se [Hvordan automatisere Jupyter notebooks ved bruk av funksjoner?](Test%20og%20kodekvalitet/Hvordan-beskrivelser%20for%20test%20og%20kodekvalitet/Hvordan%20automatisere%20Jupyter%20notebooks%20ved%20bruk%20av%20funksjoner_.md).

Når det gjelder kodekvalitet, så lener vi oss i stor grad på bruk av verktøy for å hjelpe oss til å sikre god kodekvalitet. Ved bruk av dette over tid vil man etter hvert lære seg hva som er god kode.

## Terminologi

**Enhetstesting:** Testing av at funksjoner eller metoder gjør det de er forventet å gjøre.

***Mocking*****:** Brukes om testing der man erstatter et virkelig objekt, for eksempel en database, med et simulert objekt, en *mock*.

**Testdekning:** Hvor stor andel av koden som blir testet gjennom automatiserte tester.

Se også definisjoner i [Testordbok](../../../Avdelingen%20for%20IT/Avdelingen%20for%20IT%20Home/Operasjonell%20modell%20Avdeling%20for%20IT%20-%20A700/Prosesser%20og%20metoder/Test%20og%20kvalitetsikring/Testordbok.md), samt tidligere definisjoner av [Gjenbruk](Gjenbruk.md).

## Automatisert testing

### Hvorfor skrive tester?

- Sikre at koden gjør det den skal.
- Sparer tid på manuelle sjekker. Testing kan automatiseres.
- Gjør det tryggere å endre kode. Du får beskjed hvis resultatet av en funksjon endrer seg utilsiktet.
- Du forhindrer at samme feil oppstår flere ganger hvis du skriver en test for den.
- Lettere å feilsøke når man vet hvilken test det feiler i.
- Det er å skrive test av en funksjon får deg til å tenke gjennom mulige feilsituasjoner og grensetilfeller. Gjør i seg selv at du ofte skriver mer robust kode i funksjonen.
- Dokumentasjon. Tester dokumenterer på en konkret og kjørbar måte hvordan koden er forventet å virke. Det gjør det lettere for nye utviklere å forstå koden.

### Kjennetegn på enhetstester

- Skal være kjappe å kjøre.
- Skal være automatisert, det vil si at testene skal ikke kreve noen manuelle steg.
- Skal være uavhengige av hverandre. Det vil si at kjøring av en test ikke skal påvirke resultatet til en annen test.
- Skal være deterministiske, det vil si at de skal gi samme resultat når de kjøres med samme input.

### Hva skal vi teste?

- Funksjoner. Det vi skal teste må ligge i en funksjon eller metode. Se beskrivelse av [Hvordan automatisere Jupyter notebooks ved bruk av funksjoner?](Test%20og%20kodekvalitet/Hvordan-beskrivelser%20for%20test%20og%20kodekvalitet/Hvordan%20automatisere%20Jupyter%20notebooks%20ved%20bruk%20av%20funksjoner_.md) og hvordan skille ut duplisert kode til funksjoner.
- Det er ikke hensiktsmessig å teste alt. Det er en kost/nytte vurdering, og start med å prioritere testing av:

  - Kritiske/sentrale funksjoner som har stor betydning for resultatet.
  - Funksjoner med kompleks logikk (større sannsynlighet for feil).
  - Funksjoner som gjenbrukes flere steder i koden.
- Begynn i det små, og øk etter hvert.
- For statistikkproduksjon så trenger man ikke teste funksjoner som krever *mocking*.

### Hvilke testtilfeller bør man teste en funksjon for?

- Minimum et “godværsscenario”. Det vil si at alle input-parametre er som forventet og i enkleste form. Dette vil fange opp skrivefeil i koden og sjekke at koden lar seg kjøre, selv om man ikke sjekker resultatet. Men legg inn en sjekk på at resultatet er som forventet.  
  Tips for når man har kompleks input og output fra en funksjon, for eksempel dataframes:

  - Lagre input og output til funksjonen fra en vanlig kjøring til fil. [Eksempel](https://github.com/statisticsnorway/tech-coach-examples/blob/main/src/pytest_examples/notebook_example.py).
  - Les inn disse filene i testen, kall den aktuelle funksjonen med de aktuelle dataene, og sjekk at resultatet er som forventet. [Eksempel](https://github.com/statisticsnorway/tech-coach-examples/blob/main/tests/test_functions.py#L22-L27).
- Du kommer langt med “godværsscenario” i første omgang. Etterhvert kan du vurdere:

  - Negative tester, det vil si vanlige feilsituasjoner: Feil verdier i inputparametre, feil typer, ting som gjør at det kastes *exceptions*.
  - Bruk testdekning til å se på hvilke linjer som ikke er kjørt og lag testtilfeller som gjør at disse kjøres.
  - Grenseverdier. La oss si at en funksjon har en parameter som skal være mellom null og hundre. Da tester man med verdier som er rett innenfor, på grenseverdien og rett utenfor. I dette tilfellet -1, 0, 1, 99, 100 og 101.
- Kode i kodebiblioteker og funksjoner som brukes av mange bør ha bedre tester og testdekning enn funksjoner i et vanlig statistikkproduksjonsløp. Vi anbefaler en testdekning på minst 50 % for kodebiblioteker.

### Hvordan lage enhetstester?

For python, se [Eksempler på bruk av pytest](Test%20og%20kodekvalitet/Hvordan-beskrivelser%20for%20test%20og%20kodekvalitet/Eksempler%20på%20bruk%20av%20pytest.md).

For R, se [Eksempler på enhetstester i R](Test%20og%20kodekvalitet/Hvordan-beskrivelser%20for%20test%20og%20kodekvalitet/Eksempler%20på%20enhetstester%20i%20R.md)

## Kodekvalitet

Det finnes mange verktøy som kan hjelpe deg til å få og holde god kvalitet på koden. Vi deler det inn i to hovedgrupper:

- Formattering: Verktøy som sikrer konsistent formattering av koden, sortering av importer osv. De fleste av disse verktøyene fikser endringene automatisk, og ingen endrer logikken i koden. Eksempel: black og isort for python, og [styler](https://cran.r-project.org/web/packages/styler/vignettes/styler.html) for R.
- Linting: Påpeker feil og ting som bør forbedres i selve koden. Eksempel: SonarCloud, ruff, mypy for python, og [lintr](https://lintr.r-lib.org/) og [covr](https://covr.r-lib.org/) for R.

### SonarQube Cloud

SonarQube Cloud er et kodekvalitetsverktøy som er tilgjengelig for alle i SSB og anbefales for all produksjonskode som ikke er R. Vi har en egen [SonarQube Cloud kodekvalitetsverktøy](Gjenbruk/Hvordan-beskrivelser%20for%20gjenbruk/SonarQube%20Cloud%20kodekvalitetsverktøy.md) som beskriver hvordan du kommer i gang og [SonarQube Cloud kodekvalitetsverktøy](Gjenbruk/Hvordan-beskrivelser%20for%20gjenbruk/SonarQube%20Cloud%20kodekvalitetsverktøy.md).
