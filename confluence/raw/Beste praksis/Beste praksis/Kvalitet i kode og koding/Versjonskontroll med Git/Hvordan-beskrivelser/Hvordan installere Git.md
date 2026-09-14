---
tags:
  - howto-kvakk-git
  - howto-kvakk
  - kb-how-to-article
---

# Hvordan installere Git

Status: <mark style="background: #baf3db;">I BRUK</mark>

Når du skal arbeide med kode som er versjonskontrollert med Git, må du ha en Git-klient der du skal jobbe med koden slik at du kan hente ned nyeste versjon og lagre endringer i koden. Det er mange ulike situasjoner hvor vi i SSB bruker Git og ofte finnes det allerede en Git-klient der vi jobber. Eksempler hvor Git allerede er installert:

- JupyterLab i produksjonssonen
- DaplaLab
- Linux i produksjonssonen og administrativ sone (f.eks. *sl-sas-work*-tjenerne)
- Citrix-klientene for administrativ sone og produksjonssone

Dersom du skal jobbe med koden på din egen maskin, må du installere Git på maskinen. Mange kodeverktøy har innebygget støtte for Git, men dersom du ikke bruker et slikt, følger du instruksjonene nedenfor og installerer Git selv.

## \uD83D\uDCD8 Instruksjoner

> [!IMPORTANT]
> Før du begynner med selve installasjonen av Git: Sørg for å ha installert en tekst-editor som du er komfortabel med. Denne kommer du til å angi i Git-installasjonen som standard editor og den vil åpnes automatisk av Git når det trengs tekst-input. For eksempel vil Git be deg om å skrive en tekst som beskriver endringene du har gjort, når du lagrer (committer) dem.

I mange sammenhenger trenger man å få tildelt midlertidige administrator-rettigheter for å få installert programmer på egen maskin. Det trenger du ikke for å installere Git.

1. Velg installasjonspakke fra <https://git-scm.com/downloads>.
2. Hvis du har Windows og er usikker på hvilken versjon du skal installere, gå til <https://git-scm.com/download/win> og velg 64-bit-versjonen.
3. Følg instruksjonene underveis i installasjonen. Når du blir spurt om standard-editor, angi den teksteditoren du ønsker. Dersom du ikke angir en, settes standard editor til å være [VIM](https://www.vim.org/), som kan være utfordrende å bruke dersom man ikke er kjent med den fra før.
4. Når du har installert Git lokalt på egen maskin, er neste steg å konfigurere Git. Se [Hvordan konfigurere git (git config) etter SSB-standard?](Hvordan%20konfigurere%20git%20(git%20config)%20etter%20SSB-standard_.md)

> Tips: Lag en katalogstruktur på maskinen der du jobber, som gjør at du enkelt finner igjen koden når du skal jobbe med den. Et forslag kan være å ha en “kode”-katalog under brukerkatalogen din, hvor du har alle kataloger for Git-repoer.

## \uD83D\uDCCB Relaterte artikler

##### Filtrer etter etikett

Det er ingen elementer i de valgte etikettene akkurat nå.
