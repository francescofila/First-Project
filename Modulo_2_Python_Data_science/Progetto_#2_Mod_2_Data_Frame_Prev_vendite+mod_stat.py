"""
Esercizi pratici Pandas — Creazione e gestione DataFrame (riassunto)

Scenario: pipeline "vendite" con dataset finti:
- prodotti (JSON)
- clienti (CSV)
- ordini (CSV)

Obiettivi:
1) I/O + merge + ottimizzazione dtypes + query subset
2) MultiIndex + groupby gerarchico con NamedAgg
3) Concat mensile + metriche per cliente
4) Lettura a chunk e aggregazione streaming
5) Export Parquet (con fallback) + metriche per categoria
"""


import pandas as pd
import numpy as np


# ==== 
# Setup riproducibile
# ====
np.random.seed(42)

# ==== 
# Esercizio 1
# creazione dataset, salvataggio, lettura, merge, dtypes, colonna calcolata, subset
# ====

# --- Dataset prodotti (JSON) ---

prodotti = pd.DataFrame({
    "ProdottoID": np.arange(1, 11), 
    "Categoria": np.random.choice(["A", "B", "C"], 10), 
    "PrezzoUnitario": np.random.random(10) * 100
})
prodotti.to_json("prodotti.json", orient="records")

# --- Dataset clienti (CSV) ---
clienti = pd.DataFrame({
    "ClienteID": np.arange(1,21),
    "Nome": [f"Cliente_{i}" for i in range(1,21)],
    "Segmento": np.random.choice(["Premium", "Standard"], 20)
})

clienti.to_csv("clienti.csv", index=False)

# --- Dataset ordini (CSV) ---
ordini = pd.DataFrame({
    "OrdineID": np.arange(1,51),
    "ClienteID": np.random.randint(1, 21, 50),
    "ProdottoID": np.random.randint(1, 11, 50),
    "Quantità": np.random.randint(1, 5, 50)
})

ordini.to_csv("ordini.csv", index=False)

# --- Lettura file ---
df_prodotti = pd.read_json("prodotti.json")
df_clienti = pd.read_csv("clienti.csv")
df_ordini = pd.read_csv("ordini.csv")

# --- Merge ordini + prodotti + clienti ---
df_base = (
    df_ordini
    .merge(df_prodotti, on="ProdottoID", how="left")
    .merge(df_clienti, on="ClienteID", how="left")
)

# --- Ottimizzazione tipi (memory-friendly) ---
df_base["Categoria"] = df_base["Categoria"].astype("category")
df_base["Segmento"]= df_base["Segmento"].astype("category")
df_base["Quantità"] = df_base["Quantità"].astype("int16")

# Downcast float per risparmio memoria
df_base["PrezzoUnitario"] = pd.to_numeric(df_base["PrezzoUnitario"], downcast="float")

# --- Creazione colonna valore totale ---
df_base["ValoreTotale"] = (df_base["PrezzoUnitario"] * df_base["Quantità"]).astype("float32")

# --- Subset: clienti Premium con valore alto ---
subset = df_base.query("Segmento == 'Premium' and ValoreTotale > 50").copy()

print("=== \n Esercizio 1 : Subset Premium con valore > 50 ===\n")
print(subset.head(10))


# ====
# ESERCIZIO 2
# MultiIndex + aggregazioni gerarchiche
# ====

# Sul df principale creiamo una vista dedicata per MultiIndex [no inplace]

df_mi = df_base.set_index(["Categoria", "ClienteID"])

report = df_mi.groupby(level=["Categoria", "ClienteID"]).agg(
    totale_vendite = pd.NamedAgg(column="ValoreTotale", aggfunc="sum"), 
    media_quantità = pd.NamedAgg(column="Quantità", aggfunc="mean"), 
    numero_ordini = pd.NamedAgg(column="OrdineID", aggfunc="count"),
)

report= report.reset_index()

print("\n=== ES2: Report per (Categoria, ClienteID) ===")
print(report.head(10))

# ====
# ESERCIZIO 3
# Simulazione ordini mensili + concatenazione + metriche per cliente
# ====

ordini_gen = df_base.sample(10, random_state=1).reset_index(drop=True)
ordini_feb = df_base.sample(8, random_state=2).reset_index(drop=True)
ordini_mar = df_base.sample(12, random_state=3).reset_index(drop=True)

# Aggiungiamo una colonna "Mese"

ordini_gen["Mese"] = "Gen"
ordini_feb["Mese"] = "Feb"
ordini_mar["Mese"] = "Mar"

# Concatenazione verticale (mesi diversi)
ordini_totali = pd.concat([ordini_gen, ordini_feb, ordini_mar], ignore_index=True)


ordini_totali = ordini_totali.drop(columns=["Nome", "Segmento"], errors="ignore")
ordini_totali = ordini_totali.merge(df_clienti, on="ClienteID", how="left")

metrics = ordini_totali.groupby("ClienteID").agg(
    spend_totale=pd.NamedAgg(column="ValoreTotale", aggfunc="sum"),
    ordini_totali=pd.NamedAgg(column="OrdineID", aggfunc="count"),
)

print("\n=== ES3: Metriche per ClienteID (3 mesi concatenati) ===\n")
print(metrics.head(10))


# ====
# ESERCIZIO 4
# Lettura a chunk (streaming) e calcolo valore totale ordini
# ====


totale_valore = 0.0

# Ottimizzazione: leggiamo solo le colonne necessarie
usecols = ["OrdineID", "ClienteID", "ProdottoID", "Quantità"]

for chunk in pd.read_csv("ordini.csv", chunksize=10, usecols=usecols):
    # Merge solo con le colonne essenziali dei prodotti
    chunk = chunk.merge(df_prodotti[["ProdottoID", "PrezzoUnitario"]], on="ProdottoID", how="left")

    # Calcolo metrica e accumulo (streaming)
    chunk["ValoreTotale"] = chunk["PrezzoUnitario"] * chunk["Quantità"]
    totale_valore += float(chunk["ValoreTotale"].sum())

print("\n=== ES4: Valore totale ordini (chunked) ===")
print("Valore totale ordini:", totale_valore)


# ====
# ESERCIZIO 5
# Subset Premium + export Parquet + aggregazioni per categoria
# ====

# Creazione subset clienti Premium ad alto valore
premium_subset = df_base.query("Segmento == 'Premium' and ValoreTotale > 50").copy()

premium_subset.to_parquet("premium_subset.parquet", index=False)
print("\n=== ES5: Salvato premium_subset.parquet ===\n")

# Aggregazioni per Categoria

categoria_metrics = df_base.groupby("Categoria").agg(
    totale_vendite=("ValoreTotale", "sum"),
    ordini=("OrdineID", "count"),
    media_quantità=("Quantità", "mean"),
).reset_index()

print("\n=== ES5: Metriche per Categoria ===\n")
print(categoria_metrics)