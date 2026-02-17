
import numpy as np
import pandas as pd

# =========================
# SEED + DIMENSIONI
# =========================
np.random.seed(42)

N_ORDINI = 100_000
N_PRODOTTI = 20
N_CLIENTI = 5_000

# =========================
# PARTE 1 — CREA DATASET + SALVA FILE
# =========================

# a) prodotti.json (20 prodotti)

prodotti = pd.DataFrame({
    "ProdottoID": np.arange(1, N_PRODOTTI +1), 
    "Categoria": np.random.choice(["A", "B", "C", "D"], size = N_PRODOTTI),
    "Fornitore": np.random.choice(
        ["NordSupply", "LagunaTrade", "AdriaticHub", "TerraBit", "VineOps"],
        size = N_PRODOTTI
    ),
    "PrezzoUnitario": np.random.uniform(5, 250, size=N_PRODOTTI)
})

prodotti.to_json("prodotti.json", orient="records")

# b) clienti.csv (5000 clienti)

clienti = pd.DataFrame({
    "ClienteID": np.arange(1, N_CLIENTI + 1),
    "Regione": np.random.choice(["Nord", "Centro", "Sud", "Isole"], size=N_CLIENTI, p=[0.35, 0.25, 0.28, 0.12]),
    "Segmento": np.random.choice(["Premium", "Standard"], size = N_CLIENTI, p=[0.22, 0.78])
})

clienti.to_csv("clienti.csv", index=False)

# c) ordini.csv (100000 righe)
date = pd.date_range("2025-01-01", "2025-12-31", freq="D")

ordini = pd.DataFrame({
    "ClienteID": np.random.randint(1, N_CLIENTI + 1, size = N_ORDINI),
    "ProdottoID": np.random.randint(1, N_PRODOTTI + 1, size = N_ORDINI),
    "Quantità": np.random.randint(1, 6, size = N_ORDINI),
    "DataOrdine": np.random.choice(date, size = N_ORDINI)
})
ordini.to_csv("ordini.csv", index=False)


# ====
# PARTE 2 — CARICA + UNISCI
# ====
df_ordini = pd.read_csv("ordini.csv", parse_dates=["DataOrdine"])
df_prodotti = pd.read_json("prodotti.json")
df_clienti = pd.read_csv("clienti.csv")

df = (
    df_ordini
    .merge(df_prodotti, on="ProdottoID", how="left")
    .merge(df_clienti, on="ClienteID", how="left")
)


# ====
# PARTE 3 — OTTIMIZZAZIONE
# ====
mem_pre = df.memory_usage(deep=True).sum()

df["Categoria"] = df["Categoria"].astype("category")
df["Fornitore"] = df["Fornitore"].astype("category")
df["Regione"] = df["Regione"].astype("category")
df["Segmento"] = df["Segmento"].astype("category")

df["Quantità"] = pd.to_numeric(df["Quantità"], downcast="integer")
df["ClienteID"] = pd.to_numeric(df["ClienteID"], downcast="integer")
df["ProdottoID"] = pd.to_numeric(df["ProdottoID"], downcast="integer")
df["PrezzoUnitario"] = pd.to_numeric(df["PrezzoUnitario"], downcast="float")

mem_post = df.memory_usage(deep=True).sum()

# ====
# PARTE 4 — COLONNA + FILTRI
# ====
df["ValoreTotale"] = df["PrezzoUnitario"] * df["Quantità"]

df_filtrato = df.query("ValoreTotale > 100 and Segmento == 'Premium'").copy()

# CHECK FINALE 

print("df shape:", df.shape)
print("df_filtrato shape:", df_filtrato.shape)
print(f"Memoria pre : {mem_pre/1024/1024:.2f} MB")
print(f"Memoria post: {mem_post/1024/1024:.2f} MB")

print("\nPrime 5 righe filtrate:")
print(df_filtrato.head())