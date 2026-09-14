
# Hvordan importere egendefinerte funksjoner i Jupyter Notebooks?

Status: <mark style="background: #baf3db;">I BRUK</mark>

Både i standard python og i Jupyter Notebooks er det lett å importere moduler/filer som ligger i samme mappe som filen man vil importere modulen inn i. Det er bare å skrive: `from <modulnavn> import <funksjonsnavn>`. Men hva hvis man vil importere moduler som ligger andre steder i katalogtreet?

I Jupyter Notebooks så kan/vil importsystemet oppføre seg annerledes enn i standard python. For å gardere for dette så kan man enten sette opp *packages* i `pyproject.toml`, noe som gjør at python søker etter funksjoner i andre deler av katalogtreet. (Eller man kan bruke `ProjectRoot` fra “hjelpe-pakken” [ssb-fagfunksjoner](https://pypi.org/project/ssb-fagfunksjoner/). - men denne skal kanskje fjernes på sikt, så vi anbefaler å bruke lokal pakke.)

## Bruk av packages i pyproject.toml (anbefalt)

Den anbefalte løsningen er å sette opp "packages" i `pyproject.toml` til å inkludere de topp-katalogene du vil at python skal søke gjennom når den leter etter funksjoner. Se [eksempel i linje 8-14 i pyproject.toml](https://github.com/statisticsnorway/tech-coach-importtest/blob/main/pyproject.toml#L8-L14) i tech-coach-importtest repoet.

Sett opp tilsvarende i ditt repo. Hvis du oppretter et nytt repo med `ssb-project`-kommandoen etter slutten av august 2024, så får du med ferdig oppsett for dette.

De lokale pakkene blir da installert som "[editable installs](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs)" når du kjører kommandoen `poetry install` eller `ssb-project build`. Du må huske å kjøre en av disse kommandoene før du prøver å importere de aktuelle funksjonene.

Etter det kan du importere funksjonene på samme måte som i vanlig python, slik som vist i her:

```py
from functions.fizzbuzz import fizz
from package1.module1 import pluss
from package2.module3 import gange
```

Husk at du må restarte kernel’en når du gjør endringer i de importerte funksjonene.

## Eksempler

Du finner flere eksempler på siden [Kodeeksempler på gjenbruk med Python](../Gjenbruk%20i%20egen%20kode/Kodeeksempler%20på%20gjenbruk%20med%20Python.md).
