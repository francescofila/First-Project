# ===============
# ESRCIZIO 2

print("\n ESERCIZIO 1 \n")

import pandas as pd

df_prodotti = pd.DataFrame({
    "prodotto": ["Cavatappi pro", "Decanter", "Bicchiere Zalto", "Taccuino appunti"],
    "prezzo":   [18,             65,         110,              12]
})

mask = df_prodotti["prezzo"] > 50
df_sel = df_prodotti.loc[mask].copy()

df_sel["Costoso"] = df_sel["prezzo"] > 100

df_sel.sort_values("prezzo", ascending=False, inplace=True)

print("Originale:")
print(df_prodotti)
print("\nSelezione lavorabile:")
print(df_sel)

# ===============
# ESRCIZIO 2

print("\n ESERCIZIO 2 \n")

import pandas as pd

df_libri = pd.DataFrame({
    "titolo": ["La caverna", "Solaris", "Il mito moderno del progresso", "Racconti brevi"],
    "autore": ["Saramago",   "Lem",     "Bouveresse",                  "Autore X"],
    "pagine": [336,          224,       420,                           180],
    "prezzo": [14.5,         12.0,      19.9,                          9.0]
})

mask = df_libri["pagine"] > 300
df_big = df_libri.loc[mask].copy()

df_big["Lungo"] = df_big["pagine"] > 400

df_big.sort_values("prezzo", ascending=True, inplace=True)

print("Originale:")
print(df_libri)
print("\nSelezione lavorabile:")
print(df_big)

# ===============
# ESRCIZIO 3

print("\n ESERCIZIO 3 \n")

import pandas as pd

df_clienti = pd.DataFrame({
    "nome": ["Ada", "Bruno", "Chiara", "Dario", "Elena"],
    "città": ["Venezia", "Padova", "Venezia", "Treviso", "Verona"],
    "spesa_totale": [900, 1200, 1750, 1100, 800]
})

mask = df_clienti["spesa_totale"] > 1000
df_top = df_clienti.loc[mask].copy()

df_top["VIP"] = df_top["spesa_totale"] > 1500

df_top.sort_values("spesa_totale", ascending=False, inplace=True)
df_top.reset_index(drop=True, inplace=True)

print("Originale:")
print(df_clienti)
print("\nSelezione lavorabile:")
print(df_top)
