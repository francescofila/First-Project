import pandas as pd
import numpy as np

np.random.seed(123)

regioni = ["Nord", "Centro"]
citta = ["Milano", "Roma"]
prodotti = ["Libro", "Vino", "Taccuino"]
mesi = ["Gen", "Feb", "Mar"]

idx = pd.MultiIndex.from_product(
    [regioni, citta, prodotti, mesi],
    names=["Regione", "Citta", "Prodotto", "Mese"]
)

df = pd.DataFrame({"Vendite": np.random.randint(10, 101, size=len(idx))}, index=idx)

print("=== Solo Regione Nord ===")
nord = df.loc["Nord"]  # rimuove il livello Regione dall'index risultante
print(nord.head(10))

print("\n=== Somma vendite per Mese (solo Nord) ===")
somma_mese = nord.groupby(level="Mese")["Vendite"].sum()
print(somma_mese)

print("\n=== Ordina indice per Prodotto (solo Nord) ===")
# metto Prodotto come primo livello per ordinare “primariamente” per prodotto
ordinato = nord.swaplevel("Citta", "Prodotto").sort_index()
print(ordinato.head(10))

print("\n=== Riporta due livelli a colonna (Prodotto, Mese) ===")
flat2 = nord.reset_index(["Prodotto", "Mese"])
print(flat2.head(10))

print("\n=== Prodotto più venduto in ogni Citta (solo Nord) ===")
# 1) sommo per Citta+Prodotto
tot_cp = nord.groupby(level=["Citta", "Prodotto"])["Vendite"].sum()

# 2) per ogni città, prendo il prodotto con totale massimo
best = tot_cp.groupby(level="Citta").idxmax()   # restituisce (Citta, Prodotto)
best_prodotti = best.apply(lambda x: x[1])      # estraggo solo il prodotto

print(best_prodotti)
