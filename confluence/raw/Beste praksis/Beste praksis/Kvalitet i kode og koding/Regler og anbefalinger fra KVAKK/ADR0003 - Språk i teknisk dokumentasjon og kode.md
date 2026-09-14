
# ADR0003 - Språk i teknisk dokumentasjon og kode

> [!IMPORTANT]
> Originalen til denne siden ligger på GitHub med link [ADR0003](https://github.com/statisticsnorway/adr/blob/main/docs/0003-teknisk-dokumentasjon-spraak.md). Men det er ikke alle lesere av disse sidene som har GitHub-konto, så derfor har vi kopiert ut teksten her, slik at informasjonen blir tilgjengelig for alle.

- Dato: 23.11.2021
- Besluttende myndighet: Seksjon for IT-arkitektur

## Status

Godkjent.

## Kontekst

Det er meldt inn spørsmål vedrørende hvilket språk man skal bruke i teknisk dokumentasjon og ved utvikling av kode. Begrunnelse og anbefaling bygger på Kostra sine erfaringer og retningslinjer for bruk av språk i dokumentasjon av løsninger. Det forslås at "Principles and Guidelines on Building Multilingual Applications for Official Statistics" blir del av SSBs beste praksis for teknisk dokumentasjon og kode.

## Beslutning

Bruk av språk i dokumentasjon Overodnede dokumentasjon - som system- og brukerdokumentasjon - skrives på norsk (inklusive modulbeskrivelser etc).  
Underliggende teknisk dokumentasjon (typisk API-dokumentasjon) skrives på engelsk, det samme gjelder kodespråket og alle commit-meldinger (innsjekkingsmeldinger til versjonskontrollsystemet).  
Anbefalingen handler ikke bare om potensiell deling med andre, men også for å ha mulighet for å åpne for engelskspråklige utviklere (ref sourcing-strategien). Vi binder altså bruk av internasjonale standarder som skal bidra til samarbeid opp mot behovet for å skrive kode alle kan forstå. "Samarbeid på tvers av landegrenser, og innføring av standarder som GSPBM for arbeidsprosesser og GSIM for informasjonsmodeller, gjør at vi enklere kan utveksle og dele programvarekomponenter på tvers av landegrenser. Dette krever mer av oss enn at vi støtter f.eks. GSBPM og GSIM, det betyr også at koden vi skriver må kunne forstås av andre enn oss, samtidig som vi også sikrer at flerspråklighet er bygget inn i løsningene vi bygger fra begynnelsen av.  
UNECE har utarbeidet en veiledning for flerspråklige applikasjoner, og og gir gode prinsipper og retningslinjer for hvordan flerspråklige applikasjoner skal utvikles. Videre må vi skrive koden vår på et språk som alle har mulighet for å forstå. All kode (variabelnavn, klassenavn, metodenavn, pakkenavn, API-endepunkt, eventuelle kommentarer og lavnivå dokumentasjon som maskinlesbar API dokumentasjon (Swagger, RAML etc), i tillegg til innsjekkingmeldinger skal skrives på engelsk. Alle funksjoner/metoder skal beskrive hva variabelen er og hva funksjoner og metoder gjør.

**Eksempel**

metode: `convertJsonToCsv()`  
metode: `getUniqeKeywords()`  
metode: `updateDatasetFrom()`  
variabler: `title, description, keyword`

Se [Multilingual applications for official statistics](https://unece.org/statistics/publications/multilingual-applications-official-statistics)

I retningslinjer og krav til løsningsarkitektur på Virksomhetsarkitekturområdet bør vi vise til konkrete eksempler som utviklere og arkitekter kan bruke, retningslinjene bør inkludere UNECEs "Principles and Guidelines on Building Multilingual Applications for Official Statistics".

All kode (variabelnavn, klassenavn, metodenavn, pakkenavn, API-endepunkt, eventuelle kommentarer og "lavnivå" dokumentasjon som for eksempel maskinlesbar API dokumentasjon (Swagger, RAML etc) skal skrives på engelsk. Overordnet dokumentasjon som system- og brukerdokumentasjon skrives på norsk (nynorsk/bokmål).

## Konsekvenser

**Fordeler**  
Bidra til økt standardisering av teknisk dokumentasjon Bidrar til at engelskspråklige utviklere raskere kan bidra i videreutvikling av komponenter og tjenester Øker mulighetene for deling av komponenter og tjenester på tvers av landegrenser Valgmulighetene på eksterne konsulenter øker

**Ulemper**  
Ikke alle utviklere føler seg komfortable med å skrive på engelsk Beskrivelsene kan bli mindre presise Kan oppfattes som utfordrende å skrive teknisk dokumentasjon på to språk.
