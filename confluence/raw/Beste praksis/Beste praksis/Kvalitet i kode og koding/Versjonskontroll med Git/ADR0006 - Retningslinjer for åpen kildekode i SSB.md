
# ADR0006 - Retningslinjer for åpen kildekode i SSB

> [!IMPORTANT]
> Originalen til denne siden ligger på GitHub med link [ADR0006](https://github.com/statisticsnorway/adr/blob/main/docs/0006-aapen-kildekode-i-ssb.md). Men det er ikke alle lesere av disse sidene som har GitHub-konto, så derfor har vi kopiert ut teksten her, slik at informasjonen blir tilgjengelig for alle.

- Status: Akseptert
- Myndighet: Seksjon for IT-arkitektur
- Dato: 2022-03-07
- Oppdatert: 2024-10-21

## Kontekst og problemstilling

Mye av koden SSB har produserer er kun tilgjengelig internt. For å skape tillit er åpenhet og gjennomsiktighet i det SSB gjør viktig. Derfor bør mest mulig av koden og dokumentasjonen vi skriver være åpen tilgjengelig, på lik linje med statistikken vi produserer. At offentlig finansierte løsninger er mest mulig tilgjengelig er et viktig prinsippp. Motivasjonen er da ikke hovedsakelig gjenbruk, selv om det selvsagt er en heldig bieffekt. Motivasjonen er først og fremst åpenhet og gjennomsiktighet i de digitale løsningene. Retningslinjene som beskrives her legger seg tett opptil [NAV sine retningslinjer](https://github.com/navikt/offentlig). I denne ADR har vi gjort vurderinger av hvordan SSBs kildekode skal tilgjengeliggjøres på Github.

## Beslutningsdrivere

- [Prinsipp 8: Åpen kildekode](../../../../Virksomhetsarkitektur/Virksomhetsarkitektur/Prinsipp%208_%20Åpen%20kildekode.md)
- [Overordnede arkitekturprinsipper fra Digitaliseringsdirektoratet](https://www.digdir.no/samhandling/prinsipp-5-del-og-gjenbruk-losninger/1062)

## Hvilke mekanismer for tilgjengelighet på GitHub er vurdert

- Public repo - Skal brukes når kildekoden kan være åpen og sikkerhets- og sensitivitetsshensyn er ivaretatt.
- Internal repo- Skal brukes når man av sikkerhetsmessige grunner ikke kan gjøre kildekoden åpen for allmennheten (utenfor SSB).
- Private repo - Skal kun brukes når sensitivitetshensyn tilsier at koden ikke kan tilgjengeliggjøres for andre enn utvalgte personer (krever godkjenning).

## Vurderte løsninger

- Åpen kildekode som standard med unntak av sikkerhetsmessige hensyn
- Intern kildekode som standard og åpne bare utvalgte kildekodelagre

## Definisjoner

- **Produksjonskode**: All kode som inngår i produkter som releases i SSB. For statistikkproduksjon: All kode som kan påvirke tallene i produsert statistikk.

## Beslutning

**Public repo**: Alle som jobber med produksjonskode i SSB skal etterstrebe allmenn tilgjengeliggjøring av sin kildekode på GitHub. For at kode skal kunne være åpen og tilgjengelig for allmenheten må den oppfylle SSBs kriterier for åpen kildekode nedenfor. Alle ansatte som skriver kode skal derfor etterstrebe å oppfylle disse kriteriene. Teamet som eier koden har ansvaret for vurdere om koden er trygg å distribuere som åpen kildekode. Dersom koden overføres til et nytt team, må dette teamet gjøre en ny vurdering. Dette ansvaret gjelder i kodens levetid. Alle på internett vil kunne se kildekoden, men kun de med eksplisitte rettigheter kan gjøre endringer.

**Internal repo**: Dette er standard valg for repoer i SSB og skal brukes når koden inneholder informasjon som anses utrygt at eksterne får tilgang til. Eksempler på slik informasjon er brannmurregler, oppkoblingsinformasjon mot databaser eller annen teknisk informasjon som ikke kan deles med eksterne. Det stilles ingen speiselle krav eller godkjenninger for å gjøre et repo internt. Alle medlemmer i organisasjonen vil få lesetilgang, men skrivetilgang må eksplisitt tildeles.

**Private repo**: Det er kun anledning til å lukke et repo hvis den inneholder kode eller dokumentasjon som er unntatt offentligheten. Et lukket repo vil sikre at kun godkjente personer kan ha tilgang til kildekoden (uavhengig av om disse er interne eller eksterne). Imidlertid stilles det krav om begrunnelse for lukking av et repo, og som må godkjennes av *Seksjon for IT-arkitektur* (se under). Når godkjenning foreligger og repoet er lukket vil bare inviterte bidragsytere kunne se og endre kildekoden, i tillegg til organisasjonens Github administratorer.

### Kriterier for public repo

Forutsetninger for at kildekode kan være åpen:

1. Repoet må inneholde en [LICENSE.md](https://github.com/statisticsnorway/adr/blob/main/docs/0006-aapen-kildekode-i-ssb.md#lisensiering), [SECURITY.md](https://github.com/statisticsnorway/adr/blob/main/docs/0006-aapen-kildekode-i-ssb.md#sikkerhet) og en forklarende `README.md`
2. Kildekode skal ikke inneholde ukrypterte passord og hemmeligheter. Les mer om hva som betraktes som hemmeligheter [Hva anses som hemmeligheter i kode i SSB?](Hvordan-beskrivelser/Hvordan%20håndtere%20hemmeligheter%20og%20passord%20i%20git_/Hva%20anses%20som%20hemmeligheter%20i%20kode%20i%20SSB_.md).
3. Data skal ikke lagres på GitHub, med mindre det er mindre mengder testdata eller små eksempler, og det kun inneholder åpne data.
4. Følgende [Branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule#creating-a-branch-protection-rule) må være satt på repoet:

   - `Requires a pull request before merging`
   - `Require approvals` minimum 1 approval
   - `Dismiss stale pull request approvals when new commits are pushed`
   - `Do not allow bypassing the above settings`
5. Repoer som er public skal vedlikeholdes aktivt, public repoer som ikke har hatt oppdateringer i løpet av 12 måneder settes internal.
6. Repoer som ikke har hatt oppdateringer i løpet av 24 måneder arkiveres.
7. Arkiverte repoer bevares i 10 år, og kan gjenopprettes av kundeservice på forespørsel.
8. Arkiverte repoer eldre en 10 år slettes.

Enkelte tiltak kan ikke gjennomføres før repoet er satt til public. Etter repoet er public er følgende kritere også gjeldende:

1. `Private vulnerability reporting` må være aktivert for repoet. Se [her](https://docs.github.com/en/code-security/security-advisories/repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository) for oppsettsveiledning.

#### Lis**ensiering**

Alle åpne repoer skal ha en lisensfil i rotkatalogen til repositoriet. Denne filen skal hete LICENSE.md.

SSB lisensierer kode under MIT-lisensen: (Kopier/lim inn teksten, men endre til riktig `<YEAR>`)

```java
# The MIT License

Copyright <YEAR> Statistisk sentralbyrå - Statistics Norway

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
USE OR OTHER DEALINGS IN THE SOFTWARE.

```

Siden dette er MIT-lisensen, en fri lisens, så er det ikke så viktig om året er oppdatert.

Det er ikke behov for å endre årstall uten en spesifikk grunn. Ved behov for å endre årstall, er det viktig at dette gjøres sammen med endring av kode.

### **Kriterier for når GPL-kravene trigges**

1. **Referanse til GPL-lisensierte biblioteker (*****Aggregation*****):**

   - Hvis et prosjekt **refererer** til [GPL-lisensierte biblioteker](https://www.gnu.org/licenses/gpl-3.0.html) via `import`- eller `library()`-kall i R eller Python, anses dette som **aggregering (*****aggregation*****)**, ikke som et **derivativt arbeid (*****derivative work*****)**.
   - **Konsekvens:** Prosjektet kan fortsette å bruke SSBs foretrukne lisens, [MIT-lisensen](https://opensource.org/licenses/MIT), så lenge det ikke distribueres som en samlet binær eller integrert løsning.
2. **Inkludering eller modifikasjon av GPL-kode (*****Derivative Work*****):**

   - Hvis GPL-lisensiert kode **modifiseres**, **kombineres** eller **distribueres sammen med** prosjektkoden som en integrert løsning, anses dette som et **derivativt arbeid (*****derivative work*****)**.
   - **Konsekvens:** Hele prosjektet må distribueres under GPL ved ekstern distribusjon.
3. **Intern bruk (*****Internal Use*****):**

   - Hvis koden **ikke distribueres eksternt**, men kun brukes internt (inkludert i private og interne kildekoderepositorier), **utløses ingen lisenskrav**.

### Krav om lisensendring til GPL

Hvis prosjektet distribueres eksternt og inkluderer GPL-lisensiert kode som beskrevet i punkt 2, **må lisensen endres til GPL før distribusjon**. Prosjektteamet har ansvar for å sikre korrekt lisensiering i henhold til GPLs vilkår.

#### **Sikkerhet**

Alle kodebaser skal ha en sikkerhetspolicy-fil i rotkatalogen til repositoriet. Denne filen skal hete `SECURITY.md`. Dette er for å gi eksterne brukere instruksjoner for rapportering av sårbarheter i prosjektet.

Forslag til innhold i `SECURITY.md` under: (Kopier/lim inn teksten i din `SECURITY.md` i root i ditt repo, men endre url med ditt repo-navn)

```java
# Security Policy

SSB takes the security of our software products and services seriously, which 
includes all source code repositories managed through our GitHub organization.

We believe that responsible disclosure of security vulnerabilities helps us ensure
the security and privacy of all our users.

## Reporting a Vulnerability

If you believe you have found a security vulnerability in any of SSB's GitHub
repositories, please report it to us using the 
[Github Private vulnerability reporting tool](https://github.com/statisticsnorway/<ditt-repo>/security/advisories).

```

### Kriterier for private repo

Forutsetninger for private repo:

1. Før man kan gjøre et repo private, må det lages en begrunnelse for hvorfor det er nødvendig å skjerme det fra resten av SSB. Begrunnelsen skal sendes til *seksjon for IT-arkitektur* for godkjenning. Begrunnelsen må være godkjent før repoet kan gjøres private.
2. Kildekode skal ikke inneholde ukrypterte passord og hemmeligheter. Les mer om hva som betraktes som hemmeligheter [Hva anses som hemmeligheter i kode i SSB?](Hvordan-beskrivelser/Hvordan%20håndtere%20hemmeligheter%20og%20passord%20i%20git_/Hva%20anses%20som%20hemmeligheter%20i%20kode%20i%20SSB_.md).
3. Data skal ikke lagres på GitHub, med mindre det er mindre mengder testdata eller små eksempler, og det kun inneholder åpne data.
4. Følgende [Branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule#creating-a-branch-protection-rule) må være satt på repoet:

   - `Requires a pull request before merging`
   - `Require approvals` minimum 1 approval
   - `Dismiss stale pull request approvals when new commits are pushed`
   - `Do not allow bypassing the above settings`
5. Et private repo kan ikke forkes.

### Positive konsekvenser

- Åpenhet og gjennomsiktighet i SSBs digitale løsninger skaper tillit
- Fokus på å skrive ren og godt strukturert kode som er enkel å vedlikeholde
- Bidrar til samarbeid
- Eksterne kan foreslå forbedringer i koden vår
- Bidrar til å vise frem SSB som en kompetansebedrift
- Kildekode som ikke kan være åpen av sikkehetshensyn kan fortsatt deles internt som *innersource*.
- Det er anledning til å ha et private repo når koden må være unntatt offentligheten, slik at kun godkjente personer får tilgang. Og at denne typen repoer også kan bruke Github istedenfor egne separate løsinnger.

### Negative konsekvenser

- Lav kvalitet og dårlig eller ingen aktiv forvaltning på åpen kode kan bidra til negativt omdømme.

## Lenker

- [Statistisk sentralbyrå sin organisasjonsside på GitHub](https://github.com/statisticsnorway)
