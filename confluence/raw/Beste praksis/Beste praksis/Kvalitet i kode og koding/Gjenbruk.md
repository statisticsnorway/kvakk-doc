
# Gjenbruk

Forvalter av siden: [KVAKK-gruppa](/wiki/spaces/KOD)

Status: <mark style="background: #baf3db;">I BRUK</mark>

## Introduksjon

Gjenbruk er et av [Arkitekturprinsipper](../../../Arkitektur/Arkitektur/Hvor%20skal%20vi_/Arkitekturprinsipper.md). Gjenbruk gjør at man slipper å kode det samme som noen allerede har gjort, og er lurt med tanke på kostnadseffektivitet, vedlikehold og sikkerhet.

## Terminologi

Temaet gjenbruk bruker flere ord og begreper fra R og Python i sine beskrivelser. Følgende er noen av de som er mest relevante.

| **Begrep** | **Python** | **R** |
| --- | --- | --- |
| Modul | En modul er en .py-fil som som inneholder en samling av funksjoner og klasser. Den kan importeres og brukes i andre pythonmoduler eller skript. | Begrepet modul brukes ikke i R. |
| Pakke | En pakke er en mappe som inneholder en `__init__.py` fil. Mappen kan også inneholde .py-filer og underpakker. | En pakke er en samling av R-funksjoner, kompilert kode og testdata, som er lagret under et bestemt format. En R-pakke inkluderer dokumentasjon som beskriver funksjonene og hvordan man bruker dem. |
| Bibliotek | En samling av en eller flere pakker, ment for gjenbruk og ofte publisert på [PyPI](https://pypi.org/). | Bibliotek og pakker brukes vanligvis om hverandre i R. Men teknisk sett refererer et bibliotek i R til mappen der R-pakker er installert. |
| Kodebibliotek | Brukes som et fellesbegrep for en samling gjenbrukbar kode og tilsvarer begrepet bibliotek i python og begrepet pakke i R. | Brukes som et fellesbegrep for en samling gjenbrukbar kode og tilsvarer begrepet bibliotek i python og begrepet pakke i R. |
| Funksjon | En funksjon brukes til å utføre en spesifikk oppgaver. Den består av en blokk med organisert, gjenbrukbar kode. Funksjon kan/skal gjenbrukes. I både R og Python er funksjoner nyttige for å skrive klar, forståelig og gjenbrukbar kode. | En funksjon brukes til å utføre en spesifikk oppgaver. Den består av en blokk med organisert, gjenbrukbar kode. Funksjon kan/skal gjenbrukes. I både R og Python er funksjoner nyttige for å skrive klar, forståelig og gjenbrukbar kode. |

## Fire typer gjenbruk

Punktene nedenfor beskriver fire typer gjenbruk, med fordeler, ulemper, eksempler og når de bør brukes.

1. [Gjenbruk i egen kode](Gjenbruk/Gjenbruk%20i%20egen%20kode.md)
2. [Gjenbruk ved kopiering](Gjenbruk/Gjenbruk%20ved%20kopiering.md)
3. [Gjenbruk av kodebiblioteker](Gjenbruk/Gjenbruk%20av%20kodebiblioteker.md)
4. [Fellestjenester](Gjenbruk/Fellestjenester.md)

## Praksisanbefalinger

Definisjon av regel, anbefaling, produksjonskode og kildekode finner du på [Kvalitet i kode og koding](../Kvalitet%20i%20kode%20og%20koding.md).

- [Regler og anbefalinger fra KVAKK](Regler%20og%20anbefalinger%20fra%20KVAKK.md)
- [Hvordan-beskrivelser for gjenbruk](Gjenbruk/Hvordan-beskrivelser%20for%20gjenbruk.md)

  - [Hvordan lage et python-bibliotek etter SSB standard?](Gjenbruk/Hvordan-beskrivelser%20for%20gjenbruk/Hvordan%20lage%20et%20python-bibliotek%20etter%20SSB%20standard_.md)
  - [SonarQube Cloud kodekvalitetsverktøy](Gjenbruk/Hvordan-beskrivelser%20for%20gjenbruk/SonarQube%20Cloud%20kodekvalitetsverktøy.md)
