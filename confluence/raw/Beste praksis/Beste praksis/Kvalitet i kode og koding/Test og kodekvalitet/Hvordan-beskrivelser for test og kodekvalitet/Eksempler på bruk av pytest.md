
# Eksempler på bruk av pytest

### Hvorfor bruke pytest

`pytest` er et testrammeverk for `python` som gjør det enkelt å skrive, organisere og kjøre tester.

Se: [Oppsett og komme i gang med pytest](Eksempler%20på%20bruk%20av%20pytest/Oppsett%20og%20komme%20i%20gang%20med%20pytest.md) for en oppskrift for å komme i gang med `pytest`

### Kodeeksempler

Repoet [tech-coach-examples](https://github.com/statisticsnorway/tech-coach-examples/tree/main/tests) viser enkel bruk av `pytest` for å komme i gang med testing i python. Koden viser:

1. Eksempler:

   1. Enkel test med basisfunksjon med assert.
   2. Test av funksjon som kaster exception.
   3. Bruk av fixtures for å definere oppsett/rigging/input-verdier til testfunksjonen. Bruk av conftest.py.
   4. Test av pandas dataframe hvor man definerer fasit og sammenligner kolonner, rader og enkeltverdier.
   5. Lesing av fasit fra fil.
   6. Testing av float-verdier. Ofte egne test-funksjoner.
2. Konfigurasjon av pytest (i pyproject.toml).

#### Pakker og moduler for å bruke pytest

```py
import pytest
```

#### Enkel test med basisfunksjon med assert.

Koden under tester funksjonen `is_prime` ved bruk av `assert`. `assert` er innebygd funksjonalitet i python som brukes til å verifisere om en “betingelse” er sann eller usann. `pytest` vil dersom en `assert` feiler automatisk generere en feilmelding med detaljer om årsaken og verdier som første til feilen.

```py
from pathlib import Path

import pandas as pd
import pytest
from pandas import testing as tm

from pytest_examples.functions import is_prime, valuta_omv

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False
```

### Kodeforklaring

- `is_prime`: Denne funksjonen er definert i `pytest_examples.functions` og sjekker om et gitt tall er et primtall.
- `assert`: Er en innebygd Python-funksjon som tester om en betingelse er sann.

#### Test av funksjon som kaster exception.

Koden under tester funksjonen `is_prime` og “kaster” en `exception` dersom funksjonen får en feil type som input.

```py
from pathlib import Path

import pandas as pd
import pytest
from pandas import testing as tm

from pytest_examples.functions import is_prime, valuta_omv

def test_is_prime():
    with pytest.raises(TypeError) as excinfo:
        is_prime(3.5)
    assert str(excinfo.value) == "Number must be an integer."
```

#### Bruk av fixtures

`pytest` støtter også bruk av fixtures. Fixtures i testrammeverk er mekanismer for å klargjøre og rydde opp i testmiljøet. Fixtures brukes for rigge data og infrastruktur som skal benyttes i testingen.

Her er et enkelt eksempel på hvordan du kan bruke fixtures med `pytest` :

```py
# Filstruktur:
# my_project/
# ├── src/
# │   ├── __init__.py
# │   └── example.py
# ├── tests/
# │   ├── __init__.py
# │   └── conftest.py
# │   └── test_example.py

# src/example.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# tests/test_example.py
import pytest
from src.example import add, subtract

@pytest.fixture
def setup():
    # Setup: print a message or prepare some data
    print("\nSetup: Prepare resources")
    data = {"a": 5, "b": 3}
)

def test_addition(setup_and_teardown):
    data = setup_and_teardown
    result = add(data["a"], data["b"])
    assert result == 8

def test_subtraction(setup_and_teardown):
    data = setup_and_teardown
    result = subtract(data["a"], data["b"])
    assert result == 2

# pytest

```

### Kodeforklaring

- **src/example.py**:

  - Inneholder to enkle funksjoner: `add` og `subtract`.
- **tests/conftest.py**:

  - conftest.py er en fil i `pytest` som brukes til å dele fixtures og annen konfigurasjon på tvers av flere testfiler. Man kan med `conftest.py` definere fixtures i som brukes av alle testfiler i samme katalog og underkataloger.
- **tests/test\_example.py**:

  - Importerer pytest og funksjonene fra `example.py`.
  - Definerer en fixture kalt `setup`:

    - Setup skriver ut en melding og forbereder test-data.
    - To testfunksjoner `test_addition` og `test_subtraction` bruker denne fixturen for å få tilgang til dataene.

Når du kjører `pytest` for dette eksempelet så vil man få en utskrift som viser både setup- og teardown-meldingene for hver test:

```java
$ pytest
============================= test session starts ==============================
...
Setup: Prepare resources
.
Teardown: Clean up resources
Setup: Prepare resources
.
Teardown: Clean up resources
...
============================== 2 passed in Xs ===============================

```

#### Test av pandas dataframe

Koden under tester funksjonen `sum_column`ved bruk av `assert`. `sum_column` summerer kolonner i ett Pandas Dataframe og `test_sum_column` viser at man kan verifisere funksjoner som behandler Pandas Dataframes med `pytest`.

```py
import pandas as pd

def sum_column(dataframe, column_name):
    if column_name not in dataframe.columns:
        raise ValueError(f"Column {column_name} does not exist in the DataFrame")
    return dataframe[column_name].sum()
```

```py
import pytest
import pandas as pd
from your_module import sum_column 

def test_sum_column():
    # Lag en sample DataFrame
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
    }
    df = pd.DataFrame(data)

    # Test at summen av kolonnen 'A' er korrekt
    assert sum_column(df, 'A') == 6

    # Test at summen av kolonnen 'B' er korrekt
    assert sum_column(df, 'B') == 15

    # Test at funksjonen håndterer manglende kolonne riktig
    with pytest.raises(ValueError, match="Column C does not exist in the DataFrame"):
        sum_column(df, 'C')
```

#### Test av pandas dataframe med lesing av fasit fra fil

Koden under viser testing av funksjonen `add_total_column` via funksjonen `test_add_total_column`.

Her er filen med fasit-verdiene som test resultatet skal verifiseres i mot.

```java
# fasit_data.csv
A,B,Total
1,2,3
4,5,9
-1,-1,-2
10,15,25
```

Her er modulen med funksjonen `add_total_column` som skal testes

```py
import pandas as pd

def add_total_column(df):
    df['Total'] = df.sum(axis=1)
    return df
```

Her er modulen med pytest koden som tester funksjonen `add_total_column`

```py
import pytest
import pandas as pd
from my_module import add_total_column

# Funksjon for å lese testdata fra en CSV-fil
def read_csv(file_path):
    return pd.read_csv(file_path)

def test_add_total_column():
    # Les input data
    input_data = pd.DataFrame({
        'A': [1, 4, -1, 10],
        'B': [2, 5, -1, 15]
    })

    # Les forventet resultat fra fil
    expected_result = read_csv('fasit_data.csv')

    # Få faktisk resultat fra funksjonen
    actual_result = add_total_column(input_data)

    # Bruk pandas testing funksjon for å sammenligne DataFrames
    pd.testing.assert_frame_equal(actual_result, expected_result)

```

#### Testing av float-verdier

Testing av flyttall (`float`) kan være utfordrende på grunn av presisjonsproblemer. Små avrundingsfeil kan føre til at direkte sammenligninger feiler. `pytest` tilbyr funksjoner og metoder for å håndtere disse situasjonene. La oss teste funksjonen `add_floats` med `test_add_floats`

```py
def add_floats(a, b):
    return a + b
```

```py
import pytest
from my_module.math_functions import add_floats

def test_add_floats():
    result = add_floats(0.1, 0.2)
    expected = 0.3
    assert pytest.approx(result, rel=1e-9) == expected

```

- `pytest.approx` brukes til å sammenligne flyttall med en spesifisert relativ toleranse.
- `rel=1e-9` spesifiserer at vi aksepterer en relativ forskjell på opp til 1e-9 mellom `result` og `expected`.
