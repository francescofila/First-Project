import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

# =========================================================
# 1. Caricamento dataset
# =========================================================
data = load_diabetes(as_frame=True)
df = data.frame

print("Feature:", data.feature_names)
print(df.head())

X = df[data.feature_names]
y = df["target"]

# =========================================================
# 2. Addestramento modello
# =========================================================
model = LinearRegression()
model.fit(X, y)

# =========================================================
# 3. Parametri del modello
# =========================================================
print("\nIntercetta:")
print(model.intercept_)

print("\nCoefficienti:")
for nome, coeff in zip(data.feature_names, model.coef_):
    print(f"{nome}: {coeff:.4f}")

# =========================================================
# 4. Predizioni
# =========================================================
y_pred = model.predict(X)

# =========================================================
# 5. Metri
# =========================================================
mae = np.mean(np.abs(y - y_pred))
print(f"\nMAE: {mae:.3f}")

# Residui con segno
residui = y - y_pred

# =========================================================
# 6. Grafico 1 - Scatter del target reale
# =========================================================
plt.figure(figsize=(8, 5))
plt.scatter(range(len(y)), y, alpha=0.7)
plt.xlabel("Indice osservazione")
plt.ylabel("Target reale")
plt.title("Distribuzione dei valori target - Diabetes")
plt.grid(True)
plt.tight_layout()
plt.show()

# =========================================================
# 7. Grafico 2 - Valori reali vs predetti
# =========================================================
plt.figure(figsize=(8, 5))
plt.scatter(range(len(y)), y, alpha=0.7, label="Valori reali")
plt.scatter(range(len(y_pred)), y_pred, alpha=0.7, label="Valori predetti")
plt.xlabel("Indice osservazione")
plt.ylabel("Valore target")
plt.title("Confronto tra valori reali e predetti")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# =========================================================
# 8. Grafico 3 - Residui
# =========================================================
plt.figure(figsize=(8, 5))
plt.scatter(range(len(residui)), residui, alpha=0.7, label="Residui")
plt.axhline(y=0, linestyle="--", linewidth=2, label="Errore nullo")
plt.xlabel("Indice osservazione")
plt.ylabel("Residuo (y_reale - y_pred)")
plt.title("Grafico dei residui")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()