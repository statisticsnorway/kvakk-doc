---
tags:
  - git
---

# Hva anses som hemmeligheter i kode i SSB?

Status: <mark style="background: #baf3db;">I BRUK</mark>

> [!IMPORTANT]
> Det er det enkelte team som er ansvarlig for ikke å ha ukrypterte hemmeligheter og passord i koden. Denne siden vil oppdateres med felles retningslinjer på hva som anses som hemmeligheter og ikke, etter hvert som det utarbeides. Ansvarlig for siden er sikkerhetssenteret.

### Hemmeligheter

Med hemmeligheter menes sensitive data eller informasjon som skal beskyttes mot uautorisert tilgang til tjenester eller systemer. Dette kan inkludere passord, krypteringsnøkler, tilgangstoken og andre sensitive data som kan utnyttes av ondsinnede aktører hvis de kommer på avveie.

Det er viktig å beskytte disse hemmelighetene ved hjelp av sikkerhetsmekanismer som kryptering, autentisering og autorisasjon. Github og Google har tjenester som kan benyttes for å skille kode fra hemmeligheter. Da kan koden referere til disse hemmelighetene i stedet for å angi de direkte.

Hemmeligheter skal ikke lagres ukryptert i kode eller konfigfiler verken i public/åpne eller private/internal repositories.   
Noen av disse er beskrevet under:

- **Brukernavn og passord (credentials)**  
  Tilgangsautentiseringsinformasjon som brukernavn, passord, API-nøkler, tokens og sertifikater bør aldri være offentlige. Disse brukes til å autentisere en bruker eller applikasjon og gi tilgang til sensitiv data eller systemer. Hvis tilgangsautentiseringsinformasjonen er eksponert, kan en angriper enkelt få uautorisert tilgang til systemet ditt.
- **Private nøkler**  
  Private nøkler brukes for kryptering og dekryptering og skal holdes hemmelige. Hvis en privat nøkkel blir publisert, kan en angriper bruke den til å dekryptere sensitiv informasjon eller utgi seg for å være deg.
- **API-nøkler**  
  API-nøkler brukes til å få tilgang til og kontrollere tredjeparts tjenester og API-er. De må holdes konfidensielle da de kan brukes til å få tilgang til sensitiv data og utføre handlinger på vegne av brukeren.
- **Cluster ID (cluster-navn)**  
  Våre clustere har flere tjenester som er eksponert ut mot internett. De fleste tjenestene benytter dns-alias for å ha et enklere navn å forholde seg til. F.eks. [tid.ssb.no](http://tid.ssb.no), men samtidig vil cluster-navnene også eksponeres i adressene/tjenestene som eksponeres slik at det ved ev. feilkonfigurasjon av backends etc. vil cluster-navn URL’ene kunne misbrukes.

### Sensitiv informasjon

Sensitiv informasjon er ikke helt det samme som hemmeligheter, men kan være informasjon av sensitiv art som personidentifiserende informasjon, kredittkortinformasjon, men også informasjon som kan gi potensielle ondsinnede aktører informasjon som kan brukes til å kartlegge en organisasjons nettverk, infrastruktur og datasystemer.  
Noen av disse er beskrevet under:

- **Personidentifiserende informasjon**  
  Dette inkluderer sensitiv personlig informasjon som personnummer, kredittkortnummer og adresser mm.
- **Konfigurasjonsfiler**  
  Konfigurasjonsfiler kan inneholde sensitiv informasjon om systemets oppsett og konfigurasjon, inkludert tilkoblingsstrenger til databaser, serveradresser- og navn og annen informasjon som ikke bør være offentlig.
- **Infrastrukturkode**  
  IaC som Terraformkode, Ansiblekode mm.
- **Nettverksskisser**
- **Google Secret Manager hemmelighets id’er** (men kan også i noen tilfeller anses som ikke hemmeligheter, se [ADR0026](https://github.com/statisticsnorway/adr/blob/main/docs/0026-behandling-av-identifikatorer.md)).

### Ikke hemmeligheter

- **Bøttenavn** (uten GCP prosjekt ID). Eksempel: `ssb-prod-tech-coach-data-produkt/kilde1_data/inndata/g2021` og [Hvordan håndtere hemmeligheter og passord i git?](../Hvordan%20håndtere%20hemmeligheter%20og%20passord%20i%20git_.md).
- **Filstier**
- **GCP prosjekt ID.** Eksempel `prod-tech-coach-54f3`. (se [ADR0026](https://github.com/statisticsnorway/adr/blob/main/docs/0026-behandling-av-identifikatorer.md))
- **Maskinporten client ID** (se [ADR0026](https://github.com/statisticsnorway/adr/blob/main/docs/0026-behandling-av-identifikatorer.md))
