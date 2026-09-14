
# Kodeeksempler på gjenbruk med Python

Status: <mark style="background: #baf3db;">I BRUK</mark>

Repoet [tech-coach-importtest](https://github.com/statisticsnorway/tech-coach-importtest) illustrerer god praksis for gjenbruk av egen kode med funksjoner og moduler i Python og Jupyter Notebooks. Koden viser:

- Bruk av funksjoner i egen kode.
- Bruk av moduler i egen kode.

  - I Python er en modul en fil som inneholder Python-kode.
- Organisering av moduler i pakker.

  - I Python er en pakke en mappe (på filsystemet) som inneholder en eller flere Python-moduler.
- Import av moduler fra hierarki.

### Beskrivelse av tech-coach-importtest.

Kildekoden til tech-coach-importtest er organisert i følgende struktur.

```java
.
├── tech-coach-importtest
│   ├── package1
│   │   ├── __init__.py
│   │   ├── module1.py
│   │   ├── module1.ipynb
│   │   ├── module2.py
│   │   └── module2.ipynb
│   └── package2
│       ├── subpackage1
│       │   ├── module5.ipynb
│       │   └── module5.py
│       ├── __init__.py
│       ├── module3.py
│       └── module4.py
├── __init__.py
├── main.ipynb
└── main.py
```

1. **tech-coach-importtest:** Er prosjektets rotmappe.

   - **package1:** En Python-pakke som inneholder moduler og en underpakke.

     - `__init__.py`: En tom fil som markerer mappen som en Python-pakke.
     - `module1.py` og `module2.py`: Python-moduler i pakken.
     - `module1.ipynb` og `module2.ipynb`: Jupyter Notebook-filer relatert til modulene.
   - **package2:** En annen Python-pakke som inneholder moduler og en underpakke.

     - **subpackage1:** En underpakke av `package2`.

       - `module5.py` og `module5.ipynb`: Python-modul og Jupyter Notebook relatert til denne underpakken.
     - `__init__.py`: En tom fil som markerer mappen som en Python-pakke.
     - `module3.py` og `module4.py`: Python-moduler i pakken.
2. **init.py:** En tom fil som markerer rotdirektivet som en Python-pakke.
3. **main.ipynb:** En Jupyter Notebook-fil.
4. [**main.py**](https://github.com/statisticsnorway/tech-coach-importtest/blob/main/main.py)**:** En Python-skriptfil.

> [!IMPORTANT]
> Merk: Jupyter Notebook filen main.ipynb gjør import og funksjonskall akkurat på samme måte som i main.py så dokumentasjonen for main.py gjelder også for main.ipynb

### Beskrivelse av module5.py

[module5.py](https://github.com/statisticsnorway/tech-coach-importtest/blob/main/package2/subpackage1/module5.py) illustrerer gjenbruk av funksjoner (pluss, minus, gange, dele) fra moduler spredt rundt i prosjektets trestruktur. Import utrykkene viser både absolutt og relativ import.

### Beskrivelse av module5.ipynb

[module5.ipynb](https://github.com/statisticsnorway/tech-coach-importtest/blob/main/package2/subpackage1/module5.ipynb) illustrerer gjenbruk av funksjoner (pluss, minus, gange, dele) fra moduler spredt rundt i prosjektets trestruktur. **Merk**: For at relative imports skal fungere, må modulene være en del av en pakke, og prosjektstrukturen må være riktig “konfigurert”. I Jupyter Notebooks så kan/vil importsystemet “oppføre” seg annerledes en i “standard Python”. For å “gardere” for dette så brukes funksjonaliteten “`ProjectRoot`" fra “hjelpe-pakken” `fagfunksjoner.paths.project_root` i module5.ipynb.
