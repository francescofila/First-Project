import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

rng = np.random.default_rng(42)

def scott_bw_1d(x):
    x = np.asarray(x).ravel()
    n = x.size
    s = np.std(x, ddof=1)
    return s * (n ** (-1/5))

def silverman_bw_1d(x):
    x = np.asarray(x).ravel()
    n = x.size
    s = np.std(x, ddof=1)
    q75, q25 = np.percentile(x, [75, 25])
    iqr = q75 - q25
    a = min(s, iqr/1.34) if iqr > 0 else s
    return 0.9 * a * (n ** (-1/5))

def kde_1d(x, grid, h):
    x = np.asarray(x).ravel()[:, None]
    kde = KernelDensity(kernel="gaussian", bandwidth=float(h)).fit(x)
    return np.exp(kde.score_samples(grid[:, None]))

def kde_2d(X, grid_xy, h):
    kde = KernelDensity(kernel="gaussian", bandwidth=float(h)).fit(X)
    return np.exp(kde.score_samples(grid_xy))


import pandas as pd

def make_tips_like(n=244, seed=7):
    r = np.random.default_rng(seed)
    time = r.choice(["Lunch", "Dinner"], size=n, p=[0.3, 0.7])
    smoker = r.choice(["Yes", "No"], size=n, p=[0.4, 0.6])
    base = r.gamma(shape=6, scale=3, size=n)
    base += np.where(time == "Dinner", r.normal(3, 2, size=n), r.normal(0, 1.5, size=n))
    base += np.where(smoker == "Yes", r.normal(1.0, 1.0, size=n), r.normal(0, 1.0, size=n))
    base = np.clip(base, 2, None)
    return pd.DataFrame({"total_bill": base, "time": time, "smoker": smoker})

tips = make_tips_like()

grid = np.linspace(tips["total_bill"].min()-2, tips["total_bill"].max()+2, 600)

plt.figure(figsize=(9,4))
for g, df_g in tips.groupby("time"):
    h = silverman_bw_1d(df_g["total_bill"].to_numpy())
    plt.plot(grid, kde_1d(df_g["total_bill"].to_numpy(), grid, h), label=g)
plt.title("Esempio 3 — KDE condizionata: total_bill per time")
plt.xlabel("total_bill"); plt.ylabel("density (per gruppo)")
plt.legend(); plt.tight_layout(); plt.show()



import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

rng = np.random.default_rng(42)

def scott_bw_1d(x):
    x = np.asarray(x).ravel()
    n = x.size
    s = np.std(x, ddof=1)
    return s * (n ** (-1/5))

def silverman_bw_1d(x):
    x = np.asarray(x).ravel()
    n = x.size
    s = np.std(x, ddof=1)
    q75, q25 = np.percentile(x, [75, 25])
    iqr = q75 - q25
    a = min(s, iqr/1.34) if iqr > 0 else s
    return 0.9 * a * (n ** (-1/5))

def kde_1d(x, grid, h):
    x = np.asarray(x).ravel()[:, None]
    kde = KernelDensity(kernel="gaussian", bandwidth=float(h)).fit(x)
    return np.exp(kde.score_samples(grid[:, None]))

def kde_2d(X, grid_xy, h):
    kde = KernelDensity(kernel="gaussian", bandwidth=float(h)).fit(X)
    return np.exp(kde.score_samples(grid_xy))




# ===================
# Esercizio 1 - istogramma + KDE con 3 bandwidth (Scott, Silverman, manuale)
# ===================

from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame.copy()
df.columns = [c.replace(" (cm)", "").replace(" ", "_") for c in df.columns]

x = df["sepal_length"].to_numpy()
grid = np.linspace(x.min()-0.5, x.max()+0.5, 600)

h_sc = scott_bw_1d(x)
h_si = silverman_bw_1d(x)
h_manual = 0.15

plt.figure(figsize=(9,4))
plt.hist(x, bins=20, density=True, alpha=0.3, label="Istogramma")
plt.plot(grid, kde_1d(x, grid, h_sc), label=f"Scott (h={h_sc:.3f})")
plt.plot(grid, kde_1d(x, grid, h_si), linestyle="--", label=f"Silverman (h={h_si:.3f})")
plt.plot(grid, kde_1d(x, grid, h_manual), linestyle=":", label=f"Manuale (h={h_manual:.2f})")
plt.title("Esercizio 1 — Iris sepal_length")
plt.legend(); plt.tight_layout(); plt.show()



# ===================
# Esercizio 2 - KDE 2D con contour+fill + scatter
# ===================

"""calcolo densità massima stimata e punto mediano della griglia"""
x = df["sepal_length"].to_numpy()
y = df["sepal_width"].to_numpy()
X = np.column_stack([x, y])

gx = np.linspace(x.min()-0.5, x.max()+0.5, 140)
gy = np.linspace(y.min()-0.5, y.max()+0.5, 140)
xx, yy = np.meshgrid(gx, gy)
grid_xy = np.column_stack([xx.ravel(), yy.ravel()])

h = 0.25
z = kde_2d(X, grid_xy, h).reshape(xx.shape)

max_dens = z.max()
max_idx = np.unravel_index(np.argmax(z), z.shape)
max_point = (xx[max_idx], yy[max_idx])

mid_point = (gx[len(gx)//2], gy[len(gy)//2])
mid_dens = kde_2d(X, np.array([mid_point]), h)[0]

print("Max densità:", max_dens)
print("Punto max:", max_point)
print("Punto mediano griglia:", mid_point, "densità:", mid_dens)

plt.figure(figsize=(7,6))
plt.contourf(xx, yy, z, levels=12)
plt.contour(xx, yy, z, levels=12)
plt.scatter(x[::5], y[::5], s=10, alpha=0.35, label="Punti (1/5)")
plt.scatter([max_point[0]], [max_point[1]], s=60, label="Max densità")
plt.scatter([mid_point[0]], [mid_point[1]], s=60, marker="x", label="Mediano griglia")
plt.title("Esercizio 2 — KDE 2D Iris")
plt.legend(); plt.tight_layout(); plt.show()



# ===================
# Esercizio 3 -  ancora KDE
# ===================
""" KDE di total_bill condizionata per smoker (Yes/No)
 e confronto common_norm=True/False """

grid = np.linspace(tips["total_bill"].min()-2, tips["total_bill"].max()+2, 600)

def plot_smoker(common_norm):
    plt.figure(figsize=(9,4))
    n_total = len(tips)
    for g, df_g in tips.groupby("smoker"):
        xg = df_g["total_bill"].to_numpy()
        h = silverman_bw_1d(xg)
        dens = kde_1d(xg, grid, h)
        if common_norm:
            dens = dens * (len(df_g) / n_total)
        plt.plot(grid, dens, label=f"{g} (n={len(df_g)})")
    plt.title("Esercizio 3 — " + ("common_norm=True" if common_norm else "common_norm=False"))
    plt.legend(); plt.tight_layout(); plt.show()

plot_smoker(False)
plot_smoker(True)



# ===================
# Esercizio 4 - GridSearchCV
# ===================

""" GridSearchCV per bandwidth ottimale su univariata
 + plot KDE risultante """

x = df["sepal_length"].to_numpy()[:, None]
params = {"bandwidth": np.logspace(-2, 0, 30)}
gridcv = GridSearchCV(KernelDensity(kernel="gaussian"), params, cv=5)
gridcv.fit(x)
best_h = gridcv.best_estimator_.bandwidth
print("Best bandwidth:", best_h)

grid = np.linspace(x.min()-0.5, x.max()+0.5, 600)
dens = kde_1d(x.ravel(), grid, best_h)

plt.figure(figsize=(9,4))
plt.hist(x.ravel(), bins=20, density=True, alpha=0.3, label="Istogramma")
plt.plot(grid, dens, label=f"KDE (best h={best_h:.3f})")
plt.title("Esercizio 4 — Bandwidth ottimale via CV")
plt.legend(); plt.tight_layout(); plt.show()


# ===================
# Esercizio 5 KDE 3D
# ===================

""" KDE 3D oppure slice condizionate su intervalli di X """


x = rng.normal(size=2000)
y = 0.7*x + rng.normal(scale=0.9, size=2000)
X = np.column_stack([x, y])

# 3D wireframe
gx = np.linspace(x.min()-1, x.max()+1, 70)
gy = np.linspace(y.min()-1, y.max()+1, 70)
xx, yy = np.meshgrid(gx, gy)
grid_xy = np.column_stack([xx.ravel(), yy.ravel()])
h = 0.50
z = kde_2d(X, grid_xy, h).reshape(xx.shape)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_wireframe(xx, yy, z, rstride=3, cstride=3, linewidth=0.6)
ax.set_title("Esercizio 5 — KDE 3D (wireframe)")
plt.tight_layout(); plt.show()

# Slice: KDE di Y per intervalli di X
bins = np.percentile(x, [0, 33, 66, 100])
grid_y = np.linspace(y.min()-1, y.max()+1, 600)

plt.figure(figsize=(9,4))
for i in range(3):
    mask = (x >= bins[i]) & (x < bins[i+1] if i < 2 else x <= bins[i+1])
    y_slice = y[mask]
    h_slice = silverman_bw_1d(y_slice)
    plt.plot(grid_y, kde_1d(y_slice, grid_y, h_slice),
             label=f"X in [{bins[i]:.2f}, {bins[i+1]:.2f}] (n={mask.sum()})")
plt.title("Esercizio 5 — Slice: KDE(Y | X in intervallo)")
plt.legend(); plt.tight_layout(); plt.show()



# ===================
# Esercizio 6 - slider per bandwidth + slider per sottocampionamento punti
# ===================

from matplotlib.widgets import Slider

x = np.concatenate([rng.normal(-2, 0.4, 350), rng.normal(2, 0.6, 350)])
grid = np.linspace(x.min()-1, x.max()+1, 600)

fig, ax = plt.subplots(figsize=(9,4))
plt.subplots_adjust(bottom=0.28)

# istogramma fisso
ax.hist(x, bins=45, density=True, alpha=0.3)

# linea KDE (placeholder)
(line,) = ax.plot([], [], lw=2)

# scatter punti sottocampionati sulla baseline
sc = ax.scatter([], [], s=12, alpha=0.35)

ax.set_title("Esercizio 6 — KDE interattiva: bandwidth + sottocampionamento")

# slider bandwidth
ax_bw = plt.axes([0.15, 0.12, 0.7, 0.03])
s_bw = Slider(ax_bw, "bandwidth", 0.02, 1.0, valinit=0.30)

# slider step (sottocampionamento)
ax_st = plt.axes([0.15, 0.06, 0.7, 0.03])
s_step = Slider(ax_st, "step", 1, 80, valinit=10, valstep=1)

def update(_):
    bw = float(s_bw.val)
    step = int(s_step.val)

    dens = kde_1d(x, grid, bw)
    line.set_data(grid, dens)

    xs = x[::step]
    ys = np.zeros_like(xs)
    sc.set_offsets(np.column_stack([xs, ys]))

    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

s_bw.on_changed(update)
s_step.on_changed(update)
update(None)

plt.show()