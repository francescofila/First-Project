import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)


df = pd.DataFrame({
    "Category" : rng.choice(list("ABCD"), size=120),
    "Users" : rng.integers(20, 1000, size=120),
    "Transaction" : rng.integers(1, 300, size=120)
})

codes = df["Category"].astype("category").cat.codes

fig, ax, = plt.subplots(figsize=(9, 6))
sc = ax.scatter(df["Users"], df["Transaction"], 
                c = codes, 
                s=df["Transaction"],
                cmap="viridis",
                alpha=0.7)

ax.set_title("Utenti vs Transazioni (colore=categoria, size=transazioni)")
ax.set_xlabel("Utenti")
ax.set_ylabel("transazioni")
ax.grid(True, alpha=0.4)

cbar = fig.colorbar(sc, ax=ax)
cbar.set_ticks(range(df["Category"].nunique()))
cbar.set_ticklabels(df["Category"].astype("category").cat.categories)

plt.show()