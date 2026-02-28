import numpy as np
import matplotlib.pyplot as plt

def sales_heatmap_10x10(threshold=90, seed=10):
    """
    Heatmap 10x10: vendite mensili (colonne) per prodotto (righe).
    - Annotazioni: valore in ogni cella
    - Marker automatici: cerchio su valori > threshold
    """

    np.random.seed(seed)
    sales = np.random.randint(0,101, (10,10))

    months = [f"M{m+1}" for m in range(10)]
    products = [f"P{p+1}" for p in range(10)]

    fig, ax = plt.subplots(figsize=(8,7))
    im = ax.imshow(sales, cmap="viridis", interpolation="nearest")
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label("Vendite")

    ax.set_xticks(range(10), months)
    ax.set_yticks(range(10), products)
    ax.set_title("vendite mensili per prodotto (10x10)", pad =15)

    for i in range(10):
        for j in range(10):
            ax.text(j , i, str(sales[i,j]), ha="center", va="center", color="white")
            if sales[i, j]>threshold:
                ax.scatter(j, i, s=170, facecolors="none", edgecolors="black", linewidths=2)

    fig.tight_layout()
    plt.show()

sales_heatmap_10x10(threshold=90)



# stesso esercizio senza def

import numpy as np
import matplotlib.pyplot as plt

threshold = 90
seed = 10

np.random.seed(seed)
sales = np.random.randint(0, 101, (10, 10))

months = [f"M{m+1}" for m in range(10)]
products = [f"P{p+1}" for p in range(10)]

fig, ax = plt.subplots(figsize=(8, 7))

im = ax.imshow(sales, cmap="viridis", interpolation="nearest")
cbar = plt.colorbar(im, ax=ax)
cbar.set_label("Vendite")

ax.set_xticks(range(10), months)
ax.set_yticks(range(10), products)
ax.set_title("Vendite mensili per prodotto (10×10)", pad=15)

for i in range(10):
    for j in range(10):
        ax.text(j, i, str(sales[i, j]), ha="center", va="center", color="white")
        if sales[i, j] > threshold:
            ax.scatter(j, i, s=170, facecolors="none", edgecolors="black", linewidths=2)

fig.tight_layout()
plt.show()


#ESERCIZIO 3
'''
heatmap interattiva meteo (7 giorni x 7 città)
con dettagli al passaggio del mouse.
'''

import numpy as np
import matplotlib.pyplot as plt

def interactive_weather_heatmap(seed=7):
    """
    Heatmap 7x7 di temperature.
    Hover: mostra città, giorno e temperatura della cella sotto il cursore.
    """
    np.random.seed(seed)
    temps = np.random.randint(10, 36, (7, 7))  # 10..35

    days = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]
    cities = ["Venezia", "Milano", "Roma", "Torino", "Bologna", "Firenze", "Napoli"]

    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(temps, cmap="Spectral_r", interpolation="nearest") # "Spectral_r" : scala dai colori "meteo" con inversione _r (reversed)
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label("°C")

    ax.set_xticks(range(7), days)
    ax.set_yticks(range(7), cities)
    ax.set_title("Temperature (7 giorni × 7 città) — hover per dettagli", pad=15)

    annot = ax.annotate(
        "",
        xy=(0, 0),
        xytext=(12, 12),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="white", alpha=0.9),
        arrowprops=dict(arrowstyle="->")
    )
    annot.set_visible(False)

    def update(event):
        if event.inaxes != ax or event.xdata is None or event.ydata is None:
            annot.set_visible(False)
            fig.canvas.draw_idle()
            return

        x = int(event.xdata + 0.5)  # giorno (colonna)
        y = int(event.ydata + 0.5)  # città (riga)

        if 0 <= x < 7 and 0 <= y < 7:
            annot.xy = (x, y)
            annot.set_text(f"{cities[y]} • {days[x]} → {temps[y, x]} °C")
            annot.set_visible(True)
        else:
            annot.set_visible(True)

        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", update)
    plt.tight_layout()
    plt.show()

interactive_weather_heatmap()


# Esercizio 4 
# combina annotazioni dinamiche 
# + marker automatici per evidenziare valori critici e valori estremi insieme.


import numpy as np
import matplotlib.pyplot as plt

def heatmap_critical_and_extremes(size=8, critical_thr=85, seed=21):
    """
    Heatmap con:
    - marker su valori critici (> critical_thr)
    - marker speciale su massimo e minimo assoluti
    - annotazioni testuali solo su celle evidenziate (meno rumore)
    """
    np.random.seed(seed)
    data = np.random.randint(0, 100, (size, size))

    # Trova estremi
    min_pos = np.unravel_index(np.argmin(data), data.shape)
    max_pos = np.unravel_index(np.argmax(data), data.shape)

    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(data, cmap="viridis", interpolation="nearest")
    plt.colorbar(im, ax=ax)

    ax.set_title("Critici + estremi (marker + annotazioni mirate)", pad=15)

    for i in range(size):
        for j in range(size):
            val = data[i, j]

            is_critical = val > critical_thr
            is_min = (i, j) == min_pos
            is_max = (i, j) == max_pos

            # Marker per critici
            if is_critical:
                ax.scatter(j, i, s=160, facecolors="none", edgecolors="black", linewidths=2)

            # Marker per estremi
            if is_max:
                ax.scatter(j, i, s=190, marker="s", facecolors="none", edgecolors="black", linewidths=2.5)
            if is_min:
                ax.scatter(j, i, s=190, marker="X", color="black")

            # Annotazioni solo dove serve
            if is_critical or is_min or is_max:
                ax.text(j, i, str(val), ha="center", va="center", color="white")

    plt.tight_layout()
    plt.show()

heatmap_critical_and_extremes()