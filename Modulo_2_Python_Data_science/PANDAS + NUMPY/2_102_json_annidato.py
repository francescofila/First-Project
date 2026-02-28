import pandas as pd

dati = [
    {
        "store": "Negozio_A",
        "city": "Venezia",
        "products": [
            {"product": "Etichetta_1", "weekly_sales": [10, 12, 9, 11]},
            {"product": "Etichetta_2", "weekly_sales": [5, 7, 6, 8]},
            {"product": "Etichetta_3", "weekly_sales": [2, 3, 4, 3]},
        ],
    },
    {
        "store": "Negozio_B",
        "city": "Padova",
        "products": [
            {"product": "Etichetta_1", "weekly_sales": [8, 9, 10, 7]},
            {"product": "Etichetta_2", "weekly_sales": [6, 6, 5, 7]},
            {"product": "Etichetta_3", "weekly_sales": [1, 2, 2, 1]},
        ],
    },
    {
        "store": "Negozio_C",
        "city": "Verona",
        "products": [
            {"product": "Etichetta_1", "weekly_sales": [13, 11, 12, 14]},
            {"product": "Etichetta_2", "weekly_sales": [4, 5, 4, 6]},
            {"product": "Etichetta_3", "weekly_sales": [3, 3, 2, 4]},
        ],
    },
]

# 1) Normalizzazione: una riga per prodotto, con weekly_sales come lista

df_prod = pd.json_normalize(
    dati, 
    record_path=["products"],
    meta= ["store", "city"]
)

print(df_prod)

# 2) Long format: una riga per settimana

df_long = df_prod.explode("weekly_sales").reset_index(drop=True)
df_long["weekly_sales"] = pd.to_numeric(df_long["weekly_sales"], errors="coerce")

print("\n", df_long, "\n")


print(df_long["weekly_sales"])




# 3) Totali per negozio e prodotto

totali_store_prod = (
    df_long.groupby(["store", "product"], as_index=False)["weekly_sales"]
    .sum()
    .rename(columns={"weekly_sales": "total_sales"})
)

print(totali_store_prod)

# 4) Media settimanale per prodotto (su tutti i negozi e settimane)

media_weekly_prod = (
    df_long.groupby(["product"], as_index=False)["weekly_sales"]
    .mean()
    .rename(columns={"weekly_sales": "avg_weekly_sales"})
)

print("\n", media_weekly_prod, "\n")