import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

np.random.seed(42)

consumo = np.random.normal(loc=300, scale=80, size=1000)

consumo = np.append (consumo, [5, 2000, 50000])

df = pd.DataFrame({
    "consumo_W": consumo
})

# Pulizia outlier con regola "plausibile" (50W–1000W)
df_clean = df[(df["consumo_W"] >= 50) & (df["consumo_W"] <= 1000)].copy()


# Controllo cosa è stato rimosso

df_out = df.loc[~df.index.isin(df_clean.index), ["consumo_W"]]
print("Righe totali:", len(df))
print("Righe dopo pulizia:", len(df_clean))
print("Outlier rimossi:", len(df_out))
print(df_out)

# 3) Istogramma in scala lineare (facoltativo ma utile per confronto)
fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(df_clean["consumo_W"], bins=20, edgecolor="black")
ax.set_title("Consumo energetico — scala lineare")
ax.set_xlabel("Consumo (W)")
ax.set_ylabel("Frequenza")
ax.xaxis.set_major_locator(mticker.MultipleLocator(100))  # ticks ogni 100 W
ax.grid(True, axis="y", linestyle="--", linewidth=0.6)
plt.tight_layout()
plt.show()


# 4) Istogramma con asse Y in scala log (richiesto)
fig, ax = plt.subplots(figsize=(10, 4))
counts, bins, _ = ax.hist(df_clean["consumo_W"], bins=20, edgecolor="black")

ax.set_yscale("log")

# Su scala log non puoi mostrare y=0: imposto minimo a 1
ax.set_ylim(1, max(counts) * 1.2)

ax.set_title("Consumo energetico — asse Y in scala log")
ax.set_xlabel("Consumo (W)")
ax.set_ylabel("Frequenza (log)")

ax.xaxis.set_major_locator(mticker.MultipleLocator(100))  # ticks ogni 100 W
ax.grid(True, which="both", axis="y", linestyle="--", linewidth=0.6)  # major+minor
plt.tight_layout()
plt.show()

# 5) Analisi
print("\nAnalisi:")
print(
    "In scala lineare le barre centrali (frequenti) dominano e le code sembrano sparire.\n"
    "Con la scala log sull'asse Y, le frequenze piccole vengono 'amplificate' visivamente,\n"
    "quindi le code della distribuzione (consumi rari) diventano leggibili."
)