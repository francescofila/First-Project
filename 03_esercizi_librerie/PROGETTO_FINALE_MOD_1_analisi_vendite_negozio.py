"""
Progetto finale - Analisi di Vendite in una Catena di Negozi
Tecnologie: NumPy, Pandas, Matplotlib
Output: vendite.csv (se non esiste), vendite_analizzate.csv
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "vendite.csv"
OUT_ANALYZED = "vendite_analizzate.csv"


def file_esiste(nome_file):
    """Ritorna True se il file esiste, False altrimenti (senza usare os)."""
    try:
        with open(nome_file, "r", encoding="utf-8"):
            return True
    except FileNotFoundError:
        return False


def crea_dataset_base(nome_csv, seed=42):
    """
    Crea un dataset di base (>= 30 righe) e lo salva in CSV.
    Random "base": np.random.seed + choice + randint.
    """
    np.random.seed(seed)

    date = pd.date_range("2023-09-01", periods=10, freq="D")  # 10 giorni
    negozi = ["Milano", "Roma", "Napoli"]  # 3 negozi -> 30 righe

    prodotti = ["Smartphone", "Laptop", "TV", "Cuffie", "Console", "Tablet"]
    prezzi = {
        "Smartphone": 499.99,
        "Laptop": 1099.00,
        "TV": 799.00,
        "Cuffie": 149.90,
        "Console": 399.00,
        "Tablet": 349.00,
    }

    righe = []
    for d in date:
        for n in negozi:
            p = np.random.choice(prodotti)
            q = int(np.random.randint(1, 13))  # quantità 1..12
            righe.append(
                {
                    "Data": d.strftime("%Y-%m-%d"),
                    "Negozio": n,
                    "Prodotto": p,
                    "Quantità": q,
                    "Prezzo_unitario": float(prezzi[p]),
                }
            )

    df_base = pd.DataFrame(righe)
    df_base.to_csv(nome_csv, index=False, encoding="utf-8")


def top_n_prodotti(df, n):
    """
    Restituisce i n prodotti più venduti in termini di INCASSO TOTALE.
    Richiede che la colonna 'Incasso' esista già.
    """
    return (
        df.groupby("Prodotto", as_index=False)["Incasso"]
        .sum()
        .sort_values("Incasso", ascending=False)
        .head(n)
    )


# ----------------------------
# Parte 1 - Dataset di base
# ----------------------------
if not file_esiste(DATA_FILE):
    crea_dataset_base(DATA_FILE)

# ----------------------------
# Parte 2 - Importazione con Pandas
# ----------------------------
df = pd.read_csv(DATA_FILE)
df["Data"] = pd.to_datetime(df["Data"])  # conversione esplicita

print("\n=== PRIME 5 RIGHE (head) ===")
print(df.head())

print("\n=== SHAPE (righe, colonne) ===")
print(df.shape)

print("\n=== INFO ===")
df.info()

# ----------------------------
# Parte 3 - Elaborazioni con Pandas
# ----------------------------
df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"]

incasso_totale = df["Incasso"].sum()
incasso_medio_negozio = df.groupby("Negozio")["Incasso"].mean()

prodotti_piu_venduti_qta = (
    df.groupby("Prodotto")["Quantità"].sum().sort_values(ascending=False).head(3)
)

incasso_medio_negozio_prodotto = df.groupby(["Negozio", "Prodotto"])["Incasso"].mean()

print("\n=== INCASSO TOTALE CATENA ===")
print(round(incasso_totale, 2))

print("\n=== INCASSO MEDIO PER NEGOZIO ===")
print(incasso_medio_negozio.round(2))

print("\n=== TOP 3 PRODOTTI PER QUANTITÀ TOTALE ===")
print(prodotti_piu_venduti_qta)

print("\n=== INCASSO MEDIO PER (NEGOZIO, PRODOTTO) ===")
print(incasso_medio_negozio_prodotto.round(2))

# ----------------------------
# Parte 4 - Uso di NumPy
# ----------------------------
q = df["Quantità"].to_numpy()

media_q = np.mean(q)
min_q = np.min(q)
max_q = np.max(q)
std_q = np.std(q)

percento_sopra_media = (np.sum(q > media_q) / q.size) * 100

print("\n=== NUMPY: STATISTICHE QUANTITÀ ===")
print(f"media={media_q:.2f}  min={min_q}  max={max_q}  std={std_q:.2f}")
print(f"% vendite sopra la media: {percento_sopra_media:.2f}%")

arr2d = df[["Quantità", "Prezzo_unitario"]].to_numpy()
incasso_np = arr2d[:, 0] * arr2d[:, 1]

coerente = np.allclose(incasso_np, df["Incasso"].to_numpy())
print("\n=== VERIFICA INCASSO (NumPy vs Pandas) ===")
print("Coerente:", coerente)

# ----------------------------
# Parte 5 - Visualizzazioni con Matplotlib
# ----------------------------
# 1) Barre: incasso totale per negozio
incasso_per_negozio = df.groupby("Negozio")["Incasso"].sum()

plt.figure()
plt.bar(incasso_per_negozio.index, incasso_per_negozio.values)
plt.title("Incasso totale per negozio")
plt.xlabel("Negozio")
plt.ylabel("Incasso totale (€)")
plt.tight_layout()
plt.show()

# 2) Torta: percentuale incassi per prodotto
incasso_per_prodotto = df.groupby("Prodotto")["Incasso"].sum()

plt.figure()
plt.pie(incasso_per_prodotto.values, labels=incasso_per_prodotto.index, autopct="%1.1f%%")
plt.title("Percentuale incassi per prodotto")
plt.tight_layout()
plt.show()

# 3) Linee: andamento giornaliero incassi totali
incasso_giornaliero = df.groupby("Data")["Incasso"].sum().sort_index()

plt.figure()
plt.plot(incasso_giornaliero.index, incasso_giornaliero.values, marker="o")
plt.title("Andamento giornaliero degli incassi totali della catena")
plt.xlabel("Data")
plt.ylabel("Incasso totale (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# Parte 6 - Analisi Avanzata
# ----------------------------
mappa_categoria = {
    "Smartphone": "Informatica",
    "Laptop": "Informatica",
    "Tablet": "Informatica",
    "TV": "Elettrodomestici",
    "Cuffie": "Audio",
    "Console": "Gaming",
}

df["Categoria"] = df["Prodotto"].map(mappa_categoria)

incasso_tot_cat = df.groupby("Categoria")["Incasso"].sum()
qta_media_cat = df.groupby("Categoria")["Quantità"].mean()

print("\n=== INCASSO TOTALE PER CATEGORIA ===")
print(incasso_tot_cat.round(2))

print("\n=== QUANTITÀ MEDIA VENDUTA PER CATEGORIA ===")
print(qta_media_cat.round(2))

df.to_csv(OUT_ANALYZED, index=False, encoding="utf-8")
print(f"\nSalvato: {OUT_ANALYZED}")

# ----------------------------
# Parte 7 - Estensioni
# ----------------------------
incasso_medio_cat = df.groupby("Categoria")["Incasso"].mean().sort_index()
qta_media_cat2 = df.groupby("Categoria")["Quantità"].mean().sort_index()

fig, ax1 = plt.subplots()
ax1.bar(incasso_medio_cat.index, incasso_medio_cat.values, color="steelblue")
ax1.set_title("Incasso medio (barre) + linea quantità media venduta")
ax1.set_xlabel("Categoria")
ax1.set_ylabel("Incasso medio (€)")

ax2 = ax1.twinx()
ax2.plot(qta_media_cat2.index, qta_media_cat2.values, marker="o", color="darkorange")
ax2.set_ylabel("Quantità media venduta")

fig.tight_layout()
plt.show()

print("\n=== TOP N PRODOTTI PER INCASSO (funzione) ===")
print(top_n_prodotti(df, 3).round(2))
