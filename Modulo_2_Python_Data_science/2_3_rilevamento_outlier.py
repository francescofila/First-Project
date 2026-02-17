import pandas as pd
import numpy as np

# DATASET con un outliner
df = pd.DataFrame({
    "importo": [12, 15, 14, 13, 16, 15, 14, 13, 12, 15, 14, 13, 16, 15, 14, 13, 12, 15, 14, 130]
})

print("\n", df["importo"].describe())
print("\n", "Media:", df["importo"].mean())
print("\n", "Mediana:", df["importo"].median(), "\n")

# --- IRQ ----

q1= df["importo"].quantile(0.25)
q3= df["importo"].quantile(0.75)

irq=q3-q1

lower = q1 - 1.5*q1
upper = q3 + 1.5*q3


mask_irq = (df["importo"]< lower) | (df["importo"]> upper)
outliners_irq = df[mask_irq]

print("\nIRQ fences:", lower, "|", upper)
print("Outliers (IRQ):")
print(outliners_irq)

# --- Z-scsore ----

median = df["importo"].median()
mad = np.median(np.abs(df["importo"]-median))

z_rob = 0.6745 * (df["importo"]- median) / mad
outliners_mad = df[abs(z_rob)> 3.5] #soglia tipica

print("\n Outliers (Robust Z vIA MAD) : ")
print("\n", outliners_mad, "\n")

# ---- CAPPING ----

df["importo_capped"] = df["importo"].clip(upper, lower)

print("\nMedia iniziale: ", df["importo"].mean())
print("\nMedia dopo capping:", df["importo_capped"].mean(), "\n")

from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

rng = np.random.default_rng(42)

normali = rng.normal(loc=0, scale=1, size=(200,2))
anomali = rng.normal(loc=6, scale=0.5, size=(5,2))

X = np.vstack([normali, anomali])

df2 = pd.DataFrame(X, columns= ["x","y"])

print(X, "\n")
print("\n", df2, "\n")

print(normali.shape, "\n")  # (200, 2)
print(anomali.shape, "\n")  # (5, 2)
print(X.shape, "\n")        # (205, 2)


iso = IsolationForest (contamination=0.02, random_state=42)

df2["iso_pred"] = iso.fit_predict(df2[["x","y"]])

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.02)
df2["lof_pred"] = lof.fit_predict(df2[["x","y"]])

print("\n Outlier IsolationForest:", (df2["iso_pred"] == -1).sum())
print("\n Outlier LOF: ", (df2["lof_pred"] == -1).sum())

# Outlier secondo Isolation Forest
out_iso = df2[df2["iso_pred"] == -1]
print(out_iso, "\n")

# Outlier secondo LOF
out_lof = df2[df2["lof_pred"] == -1]
print(out_lof, "\n")

iso_mask = df2["iso_pred"] == -1
lof_mask = df2["lof_pred"] == -1

df2["iso_score"] = iso.score_samples(df2[["x", "y"]])  # più basso = più anomalo
print(df2.loc[iso_mask, ["x", "y", "iso_score"]].sort_values("iso_score"))
