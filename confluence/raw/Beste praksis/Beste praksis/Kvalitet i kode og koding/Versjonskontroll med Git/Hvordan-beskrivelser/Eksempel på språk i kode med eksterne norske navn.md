---
tags:
  - kb-how-to-article
---

# Eksempel på språk i kode med eksterne norske navn

Status: <mark style="background: #baf3db;">I BRUK</mark>

> [!IMPORTANT]
> [Regler og anbefalinger fra KVAKK](../../Regler%20og%20anbefalinger%20fra%20KVAKK.md) sier “Skriv kildekode, api-dokumentasjon og commit-meldinger på engelsk.”, men med unntak for “ikke oversett elementer til engelsk der hvor det er brukt norsk språk på for eksempel navn på kolonner i databaser, felter i eksterne API’er osv.” Her er et eksempel på hvordan kildekode med slike unntak kan se ut.

## Eksempel fra folkeregisteret (FREG)

FREG henter kildedataene sine fra et grensesnitt (API) hos Skatteetaten. I dette api’et brukes navn på felter som “folkeregisteridentifikator”, “grunnkrets” og “gyldighetstidspunkt”. Disse begrepene oversettes ikke til engelsk, men brukes som de er når man legger dem inn i en dataframe og spør videre på dem. Men funksjonsnavn og andre variable skrives på engelsk. Bruk sunn fornuft. Eksempel:

```py
def join_status_at_birth(df, df_status):
    """
    Join the child's status at birth. Assume that the first given
    status is the valid status at birth. Then only keep records with
    status as either 'foedselsregistrert' or 'bosatt'. Last, join this
    along with the births dataframe (df).

    - Adds column "status" to df
    - Note that the number of rows in df can decrease.
    """

    # Add sortby ajourholdstidspunkt for stable sorting
    window = Window.partitionBy("folkeregisteridentifikator").orderBy(
        F.col("gyldighetstidspunkt").asc_nulls_last(),
        F.col("ajourholdstidspunkt").asc_nulls_last(),
    )

    # Choose oldest status record per person and filter on status
    df_status = (
        df_status.withColumn("row", F.row_number().over(window))
        .filter(
            (F.col("row") == 1)
            & (F.col("status").isin(["foedselsregistrert", "bosatt"]))
        )
        .select(["folkeregisteridentifikator", "status"])
    )

    # Join status to births dataframe (df)
    df = df.join(df_status, on="folkeregisteridentifikator", how="inner")

    return df
```
