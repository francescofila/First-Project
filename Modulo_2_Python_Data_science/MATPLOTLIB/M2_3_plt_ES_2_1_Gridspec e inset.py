import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

x = np.linspace(0, 10, 200)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2*x)
y4 = np.exp(-0.2*x)+np.sin(x)


fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(3, 2, figure = fig)

ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[0,1])
ax3 = fig.add_subplot(gs[1:,0]) # occupa due righe
ax4 = fig.add_subplot(gs[1,1])

# cella rimanente (terza riga, destra): la lasciamo vuota ma “gestita”
ax_empty = fig.add_subplot(gs[2, 1])
ax_empty.axis("off")

ax1.plot(x, y1)
ax1.set_title("Principale 1")

ax2.plot(x, y2)
ax2.set_title("Principale 2")

ax3.plot(x, y3)
ax3.set_title("Verticale (2 righe)")

ax4.plot(x, y4)
ax4.set_title("Piccolo")

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

x = np.linspace(0, 10, 400)
y_main = np.exp(-0.1*x) * np.sin(x)
y_left = np.cos(x)
y_right = np.sin(2*x)

fig = plt.figure(figsize=(11, 7), constrained_layout=True)
gs = gridspec.GridSpec(2, 2, figure=fig, height_ratios=[2, 1])

ax_main = fig.add_subplot(gs[0, :])
ax_l = fig.add_subplot(gs[1, 0])
ax_r = fig.add_subplot(gs[1, 1])

# Main
ax_main.plot(x, y_main, marker="o", markevery=30, linewidth=1.5, label="exp(-0.1x)·sin(x)")
ax_main.set_title("Dashboard — Grafico principale")
ax_main.set_xlabel("x")
ax_main.set_ylabel("y")
ax_main.legend(loc="upper left")

# Secondari
ax_l.plot(x, y_left, linestyle="--", label="cos(x)")
ax_l.set_title("Secondario sinistra")
ax_l.legend()

ax_r.plot(x, y_right, linestyle="-.", label="sin(2x)")
ax_r.set_title("Secondario destra")
ax_r.legend()

# Inset sul picco
i = np.argmax(y_main)
i0 = max(i - 25, 0)
i1 = min(i + 25, len(x) - 1)

ax_in = inset_axes(ax_main, width="35%", height="35%", loc="upper right")
ax_in.plot(x, y_main)
ax_in.set_xlim(x[i0], x[i1])
ax_in.set_ylim(y_main[i0:i1].min(), y_main[i0:i1].max())
ax_in.set_title("Zoom picco", fontsize=9)

plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Dati
x = np.linspace(0, 10, 400)
y_main = np.exp(-0.1 * x) * np.sin(x)
y_left = np.cos(x)
y_right = np.sin(2 * x)

# Layout dashboard
fig = plt.figure(figsize=(11, 7), constrained_layout=True)
gs = gridspec.GridSpec(2, 2, figure=fig, height_ratios=[2, 1])

ax_main = fig.add_subplot(gs[0, :])
ax_l = fig.add_subplot(gs[1, 0])
ax_r = fig.add_subplot(gs[1, 1])

# --- Grafico principale
ax_main.plot(
    x, y_main,
    marker="o", markevery=30,
    linewidth=1.5,
    label="exp(-0.1x)·sin(x)"
)
ax_main.set_title("Dashboard — Grafico principale")
ax_main.set_xlabel("x")
ax_main.set_ylabel("y")
ax_main.legend(loc="upper left")

# --- Subplot in basso (con labels x/y)
ax_l.plot(x, y_left, linestyle="--", label="cos(x)")
ax_l.set_title("Secondario sinistra")
ax_l.set_xlabel("x")
ax_l.set_ylabel("y")
ax_l.legend()

ax_r.plot(x, y_right, linestyle="-.", label="sin(2x)")
ax_r.set_title("Secondario destra")
ax_r.set_xlabel("x")
ax_r.set_ylabel("y")
ax_r.legend()

# --- Inset: centrato in alto dentro ax_main
# [left, bottom, width, height] in coordinate relative all'Axes principale (0..1)
ax_in = ax_main.inset_axes([0.33, 0.56, 0.34, 0.38])  # <-- qui lo centri/posizioni fine

# Linea inset rossa
ax_in.plot(x, y_main, color="red", linewidth=1.6)
ax_in.set_title("Zoom picco", fontsize=9)

# Zoom sul massimo (picco)
i = np.argmax(y_main)
i0 = max(i - 25, 0)
i1 = min(i + 25, len(x) - 1)
ax_in.set_xlim(x[i0], x[i1])
ax_in.set_ylim(y_main[i0:i1].min(), y_main[i0:i1].max())

plt.show()
