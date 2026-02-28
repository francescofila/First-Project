# ===========
# Esercizio 1
# Consumi energetici domestici (misurazioni orarie)
# ===========


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# Simulo 60 giorni di consumo orario con pattern giornaliero + rumore
idx = pd.date_range("2025-01-01", periods=60*24, freq="H")
base = 200 + 40*np.sin(2*np.pi*(idx.hour/24))          # ciclo giornaliero
weekend = np.where(idx.dayofweek >= 5, 20, 0)          # weekend un filo più alto
rumore = np.random.normal(0, 15, len(idx))

consumo = base + weekend + rumore
df = pd.DataFrame({"Consumo_kWh": consumo}, index=idx)

daily = df.resample("D").mean()
weekly = df.resample("W").mean()

df.plot(figsize=(12,4), title="Consumo orario (raw)")
plt.show()

daily.plot(figsize=(12,4), title="Consumo medio giornaliero")
plt.show()

weekly.plot(figsize=(12,4), title="Consumo medio settimanale")
plt.show()


import matplotlib.dates as mdates

fig, axs = plt.subplots(3, 1, figsize=(12, 9), sharex=True)

# 1) Raw (orario)
axs[0].plot(df.index, df["Consumo_kWh"], linewidth=0.8, alpha=0.8)
axs[0].set_title("Consumo orario (raw)")

# 2) Media giornaliera
axs[1].plot(daily.index, daily["Consumo_kWh"], linewidth=1.5)
axs[1].set_title("Consumo medio giornaliero")

# 3) Media settimanale
axs[2].plot(weekly.index, weekly["Consumo_kWh"], linewidth=2)
axs[2].set_title("Consumo medio settimanale")

# Griglia + label coerenti
for ax in axs:
    ax.grid(True, alpha=0.25)
    ax.set_ylabel("kWh")

axs[2].set_xlabel("Data")

# Date leggibili (tick automatici “intelligenti”)
locator = mdates.AutoDateLocator(minticks=6, maxticks=10)
axs[2].xaxis.set_major_locator(locator)
axs[2].xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))

fig.suptitle("Consumo energetico: raw vs aggregazioni", y=1.02)
fig.tight_layout()
plt.show()




# ===========
# Esercizio 2
# Serie epidemica
# ===========

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

idx = pd.date_range("2025-01-01", periods=120, freq="D")

# Simulo un'ondata: cresce, picco, scende + rumore
t = np.arange(len(idx))
onda = 20 + 200*np.exp(-0.5*((t-60)/15)**2)
rumore = np.random.normal(0, 10, len(idx))
casi = np.maximum(0, onda + rumore)

df = pd.DataFrame({"Casi": casi}, index=idx)

df["MA7"] = df["Casi"].rolling(7).mean()

# Caloclo una EMA: Exponential Moving Average = media mobile esponenziale.
df["EMA"] = df["Casi"].ewm(span=14, adjust=False).mean()

ax = df[["Casi","MA7","EMA"]].plot(figsize=(12,5), title="MA7 vs EMA")
ax.set_xlabel("Data")
ax.set_ylabel("Nuovi casi")
plt.show()


# ===========
# Esercizio 3
# Trasporto Pubblico
# ===========

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

idx = pd.date_range("2023-01-01", periods=90, freq="D")
temp = 8 + 6*np.sin(2*np.pi*np.arange(len(idx))/30) + np.random.normal(0, 1, len(idx))

# Passeggeri: un po' più alti quando fa "meglio" + pattern settimanale
weekly_pattern = np.where(idx.dayofweek < 5, 1.0, 0.7)  # weekend meno
passeggeri = 10000*weekly_pattern + 250*temp + np.random.normal(0, 400, len(idx))

df = pd.DataFrame({"Temperatura": temp, "Passeggeri": passeggeri}, index=idx)

# 1) Doppi assi
fig, ax1 = plt.subplots(figsize=(12,5))
ax1.plot(df.index, df["Temperatura"], label="Temperatura")
ax1.set_ylabel("°C")

ax2 = ax1.twinx()
ax2.plot(df.index, df["Passeggeri"], label="Passeggeri")
ax2.set_ylabel("N passeggeri")

fig.suptitle("Temperatura vs Passeggeri (twinx)")
plt.show()

# 2) Normalizzazione (z-score)
z = (df - df.mean()) / df.std()
z.plot(figsize=(12,5), title="Temperatura vs Passeggeri (normalizzati, z-score)")
plt.show()