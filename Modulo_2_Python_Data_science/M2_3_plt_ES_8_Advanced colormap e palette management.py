"""
Esercizio 1: Heatmap 10x10 con diverging colormap e centro a 0.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

rng = np.random.default_rng(42)

data = rng.normal(loc=0, scale=1, size=(10, 10))

# Stampa leggibile
np.set_printoptions(precision=3, suppress=True, linewidth=140)
print("Matrice (numpy):")
print(data)

df = pd.DataFrame(data, index=[f"R{i}" for i in range(10)], columns=[f"C{i}" for i in range(10)])
print("\nMatrice (DataFrame):")
print(df.to_string())

print("\nmin:", data.min(), "max:", data.max())

norm = TwoSlopeNorm(vmin=data.min(), vcenter=0, vmax=data.max())

fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(data, cmap="coolwarm", norm=norm)
cbar = fig.colorbar(im, ax=ax)
cbar.set_label("Valore (neg ↔ pos)")

ax.set_title("Heatmap diverging (centro = 0)")
ax.set_xlabel("Colonna")
ax.set_ylabel("Riga")
plt.show()


"""
Esercizio 2: LogNorm su dati 1..10000 con colormap continua.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Creo una matrice con valori su 4 ordini di grandezza
data = np.logspace(0, 4, num=100).reshape(10, 10)  # da 10^0 a 10^4

fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(data, cmap="viridis", norm=LogNorm(vmin=1, vmax=10000))

cbar = fig.colorbar(im, ax=ax)
cbar.set_label("Intensità (scala log)")
cbar.set_ticks([1, 10, 100, 1000, 10000])
cbar.set_ticklabels(["1", "10", "100", "1k", "10k"])

ax.set_title("Heatmap con LogNorm (1 → 10000)")
plt.show()


"""
Esercizio 3: Heatmap discreta (6 categorie) + colorbar con etichette testuali.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

rng = np.random.default_rng(7)
data = rng.integers(0, 6, size=(10, 10))  # 6 categorie: 0..5

categorie = ["Pane", "Vino", "Formaggi", "Verdure", "Dolci", "Spezie"]

cmap = ListedColormap([
    "tab:brown", "tab:purple", "gold", "tab:green", "tab:orange", "tab:red"
])

fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(data, cmap=cmap, vmin=-0.5, vmax=5.5)

cbar = fig.colorbar(im, ax=ax, ticks=range(6))
cbar.set_label("Categoria prodotto")
cbar.set_ticklabels(categorie)

ax.set_title("Heatmap discreta — 6 categorie")
plt.show()


"""
Esercizio 4: Temperature — inversione colormap + shifting del centro con TwoSlopeNorm.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

rng = np.random.default_rng(123)

# Temperature plausibili (°C): base 18, variazioni +/- 8
temp = 18 + rng.normal(0, 4, size=(12, 12))
temp = np.clip(temp, 5, 30)

# 1) Inversione: stessa informazione, “verso” cromatico invertito
fig, ax = plt.subplots(figsize=(6, 5))
im1 = ax.imshow(temp, cmap="Spectral_r")  # inversione con _r
cbar1 = fig.colorbar(im1, ax=ax)
cbar1.set_label("Temperatura [°C]")
ax.set_title("Temperature — colormap invertita (Spectral_r)")
plt.show()

# 2) Shifting del centro: evidenzio sotto/sopra una soglia (es. 15°C)
soglia = 15
norm = TwoSlopeNorm(vmin=temp.min(), vcenter=soglia, vmax=temp.max())

fig, ax = plt.subplots(figsize=(6, 5))
im2 = ax.imshow(temp, cmap="coolwarm", norm=norm)
cbar2 = fig.colorbar(im2, ax=ax)
cbar2.set_label("Temperatura [°C] (centro = 15°C)")
ax.set_title("Temperature — diverging con centro spostato a 15°C")
plt.show()