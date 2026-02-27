"""
Esercizio 1: 5M punti, memoria e visualizzazione scalabile.

Strategia:
- Genero 5M punti
- Confronto RAM float64 vs float32
- Visualizzo con:
  (1) scatter campionato
  (2) densità via histogram2d (molto più scalabile)
"""

import numpy as np
import matplotlib.pyplot as plt


def mb(n_bytes: int) -> float:
    """Bytes -> MB."""
    return n_bytes / (1024**2)


n = 5_000_000

# 1) float64 (default)
x64 = np.random.rand(n)
y64 = np.random.rand(n)
print(f"float64 totale: {mb(x64.nbytes + y64.nbytes):.2f} MB")

# 2) float32
x = x64.astype(np.float32)
y = y64.astype(np.float32)
print(f"float32 totale: {mb(x.nbytes + y.nbytes):.2f} MB")

# Libero le versioni float64 (se non servono)
del x64, y64

# (A) Scatter campionato
sample_size = 60_000
idx = np.random.choice(n, size=sample_size, replace=False)

plt.figure(figsize=(9, 5))
plt.scatter(x[idx], y[idx], s=2, alpha=0.35, rasterized=True)
plt.title("Scatter campionato (5M -> 60k)")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("ex1_scatter_sample.png", dpi=150, bbox_inches="tight")
plt.show()

# (B) Binning 2D (densità)
bins = 350
H, xedges, yedges = np.histogram2d(x, y, bins=bins)

# Per evidenziare le code: scala log (evito log(0))
H_log = np.log1p(H)

plt.figure(figsize=(9, 5))
plt.imshow(
    H_log.T,
    origin="lower",
    aspect="auto"
)
plt.title("Densità (hist2d) in scala log1p")
plt.xlabel("bin x")
plt.ylabel("bin y")
plt.colorbar(label="log1p(conteggi)")
plt.tight_layout()
plt.savefig("ex1_hist2d_log.png", dpi=150, bbox_inches="tight")
plt.show()



"""
Esercizio 3: serie multiple (100 asset), 5 anni, rendimenti, correlazioni e plot scalabili.

Focus:
- dtype: float32
- visual: subset e/o aggregazione
- niente seaborn: solo Matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(7)

n_assets = 100
dates = pd.date_range("2019-01-01", "2023-12-31", freq="B")  # giorni lavorativi
assets = [f"Asset_{i}" for i in range(n_assets)]

# Simulo "prezzi" con random walk (più realistico di rand puro)
returns = (np.random.normal(0, 0.01, size=(len(dates), n_assets))).astype(np.float32)
prices = np.empty_like(returns)
prices[0] = 100
for t in range(1, len(dates)):
    prices[t] = prices[t - 1] * (1 + returns[t])

df_prices = pd.DataFrame(prices, index=dates, columns=assets)

# Rendimenti giornalieri (pct_change)
df_ret = df_prices.pct_change().dropna()

# Correlazioni: per la heatmap uso un subset (trade-off qualità/prestazioni)
subset = np.random.choice(assets, size=15, replace=False)
corr = df_ret[subset].corr().values

plt.figure(figsize=(9, 7))
plt.imshow(corr, aspect="auto")
plt.colorbar(label="Correlazione")
plt.xticks(range(len(subset)), subset, rotation=45, ha="right")
plt.yticks(range(len(subset)), subset)
plt.title("Heatmap correlazioni (subset 15/100)")
plt.tight_layout()
plt.savefig("ex3_corr_subset.png", dpi=150, bbox_inches="tight")
plt.show()

# Scatter ottimizzato: rischio vs rendimento per singolo asset (non per tutti i punti)
mean_ret = df_ret.mean().astype(np.float32)
vol = df_ret.std().astype(np.float32)

plt.figure(figsize=(9, 6))
plt.scatter(vol.values, mean_ret.values, s=12, alpha=0.5, rasterized=True)
plt.xlabel("Volatilità (std)")
plt.ylabel("Rendimento medio")
plt.title("Asset map: volatilità vs rendimento (100 punti, leggibile)")
plt.tight_layout()
plt.savefig("ex3_risk_return_map.png", dpi=150, bbox_inches="tight")
plt.show()