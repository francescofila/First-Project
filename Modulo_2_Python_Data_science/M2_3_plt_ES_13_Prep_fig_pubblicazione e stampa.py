"""
Esempio 1 — Grafico pronto per pubblicazione:
- figura impostata alla dimensione finale (circa 85 mm di larghezza)
- salvataggio in PNG (raster) e PDF (vettoriale)
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def mm_to_in(mm: float) -> float:
    """Converte millimetri in pollici (inches)."""
    return mm / 25.4


# Dati sintetici
x = np.linspace(0, 5, 50)
y = np.exp(x)

# Dimensione: 85 mm (1 colonna) x 63 mm circa
fig_w, fig_h = mm_to_in(85), mm_to_in(63)
fig, ax = plt.subplots(figsize=(fig_w, fig_h))

ax.plot(x, y, linewidth=1.5, label="Crescita esponenziale")
ax.set_title("Crescita esponenziale", fontsize=10)
ax.set_xlabel("Tempo", fontsize=9)
ax.set_ylabel("Valore", fontsize=9)
ax.legend(fontsize=8)

# Salvataggi
out_dir = Path("output_figures")
out_dir.mkdir(exist_ok=True)

fig.savefig(out_dir / "grafico_pubblicazione.png", dpi=300, bbox_inches="tight")
fig.savefig(out_dir / "grafico_pubblicazione.pdf", bbox_inches="tight")

plt.show()

"""
Esempio 2 — Leggibilità anche in bianco e nero:
- 3 serie distinguibili con linestyle (non solo colore)
- dimensione 1 colonna
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def mm_to_in(mm: float) -> float:
    """Converte millimetri in pollici (inches)."""
    return mm / 25.4


x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)

fig, ax = plt.subplots(figsize=(mm_to_in(85), mm_to_in(63)))

ax.plot(x, y1, linestyle="-", linewidth=1.5, label="Seno")
ax.plot(x, y2, linestyle="--", linewidth=1.5, label="Coseno")
ax.plot(x, y3, linestyle=":", linewidth=1.5, label="Seno+Coseno")

ax.set_title("Funzioni trigonometriche", fontsize=10)
ax.set_xlabel("Asse X", fontsize=9)
ax.set_ylabel("Valore", fontsize=9)
ax.legend(fontsize=8)

out_dir = Path("output_figures")
out_dir.mkdir(exist_ok=True)
fig.savefig(out_dir / "grafico_bn.png", dpi=300, bbox_inches="tight")

plt.show()


"""
Esempio 3 — Annotazioni:
- evidenzio un punto notevole (massimo locale)
- uso freccia e testo con offset per non sovrapporre ai dati
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def mm_to_in(mm: float) -> float:
    """Converte millimetri in pollici (inches)."""
    return mm / 25.4


x = np.linspace(0.1, 20, 200)          # evito 0 per non avere divisione per 0
y = np.sin(x) / x

fig, ax = plt.subplots(figsize=(mm_to_in(85), mm_to_in(63)))
ax.plot(x, y, linewidth=1.5, marker="o", markersize=3, label="sin(x)/x")

max_idx = np.argmax(y)

ax.annotate(
    "Massimo locale",
    xy=(x[max_idx], y[max_idx]),
    xytext=(x[max_idx] + 2, y[max_idx] + 0.1),
    arrowprops=dict(arrowstyle="->", lw=1),
    fontsize=8
)

ax.set_title("sin(x)/x con annotazioni", fontsize=10)
ax.set_xlabel("x", fontsize=9)
ax.set_ylabel("Valore", fontsize=9)
ax.legend(fontsize=8)

out_dir = Path("output_figures")
out_dir.mkdir(exist_ok=True)
fig.savefig(out_dir / "grafico_annotazioni.png", dpi=300, bbox_inches="tight")

plt.show()

"""
Esercizio 1 — PNG vs PDF (300 dpi)
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def mm_to_in(mm: float) -> float:
    return mm / 25.4


# 1) Dati e funzione
x = np.linspace(0, 6, 200)
y = 1 / (1 + np.exp(- (x - 3)))  # funzione logistica (S-curve)

# 2) Figura a dimensione finale (1 colonna)
fig, ax = plt.subplots(figsize=(mm_to_in(85), mm_to_in(60)))

ax.plot(x, y, linewidth=1.5, label="Logistica")
ax.set_title("Funzione logistica", fontsize=10)
ax.set_xlabel("x", fontsize=9)
ax.set_ylabel("y", fontsize=9)
ax.legend(fontsize=8)

# 3) Salvataggi
out_dir = Path("output_figures")
out_dir.mkdir(exist_ok=True)

fig.savefig(out_dir / "es1_funzione.png", dpi=300, bbox_inches="tight")
fig.savefig(out_dir / "es1_funzione.pdf", bbox_inches="tight")

plt.show()

"""
Esercizio 2 — 1 colonna (85 mm) vs 2 colonne (180 mm)
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def mm_to_in(mm: float) -> float:
    return mm / 25.4


x = np.linspace(0, 10, 300)
y = np.sin(x) * np.exp(-0.15 * x)

out_dir = Path("output_figures")
out_dir.mkdir(exist_ok=True)

# --- 1 colonna ---
fig1, ax1 = plt.subplots(figsize=(mm_to_in(85), mm_to_in(60)))
ax1.plot(x, y, linewidth=1.5, label="sin(x) attenuata")
ax1.set_title("1 colonna (85 mm)", fontsize=10)
ax1.set_xlabel("x", fontsize=9)
ax1.set_ylabel("y", fontsize=9)
ax1.tick_params(labelsize=8)
ax1.legend(fontsize=8)
fig1.savefig(out_dir / "es2_1col.png", dpi=300, bbox_inches="tight")

# --- 2 colonne ---
fig2, ax2 = plt.subplots(figsize=(mm_to_in(180), mm_to_in(70)))
ax2.plot(x, y, linewidth=1.8, label="sin(x) attenuata")
ax2.set_title("2 colonne (180 mm)", fontsize=11)
ax2.set_xlabel("x", fontsize=10)
ax2.set_ylabel("y", fontsize=10)
ax2.tick_params(labelsize=9)
ax2.legend(fontsize=9)
fig2.savefig(out_dir / "es2_2col.png", dpi=300, bbox_inches="tight")

plt.show()


"""
Esercizio 3 — 3 serie distinguibili in bianco e nero
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def mm_to_in(mm: float) -> float:
    return mm / 25.4


x = np.linspace(0, 2*np.pi, 400)
y1 = np.sin(x)
y2 = np.sin(2*x) * 0.7
y3 = np.cos(x) * 0.5

fig, ax = plt.subplots(figsize=(mm_to_in(85), mm_to_in(60)))

ax.plot(x, y1, linestyle="-",  linewidth=1.5, label="sin(x)")
ax.plot(x, y2, linestyle="--", linewidth=1.5, label="0.7 sin(2x)")
ax.plot(x, y3, linestyle=":",  linewidth=1.5, label="0.5 cos(x)")

ax.set_title("Grafico BN-safe", fontsize=10)
ax.set_xlabel("x", fontsize=9)
ax.set_ylabel("ampiezza", fontsize=9)
ax.legend(fontsize=8)

out_dir = Path("output_figures")
out_dir.mkdir(exist_ok=True)
fig.savefig(out_dir / "es3_bn_safe.png", dpi=300, bbox_inches="tight")

plt.show()

"""
Esercizio 4 — Annotazioni su punti notevoli
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def mm_to_in(mm: float) -> float:
    return mm / 25.4


x = np.linspace(0, 12, 500)
y = np.sin(x) * np.exp(-0.08 * x)  # oscillazione smorzata

fig, ax = plt.subplots(figsize=(mm_to_in(85), mm_to_in(60)))
ax.plot(x, y, linewidth=1.5, label="sin(x) smorzata")

# Punto notevole: massimo globale (in questo intervallo)
imax = np.argmax(y)
x_peak, y_peak = x[imax], y[imax]

ax.plot(x_peak, y_peak, marker="o", markersize=4)  # evidenzio il picco

ax.annotate(
    f"Picco: {y_peak:.2f}",
    xy=(x_peak, y_peak),
    xytext=(x_peak + 1.2, y_peak + 0.15),
    arrowprops=dict(arrowstyle="->", lw=1),
    fontsize=8
)

ax.set_title("Annotazioni coerenti", fontsize=10)
ax.set_xlabel("x", fontsize=9)
ax.set_ylabel("y", fontsize=9)
ax.legend(fontsize=8)

out_dir = Path("output_figures")
out_dir.mkdir(exist_ok=True)
fig.savefig(out_dir / "es4_annotazioni.png", dpi=300, bbox_inches="tight")

plt.show()