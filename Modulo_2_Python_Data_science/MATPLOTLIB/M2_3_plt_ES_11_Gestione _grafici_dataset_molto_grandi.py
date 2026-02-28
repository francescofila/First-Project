
# Esercizio lezione 1 — Sampling casuale (scatter leggibile)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x= np.linspace(0, 100, 1_000_000)
y= np.sin(x) + np.random.normal(0, 0.5, len(x))
df = pd.DataFrame({"x":x, "y":y})

# sampling 1% 
df_sample = df.sample(frac=0.01, random_state=42)

plt.figure(figsize=(10, 5))
plt.scatter(df_sample["x"], df_sample["y"], alpha=0.6, s=8)
plt.title("Sampling casuale del 1% dei dati")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Esercizio lezione 2 — Streaming con FuncAnimation (buffer circolare)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data, y_data = [], []

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 100)
ax.set_ylim(-2, 2)

def init():
    """Inizializza la linea vuota."""
    line.set_data([], [])
    return (line,)

def update(frame):
    """Aggiunge un punto e mantiene un buffer circolare di 100 punti."""
    x_data.append(frame)
    y_data.append(np.sin(frame / 5) + np.random.normal(0, 0.1))

    if len(x_data) > 100:
        x_data.pop(0)
        y_data.pop(0)

    line.set_data(x_data, y_data)
    return (line,)

ani = FuncAnimation(
    fig, update,
    frames=np.arange(0, 200),
    init_func=init,
    blit=True,
    interval=50
)

plt.show()

# Esercizio lezione 3 — Sampling stratificato (pattern per categoria)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Riparto dal df enorme (x,y)
x = np.linspace(0, 100, 1_000_000)
y = np.sin(x) + np.random.normal(0, 0.5, len(x))
df = pd.DataFrame({"x": x, "y": y})

# Categoria (es. fondazione A/B/C)
df["categoria"] = np.random.choice(["A", "B", "C"], size=len(df), p=[0.5, 0.3, 0.2])

# Stratified sampling: 0.5% per categoria
df_sample_strat = (
    df.groupby("categoria", group_keys=False)
      .apply(lambda g: g.sample(frac=0.005, random_state=42))
)

plt.figure(figsize=(10, 5))
for cat in ["A", "B", "C"]:
    subset = df_sample_strat[df_sample_strat["categoria"] == cat]
    plt.scatter(subset["x"], subset["y"], alpha=0.6, s=8, label=f"Categoria {cat}")

plt.legend()
plt.title("Sampling stratificato per categoria")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Esercizio lezione 4 — Streaming “quick & dirty” con plt.pause

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 50)
ax.set_ylim(-2, 2)

x_data, y_data = [], []

for i in range(200):
    x_data.append(i)
    y_data.append(np.sin(i / 5) + np.random.normal(0, 0.1))

    # Ultimi 50 punti
    if len(x_data) > 50:
        x_data = x_data[-50:]
        y_data = y_data[-50:]

    line.set_data(x_data, y_data)
    plt.pause(0.05)

plt.show()


# # Esercizio 1 - dataset sintetico da 5 milioni di punti

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

N = 5_000_000

# Categorie (fondazioni) con probabilità diverse
categorie = rng.choice(["F1", "F2", "F3", "F4", "F5", "F6"], size=N, p=[0.30, 0.20, 0.15, 0.15, 0.10, 0.10])

# Feature numerica "x"
x = rng.uniform(0, 100, size=N).astype("float32")

# Pattern diverso per categoria (così lo stratificato ha senso)
offset = pd.Series(categorie).map({"F1": 0.0, "F2": 0.5, "F3": -0.5, "F4": 1.0, "F5": -1.0, "F6": 0.2}).to_numpy().astype("float32")
noise = rng.normal(0, 0.4, size=N).astype("float32")
y = (np.sin(x) + offset + noise).astype("float32")

df = pd.DataFrame({"x": x, "y": y, "categoria": categorie})

# 1) Sampling casuale (es. 0.1% = 5.000 punti)
df_rand = df.sample(frac=0.001, random_state=42)

plt.figure(figsize=(10, 5))
plt.scatter(df_rand["x"], df_rand["y"], alpha=0.6, s=8)
plt.title("Esercizio 1 — Sampling casuale (0.1%)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 2) Sampling stratificato: stessa frazione per categoria (0.05% = 2.500 circa totali se bilanciato, qui dipende)
df_strat = (
    df.groupby("categoria", group_keys=False)
      .apply(lambda g: g.sample(frac=0.0005, random_state=42))
)

plt.figure(figsize=(10, 5))
for cat in sorted(df_strat["categoria"].unique()):
    s = df_strat[df_strat["categoria"] == cat]
    plt.scatter(s["x"], s["y"], alpha=0.6, s=8, label=cat)

plt.legend(title="Categoria")
plt.title("Esercizio 1 — Sampling stratificato per categoria")
plt.xlabel("x")
plt.ylabel("y")
plt.show()



# Esercizio 2 - streaming in tempo reale di sin e cos con buffer di 200 punti

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

BUFFER = 200
xbuf = deque(maxlen=BUFFER)
ysin = deque(maxlen=BUFFER)
ycos = deque(maxlen=BUFFER)

fig, ax = plt.subplots()
line_sin, = ax.plot([], [], lw=2, label="sin")
line_cos, = ax.plot([], [], lw=2, label="cos")

ax.set_ylim(-1.5, 1.5)
ax.legend()

def init():
    line_sin.set_data([], [])
    line_cos.set_data([], [])
    ax.set_xlim(0, BUFFER)
    return (line_sin, line_cos)

def update(frame):
    xbuf.append(frame)
    ysin.append(np.sin(frame * 0.1))
    ycos.append(np.cos(frame * 0.1))

    line_sin.set_data(list(xbuf), list(ysin))
    line_cos.set_data(list(xbuf), list(ycos))

    # Finestra che scorre
    if frame > BUFFER:
        ax.set_xlim(frame - BUFFER, frame)

    return (line_sin, line_cos)

ani = FuncAnimation(fig, update, init_func=init, frames=np.arange(0, 2000), blit=True, interval=30)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import time

plt.ion()
fig, ax = plt.subplots(figsize=(8,4))
xdata, y1data, y2data = [], [], []
line1, = ax.plot([], [], label='sin')
line2, = ax.plot([], [], label='cos')
ax.set_xlim(0, 200)
ax.set_ylim(-1.5, 1.5)
ax.legend()
ax.set_title("Streaming dati sintetici — buffer 200 punti")

buffer_size = 200
t = 0

while t<2000:
    # aggiungi nuovo punto
    xdata.append(t)
    y1data.append(np.sin(t/10))
    y2data.append(np.cos(t/10))

    # mantieni solo ultimi 200
    if len(xdata) > buffer_size:
        xdata = xdata[-buffer_size:]
        y1data = y1data[-buffer_size:]
        y2data = y2data[-buffer_size:]

    # aggiorna grafico
    line1.set_data(xdata, y1data)
    line2.set_data(xdata, y2data)
    ax.set_xlim(min(xdata), max(xdata) if max(xdata)>buffer_size else buffer_size)

    plt.pause(0.01)
    t += 1



# - Esercizio 3 , aggiungi uno slider per modificare la finestra (buffer) in tempo reale

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from collections import deque

buffer_size = 200
xbuf = deque(maxlen=buffer_size)
ysin = deque(maxlen=buffer_size)
ycos = deque(maxlen=buffer_size)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.20)

line_sin, = ax.plot([], [], lw=2, label="sin")
line_cos, = ax.plot([], [], lw=2, label="cos")
ax.set_ylim(-1.5, 1.5)
ax.legend()

# Slider
ax_slider = plt.axes([0.15, 0.06, 0.70, 0.04])
slider = Slider(ax=ax_slider, label="Buffer", valmin=50, valmax=800, valinit=buffer_size, valstep=10)

def set_buffer(new_size: int):
    """Ricrea i buffer mantenendo gli ultimi dati."""
    global buffer_size, xbuf, ysin, ycos
    buffer_size = new_size

    x_old = list(xbuf)
    sin_old = list(ysin)
    cos_old = list(ycos)

    xbuf = deque(x_old[-buffer_size:], maxlen=buffer_size)
    ysin = deque(sin_old[-buffer_size:], maxlen=buffer_size)
    ycos = deque(cos_old[-buffer_size:], maxlen=buffer_size)

def on_slider_change(val):
    set_buffer(int(val))

slider.on_changed(on_slider_change)

def init():
    line_sin.set_data([], [])
    line_cos.set_data([], [])
    ax.set_xlim(0, buffer_size)
    return (line_sin, line_cos)

def update(frame):
    xbuf.append(frame)
    ysin.append(np.sin(frame * 0.1))
    ycos.append(np.cos(frame * 0.1))

    line_sin.set_data(list(xbuf), list(ysin))
    line_cos.set_data(list(xbuf), list(ycos))

    if frame > buffer_size:
        ax.set_xlim(frame - buffer_size, frame)
    else:
        ax.set_xlim(0, buffer_size)

    return (line_sin, line_cos)

ani = FuncAnimation(fig, update, init_func=init, frames=np.arange(0, 5000), blit=True, interval=30)
plt.show()


# - Esercizio 4 - visualizzazione aggregata: medie mobili o aggregazioni per finestre vs punti singoli. 
#                 Confronta performance e leggibilità


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

N = 2_000_000  # puoi portarlo più su, ma già così si sente
t0 = pd.Timestamp("2026-01-01")

# 2M punti a 10ms => ~5.5 ore di dati
time = pd.date_range(t0, periods=N, freq="10ms")
signal = np.sin(np.linspace(0, 2000, N)) + rng.normal(0, 0.4, N)

df = pd.DataFrame({"time": time, "valore": signal}).set_index("time")

# 1) "Raw" (prendo una finestra, altrimenti non è un confronto onesto)
raw = df.iloc[:50_000]  # 50k punti: ancora gestibile
plt.figure(figsize=(10, 4))
plt.plot(raw.index, raw["valore"], lw=1)
plt.title("Esercizio 4 — Serie raw (solo prima finestra, 50k punti)")
plt.show()

# 2) Aggregazione: media ogni 1 secondo
agg = df["valore"].resample("1S").mean()

plt.figure(figsize=(10, 4))
plt.plot(agg.index, agg.values, lw=2)
plt.title("Esercizio 4 — Aggregazione (media ogni 1s)")
plt.show()

# 3) Media mobile sull'aggregato (più liscia)
roll = agg.rolling(window=10, min_periods=1).mean()

plt.figure(figsize=(10, 4))
plt.plot(roll.index, roll.values, lw=2)
plt.title("Esercizio 4 — Media mobile (10s) sull'aggregato")
plt.show()