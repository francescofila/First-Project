import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, AutoDateLocator

rng = np.random.default_rng(42)

dates = pd.date_range("2026-01-01", periods=60, freq="D")
traffic = rng.integers(200, 1200, size=len(dates))

df = pd.DataFrame({"traffic": traffic}, index=dates)

df["ma7"] = df["traffic"].rolling(7, min_periods=1).mean()

threshold = 1000

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(df.index, df["traffic"], marker="o", linewidth=1, label="Traffico")
ax.plot(df.index, df["ma7"], linestyle="--", linewidth=2, label=" Media mobile 7 gg")
ax.axhline(threshold, linestyle=":", linewidth=2, label=f"Soglia {threshold}")

paeks = df[df["traffic"]> threshold]

for d , val in paeks["traffic"].items():
    ax.annotate(f"{int(val)}", xy = (d, val), xytext=(0,8),
                textcoords="offset points", ha= "center")

ax.xaxis.set_major_locator(AutoDateLocator())
ax.xaxis.set_major_formatter(DateFormatter("%d-%m"))
fig.autofmt_xdate()

ax.set_title("Traffico web giornaliero con media mobile e soglia")
ax.set_ylabel("Visite")
ax.grid(True, alpha=0.3)
ax.legend()
plt.show()


locator
