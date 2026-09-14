
# Eksempel på commit-melding

Status: <mark style="background: #baf3db;">I BRUK</mark>

Her er noen tips til hvordan skrive gode commit-meldinger: <https://cbea.ms/git-commit/>  
Hvis du inkuderer Jira-saksnummeret (eks. `PF-321`) i commit-meldingen, vil en lenke til committen vises i Jira-saken.

Her er et eksempel fra et av repoene til folkeregisteret i SSB:

```java
PF-321: Add function for flattening pandas dataframes

- When nested BigQuery tables are converted to pandas, the
  nesting is stored as a dictionary in the base column.
  The new function extracts and flattens a given list
  of column names.
```

På GitHub ser committen [slik ut](https://github.com/statisticsnorway/sfreg/commit/1323855d448ebfe644a268403ec3868e6f48b396).
