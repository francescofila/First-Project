

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------
# Dataset "tips-like" sintetico (offline-friendly)
# ----------------------------
rng = np.random.default_rng(42)
n = 260
tips = pd.DataFrame({
    "sex": rng.choice(["Male", "Female"], size=n, p=[0.62, 0.38]),
    "day": rng.choice(["Thur", "Fri", "Sat", "Sun"], size=n, p=[0.25, 0.08, 0.40, 0.27]),
    "size": rng.integers(1, 7, size=n),
})
tips["total_bill"] = rng.lognormal(mean=np.log(18), sigma=0.45, size=n)
tips["tip"] = (
    0.15 * tips["total_bill"]
    + rng.normal(0, 1.2, size=n)
    + np.where(tips["sex"] == "Female", 0.3, 0.0)
)
tips["tip"] = np.clip(tips["tip"], 0.5, None)

sns.set_theme(style="whitegrid", context="notebook")

# ----------------------------
# 1) BASE (nessun gruppo)
# ----------------------------
plt.figure(figsize=(7.5, 5))
ax = sns.scatterplot(data=tips, x="total_bill", y="tip", alpha=0.75)
ax.set_title("Scatter BASE — tip vs total_bill (senza hue/facet)")
plt.tight_layout()
plt.show()

# ----------------------------
# 2) HUE (gruppi colorati)
# ----------------------------
plt.figure(figsize=(7.5, 5))
ax = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", alpha=0.75)
ax.set_title("Scatter con HUE — tip vs total_bill (hue=sex)")
plt.tight_layout()
plt.show()

# ----------------------------
# 3) FACET (pannelli separati)
# ----------------------------
g = sns.relplot(
    data=tips, x="total_bill", y="tip",
    col="day", col_order=["Thur", "Fri", "Sat", "Sun"],
    kind="scatter", height=3.4, aspect=1.05, alpha=0.75
)
g.set_axis_labels("total_bill", "tip")
g.set_titles("day = {col_name}")
g.figure.suptitle("Scatter con FACET — tip vs total_bill (col=day)", y=1.05)
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

tips = sns.load_dataset("tips")

g = sns.lmplot(
    data=tips, x="total_bill", y="tip",
    hue="sex", height=6, aspect=1.2
)
g.figure.suptitle("Relazione tra conto totale e mancia (regressione per sesso)", y=1.02)
plt.show()



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

categorie = np.array(["Romanzo", "Saggio", "Poesia"])
gruppi = np.array(["Gruppo A", "Gruppo B"])

n = 180
df = pd.DataFrame({
    "Categoria": rng.choice(categorie, size=n),
    "Gruppo": rng.choice(gruppi, size=n),
})

# valori con una differenza leggera tra gruppi e categorie
base = df["Categoria"].map({"Romanzo": 55, "Saggio": 65, "Poesia": 50}).to_numpy()
shift = (df["Gruppo"] == "Gruppo B").to_numpy() * 5
df["Valore"] = base + shift + rng.normal(0, 8, size=n)

# --- Matplotlib: media per categoria (aggregazione manuale)
mean_by_cat = df.groupby("Categoria")["Valore"].mean().reindex(categorie)

plt.figure(figsize=(7, 4))
plt.bar(mean_by_cat.index, mean_by_cat.values)
plt.title("Matplotlib — Valore medio per categoria")
plt.xlabel("Categoria")
plt.ylabel("Valore medio")
plt.tight_layout()
plt.show()

# --- Seaborn: aggregazione + estetica automatica
sns.set_theme(style="whitegrid")
plt.figure(figsize=(7, 4))
sns.barplot(data=df, x="Categoria", y="Valore", hue="Gruppo")
plt.title("Seaborn — Valore medio per categoria (con hue)")
plt.tight_layout()
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

tips = sns.load_dataset("tips")

# lmplot
g = sns.lmplot(
    data=tips, x="total_bill", y="tip",
    hue="sex", height=6, aspect=1.2
)
g.figure.suptitle("tips — Regressione tip vs total_bill (hue=sex)", y=0.98)
plt.show()

# violinplot
plt.figure(figsize=(7, 4))
sns.violinplot(data=tips, x="day", y="tip", palette="mako")
plt.title("tips — Distribuzione mancia per giorno")
plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

styles = ["darkgrid", "whitegrid", "dark", "white", "ticks"]

for st in styles:
    sns.set_theme(style=st, context="notebook")
    ax = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", alpha=0.7)
    ax.set_title(f"style='{st}'")
    plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# (opzionale ma utile) resetta eventuali stili Matplotlib attivi
plt.style.use("default")

tips = sns.load_dataset("tips")

styles = ["darkgrid", "whitegrid", "dark", "white", "ticks"]

fig = plt.figure(figsize=(14, 8))
handles = labels = None

for i, st in enumerate(styles, start=1):
    # lo stile viene applicato PRIMA che l'axes venga creato
    with sns.axes_style(st), sns.plotting_context("notebook"):
        ax = fig.add_subplot(2, 3, i)

        sns.scatterplot(
            data=tips, x="total_bill", y="tip", hue="sex",
            alpha=0.7, ax=ax
        )
        ax.set_title(f"style='{st}'")
        ax.set_xlabel("total_bill")
        ax.set_ylabel("tip")

        if handles is None:
            handles, labels = ax.get_legend_handles_labels()
        if ax.get_legend() is not None:
            ax.get_legend().remove()

# 6° pannello vuoto
ax_empty = fig.add_subplot(2, 3, 6)
ax_empty.axis("off")

fig.legend(handles, labels, title="sex", loc="upper right")
fig.suptitle("Stesso plot, 5 temi Seaborn (subplots)", y=0.98)
fig.tight_layout(rect=[0, 0, 0.88, 0.95])
plt.show()



# ============================
# HEATMAP DI CORRELAZIONE
# ============================

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

tips = sns.load_dataset("tips")
corr = tips.corr(numeric_only=True)

plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("Matrice di correlazione (variabili numeriche)")
plt.tight_layout()
plt.show()




# ============================
# ESERCIZIO - PAIRPLOT + 
# ============================

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

penguins = sns.load_dataset("penguins").dropna()

# pairplot

g = sns.pairplot(penguins, hue="species")
g.fig.subplots_adjust(top=0.93)
g.fig.suptitle("Penguins — Pairplot (hue=species)", y=0.99)
plt.show()

# heatmap di correlazione

corr = penguins.corr(numeric_only=True)

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("penguins - Correlazione (Variabili numeriche)")
plt.tight_layout()
plt.show()




# ============================
# Esercizio 4 scenari: dashboard vs pubblicazione
# ============================

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)

mesi = pd.date_range("2025-01-01", periods=12, freq="MS").strftime("%b")
categorie = ["Libri", "Corsi", "Eventi"]

rows = []
for cat in categorie:
    base_sales = rng.integers(80, 140)
    trend = rng.normal(0, 4, size=len(mesi)).cumsum()
    sales = base_sales + trend + rng.normal(0, 6, size=len(mesi))
    profit = sales * rng.uniform(0.12, 0.22) + rng.normal(0, 2, size=len(mesi))
    for m, s, p in zip(mesi, sales, profit):
        rows.append({"Mese": m, "Categoria": cat, "Sales": s, "Profit": p})

df = pd.DataFrame(rows)

# --- Dashboard (Seaborn): confronto rapido per categoria
sns.set_theme(style="whitegrid")
g = sns.catplot(
    data=df, x="Mese", y="Sales",
    col="Categoria", kind="bar",
    col_wrap=3, height=3.2, aspect=1.2
)
g.set_titles("{col_name}")
g.set_xticklabels(rotation=45)
g.fig.suptitle("Dashboard — Sales mensili per categoria", y=1.03)
plt.show()

# --- Pubblicazione (Matplotlib): controllo + annotazioni
pivot = df.pivot_table(index="Mese", columns="Categoria", values="Profit", aggfunc="mean").reindex(mesi)

fig, ax = plt.subplots(figsize=(9, 4.5))
for cat in categorie:
    ax.plot(pivot.index, pivot[cat], marker="o", label=cat)

ax.set(
    title="Pubblicazione — Profit medio mensile (con annotazioni)",
    xlabel="Mese",
    ylabel="Profit"
)
ax.legend()

# annotazione: picco per una categoria
target = "Corsi"
peak_idx = pivot[target].idxmax()
peak_val = pivot[target].max()
ax.annotate(
    f"Picco {target}: {peak_val:.1f}",
    xy=(peak_idx, peak_val),
    xytext=(0, 18),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->")
)

plt.tight_layout()
plt.show()