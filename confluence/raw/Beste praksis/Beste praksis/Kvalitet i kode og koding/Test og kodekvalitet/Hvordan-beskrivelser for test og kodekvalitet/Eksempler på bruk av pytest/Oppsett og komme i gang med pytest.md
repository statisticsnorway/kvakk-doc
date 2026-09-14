
# Oppsett og komme i gang med pytest

Å sette opp `pytest` for å kjøre tester i et Python-prosjekt er ganske enkelt. Her er en trinnvis veiledning for å komme i gang med `pytest`:

### 1. Installere og klargjør `pytest`

Først må du installere `pytest`. Dette kan gjøres enkelt ved hjelp av `poetry`:

```java
poetry add -G dev pytest pytest-cov
```

Verifiser deretter at `pytest` er konfigurert for å finne "src" mappen i prosjektstrukturen ved og å inspisere

filen `pyproject.toml` for "tekst-blokken":

```java
[tool.pytest.ini_options]
pythonpath = ["src"]
```

For prosjekter opprettet med nyere utgaver av `ssb-project` så settes dette automatisk, men for prosjekter opprettet med tidligere utgaver av `ssb-project eller` prosjekter opprettet manuelt så må "tekst-blokken" legges til manuelt.

### 2. Organisere Prosjektet Ditt

Organiser prosjektet ditt slik at testene dine er enkle å finne og kjøre. En typisk prosjektstruktur kan se slik ut:

```java
my_project/
├── src/
│   ├── __init__.py
│   ├── examples/
│   │   ├── __init__.py
│   │   └── example.py
├── tests/
│   ├── __init__.py
│   └── example.py
└── README.md
```

### 3. Skrive Testene Dine

Opprett en testfil (f.eks. `test_example.py`) i `tests/`-mappen og skriv noen enkle tester. La oss anta at vi har en funksjon i `example.py` som vi vil teste:

#### `example.py`

```py
def add(a, b):
  return a + b
```

#### `test_example.py`

```py
from my_module.example import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

```

### 4. Kjøre Testene

For å kjøre testene, naviger til rotkatalogen av prosjektet ditt (der `my_project`-mappen ligger) og kjør `pytest`:

```java
pytest
```

`pytest` vil automatisk finne alle `testfiler` som starter med `test_` eller slutter med `_test.py` og kjøre alle funksjoner som starter med `test_`.

### 5. Se Testresultatene

Når du kjører `pytest`, vil du se en oversikt over testresultatene i terminalen:

```java
============================= test session starts ==============================
...
collected 1 item

tests/test_example.py .                                             [100%]

============================== 1 passed in 0.02s ===============================

```

Slik ser resultatet ut dersom alle testene dine har bestått.

### 6. Kjøre Testene med “coverage”

For å kjøre testene med `pytest-cov`, naviger til rotkatalogen av prosjektet ditt (der `my_project`-mappen ligger) og kjør `pytest`:

```java
pytest --cov --cov-report term-missing
```

### 7. Se Testrapporten fra “coverage”

Når du kjører `pytest-cov`, vil du feks se en oversikt over testresultatene i terminalen ala dette:

```java
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
example.py            9      1    89%   12
test_example.py      15      0   100%
-----------------------------------------------
TOTAL                24      1    96%
```
