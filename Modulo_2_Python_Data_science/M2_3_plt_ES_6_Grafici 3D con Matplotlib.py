"""
Esercizio 1 — Mongolfiera: traiettoria 3D con velocità rappresentata a colori.
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 60, 300)

# traiettoria "morbida": deriva laterale + oscillazioni
x = 8*np.sin(t/6) + 0.08*t
y = 6*np.cos(t/7) + 0.05*t*np.sin(t/15)
z = 0.15*t + 0.6*np.sin(t/10)          # sale lentamente + piccola ondulazione

dt = t[1] - t[0]
vx = np.gradient(x, dt)
vy = np.gradient(y, dt)
vz = np.gradient(z, dt)
speed = np.sqrt(vx**2 + vy**2 + vz**2)

fig, ax = plt.subplots(figsize=(9, 6), subplot_kw={"projection": "3d"})

ax.plot(x, y, z, linewidth=1)  # riferimento
sc = ax.scatter(x, y, z, c=speed, s=18, alpha=0.9)

fig.colorbar(sc, ax=ax, shrink=0.65, label="Velocità (unità arbitrarie)")
ax.set_title("Mongolfiera: traiettoria 3D con velocità a colori")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Quota (Z)")

plt.show()


"""
Esercizio 2 — Scatter 3D meteo:
- colore = temperatura
- alpha = densità (più denso -> più trasparente per evitare macchie)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

np.random.seed(1)

n = 400
lon = np.random.uniform(-10, 10, n)
lat = np.random.uniform(-10, 10, n)
alt = np.random.uniform(0, 2500, n)  # metri

# temperatura: base + gradiente con lat e alt + rumore
temp = 20 - 0.004*alt + 0.15*lat + np.random.normal(0, 1.2, n)

# Densità locale via binning 2D
bins = 20
H, xedges, yedges = np.histogram2d(lon, lat, bins=bins)

# assegnazione bin per punto
ix = np.clip(np.digitize(lon, xedges) - 1, 0, bins-1)
iy = np.clip(np.digitize(lat, yedges) - 1, 0, bins-1)
density = H[ix, iy]

# alpha: più denso -> più trasparente (invertiamo e normalizziamo)
d_norm = (density - density.min()) / (density.max() - density.min() + 1e-9)
alpha = 0.15 + (1 - d_norm) * 0.85  # in [0.15, 1.0]

# RGBA: colore da temperatura + alpha per punto
norm = Normalize(vmin=temp.min(), vmax=temp.max())
cmap = cm.viridis
rgba = cmap(norm(temp))
rgba[:, 3] = alpha

fig, ax = plt.subplots(figsize=(9, 6), subplot_kw={"projection": "3d"})
sc = ax.scatter(lon, lat, alt, c=rgba, s=18)

# Colorbar: serve un mappable con cmap+norm (usiamo ScalarMappable)
mappable = cm.ScalarMappable(norm=norm, cmap=cmap)
mappable.set_array([])

fig.colorbar(mappable, ax=ax, shrink=0.65, label="Temperatura (°C)")

ax.set_title("Stazioni meteo 3D: colore=temperatura, alpha=densità")
ax.set_xlabel("Longitudine")
ax.set_ylabel("Latitudine")
ax.set_zlabel("Altitudine (m)")

plt.show()


"""
Esercizio 3 — Cratere: confronto surface vs wireframe.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 80)
y = np.linspace(-6, 6, 80)
X, Y = np.meshgrid(x, y)
R2 = X**2 + Y**2

# Cratere: differenza di due gaussiane (bordo + buca centrale)
Z = 18*np.exp(-0.12*R2) - 22*np.exp(-0.35*R2)

# --- Surface ---
fig1, ax1 = plt.subplots(figsize=(9, 6), subplot_kw={"projection": "3d"})
surf = ax1.plot_surface(X, Y, Z, alpha=0.95)
fig1.colorbar(surf, ax=ax1, shrink=0.65, label="Quota")
ax1.set_title("Cratere — plot_surface (impatto visivo)")
ax1.view_init(elev=28, azim=45)

# --- Wireframe ---
fig2, ax2 = plt.subplots(figsize=(9, 6), subplot_kw={"projection": "3d"})
ax2.plot_wireframe(X, Y, Z, linewidth=0.5, alpha=0.8)
ax2.set_title("Cratere — wireframe (struttura leggibile)")
ax2.view_init(elev=28, azim=45)

plt.show()