import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

stores = ["Venezia", "Milano", "Roma"]
months = pd.date_range("2026-01-01", periods=12, freq="MS")

rows = []
for store in stores:
    sales = rng.integers(100, 220, size=len(months))
    units = rng.integers(20, 80, size=len(months))
    revenue = sales * rng.integers(15, 25, size=len(months))
    for d, s, u, r in zip(months, sales, units, revenue):
        rows.append((store, d, int(s), int(u), int(r)))

df = pd.DataFrame(rows, columns=["Store", "Month","Sales", "Units", "Revenue"])

fig, axs = plt.subplots(2, 2, figsize=(12,8), constrained_layout=True)


# (0,0) Line: Sales per store

for store in stores:
    sub = df[df["Store"]== store].set_index("Month")
    axs[0, 0].plot(sub.index, sub["Sales"], marker="o", label=store)
axs[0,0].set_title("Vendite(line)")
axs[0,0].grid(True, alpha=0.3)

# (0,1) Bar: Units totali per store

unit_tot = df.groupby("Store")["Units"].sum()
axs[0, 1].bar(unit_tot.index, unit_tot.values)
axs[0, 1].set_title("Unità totali (bar)")
axs[0, 1].grid(True, axis="y", alpha=0.3)

# (1,0) Scatter: Sales vs Revenue color by store
codes = df["Store"].astype("category").cat.codes
axs[1, 0].scatter(df["Sales"], df["Revenue"], c=codes, cmap="tab10", alpha=0.7)
axs[1, 0].set_title("Vendite vs Fatturato (scatter)")
axs[1, 0].set_xlabel("Sales")
axs[1, 0].set_ylabel("Revenue")
axs[1, 0].grid(True, alpha=0.3)


# (1,1) Line: Revenue per store
for store in stores:
    sub = df[df["Store"] == store].set_index("Month").sort_index()
    axs[1, 1].plot(sub.index, sub["Revenue"], marker="o", label=store)
axs[1, 1].set_title("Fatturato (line)")
axs[1, 1].grid(True, alpha=0.3)

# legenda comune
handles, labels = axs[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc="upper center", ncol=len(stores))

for ax in axs.flat:
    for lab in ax.get_xticklabels():
        lab.set_rotation(45)
        lab.set_ha("right")

import matplotlib.dates as mdates

# (0,0) Vendite (line)
axs[0, 0].set_ylabel("Vendite")
axs[0, 0].set_xlabel("Mese")  # opzionale, perché sharex: puoi metterla solo in basso

# (0,1) Unità totali (bar)
axs[0, 1].set_ylabel("Unità (somma anno)")
axs[0, 1].set_xlabel("Store")

# (1,1) Fatturato (line)
axs[1, 1].set_ylabel("Fatturato")
axs[1, 1].set_xlabel("Mese")

# Formattazione asse tempo (solo sui grafici con Month)
for ax in (axs[0, 0], axs[1, 1]):
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))      # un tick ogni 2 mesi
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))         # Jan, Feb, ...



fig.autofmt_xdate()
plt.show()