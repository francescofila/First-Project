# - Esercizio 1 creare un file .mplstyle per report vendite mensili (font, colori aziendali, linee coerenti) e applicarlo

# Checklist:

# - definisci una palette (anche solo 3–4 colori)
# - nel .mplstyle imposta: font.family, axes.*, grid.*, lines.linewidth
# - genera dati mensili (12 mesi)
# - applica stile e crea plot con titolo/etichette/legend
# - salva anche in PNG (300 dpi)

import numpy as np
import matplotlib.pyplot as plt

# 1) Creo il file di stile (qui lo scrivo da Python per comodità didattica, uno l'ho salvato sul mio mac)
style_text = """
font.family: Arial
font.size: 12

axes.titlesize: 16
axes.titleweight: bold
axes.labelsize: 12
axes.edgecolor: #0B1F3B
axes.labelcolor: #0B1F3B
axes.grid: True

grid.color: #D0D0D0
grid.linewidth: 0.8

lines.linewidth: 2.2
lines.markersize: 6

figure.facecolor: white
axes.facecolor: white
"""

with open("azienda.mplstyle", "w", encoding="utf-8") as f:
    f.write(style_text.strip())

# 2) Applico lo stile
plt.style.use("azienda.mplstyle")

# 3) Dati mensili sintetici
mesi = np.arange(1, 13)
vendite = np.random.randint(80, 180, size=12)

# 4) Grafico
fig, ax = plt.subplots(figsize=(9, 4.8))
ax.plot(mesi, vendite, label="Vendite", color="#1F5AA6", marker="o")  # colore “primario”
ax.set_title("Vendite mensili — Report aziendale")
ax.set_xlabel("Mese")
ax.set_ylabel("Unità vendute")
ax.set_xticks(mesi)
ax.legend()

# 5) Export
fig.savefig("vendite_mensili.png", dpi=300, bbox_inches="tight")
plt.show()


# - Esercizio 2
# - palette (almeno 4 colori) + grafico vendite vs acquisti su 12 mesi, verificando coerenza e leggibilità

import numpy as np
import matplotlib.pyplot as plt

palette = {
    "primario": "#1F5AA6",
    "secondario": "#F28C28",
    "accento": "#2AA876",
    "neutro": "#444444"
}

mesi = np.arange(1, 13)
vendite = np.random.randint(80, 180, size=12)
acquisti = np.random.randint(50, 140, size=12)

fig, ax = plt.subplots(figsize=(9, 4.8))
ax.plot(mesi, vendite, label="Vendite", color=palette["primario"], marker="o")
ax.plot(mesi, acquisti, label="Acquisti", color=palette["secondario"], marker="s", linestyle="--")

ax.set_title("Vendite vs Acquisti — 12 mesi", fontweight="bold")
ax.set_xlabel("Mese")
ax.set_ylabel("Unità")
ax.set_xticks(mesi)

ax.grid(True, alpha=0.25)
ax.legend()

plt.show() 

# - Esercizio 3
# - integrare font aziendale e logo, titolo con nome brand, annotazioni per punti chiave

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Branding base
plt.rcParams["font.family"] = "Arial"

mesi = np.arange(1, 13)
vendite = np.random.randint(80, 180, size=12)

fig, ax = plt.subplots(figsize=(9, 4.8))
ax.plot(mesi, vendite, color="#1F5AA6", marker="o", label="Vendite")

ax.set_title("Brand XYZ — Andamento vendite 2025", fontsize=16, fontweight="bold")
ax.set_xlabel("Mese")
ax.set_ylabel("Unità")
ax.set_xticks(mesi)
ax.grid(True, alpha=0.25)
ax.legend()

# Annotazione: evidenzio il massimo
idx_max = int(np.argmax(vendite))
x_max = mesi[idx_max]
y_max = vendite[idx_max]

ax.scatter([x_max], [y_max], s=60, color="#F28C28", zorder=3)
ax.annotate(
    f"Picco: {y_max}",
    xy=(x_max, y_max),
    xytext=(x_max + 0.5, y_max + 10),
    arrowprops=dict(arrowstyle="->", linewidth=1),
    fontsize=11
)

# Logo opzionale (metti un file 'logo.png' nella stessa cartella)
try:
    logo = plt.imread("logo.png")
    imagebox = OffsetImage(logo, zoom=0.12)
    ab = AnnotationBbox(imagebox, (0.98, 0.92), xycoords="axes fraction", frameon=False)
    ax.add_artist(ab)
except FileNotFoundError:
    pass  # ok: il logo non è disponibile in questa demo

plt.show()

# - Esercizio 4
# - creare un report PDF con grafici + tabella in un unico layout coerente.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Dati sintetici
mesi = np.arange(1, 13)
vendite = np.random.randint(80, 180, size=12)
acquisti = np.random.randint(50, 140, size=12)

df = pd.DataFrame({
    "Mese": mesi,
    "Vendite": vendite,
    "Acquisti": acquisti
})

# Stile “coerente”
plt.rcParams["font.family"] = "Arial"

fig = plt.figure(figsize=(9, 10))
gs = GridSpec(3, 1, figure=fig, height_ratios=[2.2, 0.2, 1.6])

# --- Grafico (in alto)
ax_plot = fig.add_subplot(gs[0, 0])
ax_plot.plot(mesi, vendite, label="Vendite", color="#1F5AA6", marker="o")
ax_plot.plot(mesi, acquisti, label="Acquisti", color="#F28C28", marker="s", linestyle="--")
ax_plot.set_title("Brand XYZ — Report mensile", fontsize=18, fontweight="bold")
ax_plot.set_xlabel("Mese")
ax_plot.set_ylabel("Unità")
ax_plot.set_xticks(mesi)
ax_plot.grid(True, alpha=0.25)
ax_plot.legend()

# --- Spazio (sottile)
ax_spacer = fig.add_subplot(gs[1, 0])
ax_spacer.axis("off")

# --- Tabella (in basso)
ax_tbl = fig.add_subplot(gs[2, 0])
ax_tbl.axis("off")

table = ax_tbl.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center"
)
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1, 1.4)

ax_tbl.set_title("Tabella dati — 12 mesi", fontsize=14, fontweight="bold", pad=12)

# Export PDF
fig.savefig("report_brand_xyz.pdf", dpi=300, bbox_inches="tight")
plt.show()



