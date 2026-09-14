---
tags:
  - howto-kvakk-git
  - kb-how-to-article
  - github
  - git
---

# Hvordan konfigurere git (git config) etter SSB-standard?

Status: <mark style="background: #baf3db;">I BRUK</mark>

## gitconfig

Det meste av oppsettet og konfigurasjonen av git lagres i en fil som heter `.gitconfig`, og som ligger rett under hjemmekatalogen til den enkelte bruker. Du kan sette verdier i denne filen ved å bruke kommandoen `git config --global <setting>`.

### Fellesting

Man må alltid sette opp navn og e-post i git. Hvis du bruker både GitHub og Bitbucket så følg beskrivelsen nedenfor for den av dem du bruker mest. Og for den du bruker minst, gå til hvert enkelt av repoene du har klonet ut fra den og kjør tilhørende kommandoer, men fjern `--global` opsjonen. Da gjelder den configen bare for det aktuelle repoet.

#### E-post og navn GitHub

Sett navn og e-post til det du bruker i GitHub. Hvis du har valgt “Keep my email address private” i GitHub så bruker du den e-postadressen som er registrert der. Se siden om [Navn og e-post i GitHub](../../../../../Arne%20Sørli/Oversikt/Git/Hvordan%20sette%20opp%20git%20(git%20config)_/Navn%20og%20e-post%20i%20GitHub.md) for detaljer om hvordan du finner dette.

Eksempel:

```java
git config --global user.email "81394972+my-usernameb@users.noreply.github.com"
git config --global user.name "Ola Nordmann"
```

```java
 
```

### Dapla og Jupyter i prod-sonen

På Dapla er riktig gitconfig allerede satt for deg. På Jupyter i prodsonen (sl-jupyter-p.ssb.no) så kjørerer du følgende kommando for å sette anbefalt gitconfig:

```bash
kvakk-git-tools
```

Husk også at i hvert enkelt repo skal det være en `.gitattributes`-fil med [Hvordan konfigurere git (git config) etter SSB-standard?](Hvordan%20konfigurere%20git%20(git%20config)%20etter%20SSB-standard_.md).

### Prod-sone Windows, Citrix

For Citrix “Produksjonssone 2025”:

1. Åpne et command prompt vindu (ikke Git Bash) ved å skrive `cmd` i søkefeltet nede til venstre.
2. Kjør følgende kommandoer:

   ```java
   git clone -c http.sslVerify=false https://github.com/statisticsnorway/kvakk-git-tools.git
   python kvakk-git-tools\kvakk_git_tools\ssb_gitconfig.py
   ```

Husk også at i hvert enkelt repo skal det være en `.gitattributes`-fil med [Hvordan konfigurere git (git config) etter SSB-standard?](Hvordan%20konfigurere%20git%20(git%20config)%20etter%20SSB-standard_.md).

### Prod-sone Windows, VDI

Skriptet [ssb\_gitconfig.py](https://github.com/statisticsnorway/kvakk-git-tools/blob/main/kvakk_git_tools/ssb_gitconfig.py) støtter ikke VDI i prod-sonen ennå, så her må git konfigureres manuelt. Gjør først oppsettet av python og poetry som beskrevet på siden [Hvordan sette opp Python og Poetry på Windows i prod-sonen?](../../../../../Avdelingen%20for%20IT/Avdelingen%20for%20IT%20Home/S703%20%20-%20IT%20Partner/Team%20tech%20coach/Tech-coach%20FAQ/Hvordan%20sette%20opp%20Python%20og%20Poetry%20på%20Windows%20i%20prod-sonen_.md), før du starter på beskrivelsen her.

Du må installere verktøyet `nbstribout` for å få automatisk fjerning av output fra Jupyter Notebooks. Siden `poetry` på VDI er installert med verktøyet `pipx`, så anbefales det å bruke `pipx` til å installere `nbstripout` også. Det gjør du med kommandoen:

```java
pipx install nbstripout
```

Deretter kjører du følgende kommandoer:

```java
# I tillegg skal ~/.gitconfig inneholde følgende seksjon for å forhindre at
# Jupyter Notebooks comittes med output. Det må kombineres med at .gitattributes
# i de aktuelle repoene må inneholde *.ipynb filter=nbstripout (se nedenfor).
# Bytt ut username med ditt brukernavn.
git config --global diff.ipynb.textconv "C:/Users/username/.local/bin/nbstripout.exe -t"
git config --global filter.nbstripout.clean "C:/Users/username/.local/bin/nbstripout.exe"
git config --global filter.nbstripout.smudge cat
git config --global filter.nbstripout.required true
git config --global filter.nbstripout.extrakeys "metadata.kernelspec metadata.language_info.version cell.metadata.pycharm metadata.language_info.pygments_lexer metadata.language_info.codemirror_mode.version"

# Be git om å ignorere selvsignert sertifikat.
git config --global http.sslverify false
```

For resterende oppsett følger du beskrivelsen for oppsett for Adm-sone Windows, bortsett fra det med fjerning av output fra Jupyter notebooks, hvor du bruker det som er beskrevet ovenfor. Se: [Hvordan konfigurere git (git config) etter SSB-standard?](Hvordan%20konfigurere%20git%20(git%20config)%20etter%20SSB-standard_.md)

### Prod-sone Linux (bortsett fra Jupyter)

Bruk følgende kommandoer for å sette anbefalt gitconfig når du jobber på Linux i prod-sonen (det gjelder også Jupyter i prod-sonen):

```bash
git clone -c http.sslVerify=false https://github.com/statisticsnorway/kvakk-git-tools.git
python kvakk-git-tools/src/kvakk_git_tools/ssb_gitconfig.py
```

GitHub-tilgang og nødvendig oppsett er foreløpig satt opp på disse Linux-serverne: [Linux-servere i prodsonen som trenger tilgang til GitHub](../../../../../Arne%20Sørli/Oversikt/Git/Linux-servere%20i%20prodsonen%20som%20trenger%20tilgang%20til%20GitHub.md).

Husk også at i hvert enkelt repo skal det være en `.gitattributes`-fil med [Hvordan konfigurere git (git config) etter SSB-standard?](Hvordan%20konfigurere%20git%20(git%20config)%20etter%20SSB-standard_.md).

### Lokal PC

Git bør konfigureres med et grafisk diff- og mergeverktøy. Det finnes mange, men [Meld](https://meldmerge.org/) er gratis, av de beste, og finnes for både Windows, Linux og Mac. Installasjon av Meld:

1. Du trenger lokaladministratorrettigheter for å installere Meld. Send en henvendelse til [Kundeservice](https://ssb.tmsportal.no/userweb/UserWebStart.aspx) og be om lokaladministratorrettigheter for å installere Meld, alternativt at de installerer Meld for deg.
2. Last ned og installer Meld med standard opsjoner.

I tillegg må du [installere Python](https://www.python.org/downloads/windows/), og det anbefales å bruke samme hovedversjon som på Dapla dvs. versjon 3.12. Bruk foreslått installasjonssti og huk av for “Add Python to PATH”.

Verktøyet `nbstripout` fjerner output fra Jupyter notebooks, og det kjører fra kommandolinja. Terminalvinduet i Windows bruker UTF-16 som standard. Dette må endres til UTF-8, og det gjør du ved å følge [Hvordan sette opp Windows til å bruke UTF-8 som tegnsett?](Hvordan%20konfigurere%20git%20(git%20config)%20etter%20SSB-standard_/Hvordan%20sette%20opp%20Windows%20til%20å%20bruke%20UTF-8%20som%20tegnsett_.md).

#### Windows

Åpne et terminalvindu og installerer verktøyet `nbstripout`, med kommandoen:

```java
 py -m pip install --user nbstripout 
```

Bruk deretter gitconfig-eksemplet nedenfor, men bytt ut `aei` med ditt brukernavn og sjekk at stien til python stemmer med det som er på din maskin, samt bytt ut navn og e-postadresse.

```bash
[user]
    name = Ola Nordmann
    email = 81394972+my-usernameb@users.noreply.github.com
[core]
    autocrlf = input
    eol = lf
[diff]
    tool = meld
    algorithm = histogram
[diff "ipynb"]
    textconv = C:/Users/aei/AppData/Local/Programs/Python/Python312/python.exe -m nbstripout -t
[difftool]
    prompt = false
[difftool "meld"]
    path = C:/Program Files/Meld/Meld.exe
[fetch]
    prune = true
[filter "nbstripout"]
    clean = C:/Users/aei/AppData/Local/Programs/Python/Python312/python.exe -m nbstripout
    smudge = cat
    required = true
    extrakeys = metadata.kernelspec metadata.language_info.version cell.metadata.pycharm metadata.language_info.pygments_lexer metadata.language_info.codemirror_mode.version
[merge]
    tool = meld
[mergetool]
    prompt = false
    keepBackup = false
[mergetool "meld"]
    path = C:/Program Files/Meld/Meld.exe
[init]
    defaultBranch = main
[filter "lfs"]
    process = git-lfs filter-process
    required = true
    clean = git-lfs clean -- %f
    smudge = git-lfs smudge -- %f
[push]
    autoSetupRemote = true
    default = current
[pull]
    ff = only
```

#### Linux med WSL2

På Windows kan man også kjøre Linux via *Windows Subsystem for Linux* (WSL). I Linux anbefales det å installere nbstripout via pipx, og det gjør du med kommandoene:

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
```

Når pipx er installert og virker (sjekk at `pipx --version` virker fra terminalvinduet) så installerer du verktøyet som stripper output fra Jupyter notebooks, nbstripout, med kommandoen: `pipx install nbstripout`

Bruk deretter gitconfig-eksemplet nedenfor, men bytt ut `arneso` med ditt linux brukernavn og `aei` med ditt Windows brukernavn..

```java
[user]
    name = Ola Nordmann
    email = 81394972+my-usernameb@users.noreply.github.com
[core]
    autocrlf = false
    editor = nano
    eol = lf
[credential]
    helper = cache --timeout=86400
[diff]
    tool = meld
    algorithm = histogram
[diff "ipynb"]
    textconv = /home/arneso/.local/bin/nbstripout -t
[difftool]
    prompt = false
[difftool "meld"]
    cmd = /mnt/c/Program\\ Files/Meld/meld.exe \"$(wslpath -aw $LOCAL)\" \"$(wslpath -aw $REMOTE)\"
[fetch]
    prune = true
[filter "lfs"]
    clean = git-lfs clean -- %f
    smudge = git-lfs smudge -- %f
    process = git-lfs filter-process
    required = true
[filter "nbstripout"]
    clean = /home/arneso/.local/bin/nbstripout
    smudge = cat
    extrakeys = metadata.kernelspec metadata.language_info.version cell.metadata.pycharm metadata.language_info.pygments_lexer metadata.language_info.codemirror_mode.version
[init]
    defaultBranch = main
[merge]
    tool = meld
[mergetool]
    keepBackup = false
    prompt = false
[mergetool "meld"]
    cmd = /mnt/c/Program\\ Files/Meld/meld.exe --auto-merge \"$(wslpath -aw $LOCAL)\" \"$(wslpath -aw $BASE)\" \"$(wslpath -aw $REMOTE)\" --output \"$(wslpath -aw $MERGED)\"
[pull]
    ff = only
[push]
    autoSetupRemote = true
    default = current
```

## gitattributes

Filen `.gitattributes` skal ligge i toppkatalogen i hvert enkelt repo. Den er viktig for to ting: Håndtere linjeendinger korrekt uavhengig av den enkelte brukers oppsett, og håndtering av filter for å fjerne output fra Jupyter Notebooks før filer comittes. Fila `.gitattributes` skal inneholde disse linjene:

```java
* text=auto eol=lf
*.ipynb filter=nbstripout
*.ipynb diff=ipynb
```

Når du endrer på den første linja (eol=lf) eller filteret, eller setter dem opp for første gang, så må du kjøre kommandoene nedenfor for å få aktivert det nye oppsettet:

```bash
# Fra topp-katalogen i det aktuelle repoet
git add --renormalize .
git commit -m"Renormalize after update of gitattributes"
```

Er git-repoet opprettet med [ssb-project](https://manual.dapla.ssb.no/ssbproject.html) kommandoen, så har repoet automatisk en anbefalt `.gitattributes`-fil.

## gitignore

Hvert enkelt repo bør ha en `.gitignore`-fil i toppkatalogen, og anbefalt `.gitignore`-fil for SSB finner du [her](https://github.com/statisticsnorway/kvakk-git-tools/blob/main/kvakk_git_tools/recommended/gitignore). Fila spesifiserer hvilke filer som git skal ignorere. Et eksempel er data-filer som `*.parquet` og `*.xlsx`. En slik `.gitgnore`-fil hjelper deg til å følge KVAKK-anbefaling [Regler og anbefalinger fra KVAKK](../../Regler%20og%20anbefalinger%20fra%20KVAKK.md) om å skille på kildekode og data, ved at den sikrer at ingen slike data-filer blir sjekket inn i git-repoet ved et uhell.

Er git-repoet opprettet med [ssb-project](https://manual.dapla.ssb.no/ssbproject.html) kommandoen, så har repoet automatisk en anbefalt `.gitignore`-fil.

## Git-repo med anbefalte oppsett

Et alternativ til å kjøre kommandoene ovenfor er å kopiere anbefalt oppsett fra git-repoet kvakk-git-tools. Da må du huske på å legge til navn og e-post som beskrevet under [Hvordan konfigurere git (git config) etter SSB-standard?](Hvordan%20konfigurere%20git%20(git%20config)%20etter%20SSB-standard_.md), samt endre “username” til ditt brukernavn der hvor det er aktuelt. Du får tak i filene slik:

```bash
git clone https://github.com/statisticsnorway/kvakk-git-tools.git
cd kvakk-git-tools/recommended       # Du finner anbefalingene i denne katalogen
```

## \uD83D\uDCCB Relaterte artikler

##### Filtrer etter etikett

Det er ingen elementer i de valgte etikettene akkurat nå.
