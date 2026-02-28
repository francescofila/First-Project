import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 31)
y = np.exp(0.2*x)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot (x, y, marker = "o", linewidth=1)

ax.set_yscale("log")
ax.set_xlabel("Giorno")
ax.set_ylabel("Casi (sacala log)")
ax.set_title("Crescita esponenziale: asse Y in LOG")

ax.grid(True, which="both", linestyle="--", linewidth=0.6)

plt.tight_layout()
plt.show()


# =============
# Es 2 ========

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

values = [1200, 15000, 2300000, 50000000]
labels = ["A", "B", "C", "D"]

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(labels, values)

def abbrev(x, pos):
    if x >= 1e9: return f"{x/1e9:.1f}B"
    if x >= 1e6: return f"{x/1e6:.1f}M"
    if x >= 1e3: return f"{x/1e3:.1f}K"
    return f"{int(x)}"

ax.yaxis.set_major_formatter(ticker.FuncFormatter(abbrev))
ax.set_ylabel("Ricavi")
ax.set_title("Vendite (ticks abbreviati)")
ax.grid(True, axis="y", linestyle="--", linewidth=0.6)

plt.tight_layout()
plt.show()