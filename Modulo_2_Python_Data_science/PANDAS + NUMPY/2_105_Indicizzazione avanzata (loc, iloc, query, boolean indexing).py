import pandas as pd

df_prodotti = pd.DataFrame({
    "Prodotto": ["Mouse", "Tastiera", "Monitor", "Libro", "Cuffie", "Borraccia", "SSD", "Lampada", "Webcam", "Router"],
    "Categoria": ["Tecnologia", "Tecnologia", "Tecnologia", "Libri", "Tecnologia", "Casa", "Tecnologia", "Casa", "Tecnologia", "Tecnologia"],
    "Prezzo": [35, 120, 280, 22, 150, 18, 110, 45, 95, 210],
    "Quantità": [10, 5, 2, 12, 4, 20, 6, 7, 8, 3],
    "Disponibilità": [True, True, False, True, True, True, True, False, True, True]
})

# 1) Query: Tecnologia + prezzo tra 100 e 300
filtrati = df_prodotti.query("Categoria == 'Tecnologia' and Prezzo >= 100 and Prezzo <= 300").copy()

# 2) “Vista” con iloc: prime 3 righe, solo Prodotto e Prezzo
vista = filtrati.loc[:, ["Prodotto", "Prezzo"]].iloc[:3]

# 3) Fatturato
filtrati["Fatturato"] = filtrati["Prezzo"] * filtrati["Quantità"]

# 4) Ordina e media fatturato
ordinati = filtrati.sort_values("Fatturato", ascending=False).reset_index(drop=True)
media_fatturato = filtrati["Fatturato"].mean()

print("Vista (prime 3 righe, Prodotto+Prezzo):\n", vista)
print("\nFiltrati con Fatturato:\n", filtrati)
print("\nOrdinati per Fatturato decrescente:\n", ordinati)
print("\nMedia Fatturato (prodotti selezionati):", media_fatturato)
