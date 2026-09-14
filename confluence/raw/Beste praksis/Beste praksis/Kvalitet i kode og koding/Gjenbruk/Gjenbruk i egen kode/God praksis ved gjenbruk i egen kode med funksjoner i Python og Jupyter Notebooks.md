
# God praksis ved gjenbruk i egen kode med funksjoner i Python og Jupyter Notebooks

Status: <mark style="background: #baf3db;">I BRUK</mark>

Gjenbruk av kode med funksjoner i Python vil forbedre effektiviteten, vedlikeholdbarheten og lesbarheten til koden. Følgende beskriver “ting å tenke på” vedrørende god praksis for gjenbruk av kode med funksjoner i Python og Jupyter Notebooks:

1. **Oppdeling**:

   - Del opp koden i logisk sammenhengende funksjoner. Hver funksjon bør utføre en bestemt oppgave eller ha et bestemt ansvarsområde. Dette gjør koden enklere å forstå og vedlikeholde.
2. **Bruk beskrivende navn**:

   - Gi funksjonene beskrivende navn som tydelig indikerer hva de gjør. Dette gjør koden mer selvforklarende og hjelper andre med å forstå hensikten til funksjonen.
3. **Gjør funksjoner generiske der det hensiktsmessig**:

   - Lag generiske funksjoner der det er hensiktsmessig. Ikke bruk hardkodede verdier og avhengigheter som begrenser bruken av funksjonen. Dette gjør funksjonen mer gjenbrukbar i ulike kontekster.
4. **Dokumentasjon**:

   - Legg til kommentarer og dokumentasjon i funksjoner for å forklare hvordan de skal brukes, hvilke argumenter de tar imot, og hva de returnerer. Dette hjelper andre utviklere og deg selv med å bruke funksjonene riktig.

```py
def calculate_vat(price, rate):
    """Calculates value-added tax (VAT) based on price and VAT rate.
    
    Args:
        price (float): The price before VAT.
        rate (float): The VAT rate as a decimal (for example, 0.25 for 25%).
    Returns:
        float: The amount of VAT.
    """
    return price * rate
```

5. **Parameterisering**:

   - Tillat funksjoner å være parametriske ved å ta inn argumenter. Dette gjør det mulig å tilpasse funksjonenes atferd ved å endre inndata.
6. **Unngå sideeffekter**:

   - Unngå sideeffekter i funksjoner, dvs. endringer i globale tilstander eller variabler utenfor funksjonens omfang. Dette bidrar til å gjøre funksjoner mer forutsigbare og testbare.
7. **Enhetstesting**:

   - Lag enhetstester for funksjonene dine. Dette sikrer at de fungerer som forventet, og at endringer i koden ikke introduserer feil.
8. **Dekomponering av store oppgaver**:

   - Hvis en funksjon blir for stor eller kompleks, bør du vurdere å dele den opp i mindre funksjoner. Dette bidrar til å forbedre lesbarheten og vedlikeholdbarheten.
9. **Modulorganisering**:

   - Organiser relaterte funksjoner i moduler/filer og pakk dem i kataloger etter behov. Dette gir en strukturert tilnærming til gjenbruk av kode.
10. **Bruk av** `__init__.py`:

    - Hvis du lager en mappe for en pakke med flere moduler, må du inkludere en `__init__.py`-fil i mappen. Dette gjør mappen til en pakke som kan importeres som en enhet.
