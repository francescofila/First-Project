import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

m = 300
df = pd.DataFrame({
    "sales": rng.normal(100, 15, size=m),
    "units": rng.normal(30, 6, size=m), 
    "revenue": rng.normal(2000, 300, size=m), 
    "returns": rng.normal(5, 2, size=m)
})

print(df)

# - correlazioni realistiche

df["revenue"] = df["sales"] * 20 + rng.normal(0, 150, size = m)
df["units"] = df["sales"] / 3 + rng.normal(0,2,size=m)

corr = df.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(corr.values, cmap="coolwarm", vmin=1 , vmax=1)


ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.index)))
ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticklabels(corr.index)

for i in range(corr.shape[0]):
    for j in range(corr.shape[1]):
        ax.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center", fontsize=9)

fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
ax.set_title("Heatmap correlazioni")
fig.tight_layout()
plt.show()
