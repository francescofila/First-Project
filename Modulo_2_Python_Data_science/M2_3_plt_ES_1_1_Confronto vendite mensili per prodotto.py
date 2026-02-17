import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

stores = ["Venezia", "Milano", "Roma"]
products = ["Libro", "Vino", "Caffè"]
months = pd.date_range("2026-01-01", periods=12, freq="MS")

rows = []

for store in stores:
    for prod in products:
        base = rng.integers(80,200)
        noise = rng.normal (0,8, size=len(months))
        season = 20 * np.sin(np.linspace(0,2+np.pi, len(months)))
        sales= np.clip(base + season + noise, 0 , None)
        for m, s in zip(months, sales):
            rows.append((store, prod, m, float(s)))

df = pd.DataFrame(rows, columns=["Store", "Product", "Month", "Sales"])

fig, axs = plt.subplots(len(stores), 1 , figsize=(10, 8), sharex=True, constrained_layout=True)

for i , store in enumerate(stores):
    ax = axs[i]
    sub = df[df["Store"] == store]

    for prod in products:
        s = sub[sub["Product"] == prod].set_index("Month")["Sales"]
        ax.plot(s.index, s.values, marker="o", label=prod)

        peak_pos = int(np.argmax(s.values))
        ax.annotate("picco",
                    xy = (s.index[peak_pos], s.values[peak_pos]),
                    xytext=(0,8), textcoords="offset points", 
                    ha = "center"
                    )
    
    ax.set_title(f"Vendite mensili - {store}")
    ax.grid(True, alpha=0.3)

axs[0].legend(ncol=len(products), loc="upper left")
fig.autofmt_xdate()
plt.show()