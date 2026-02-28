import pandas as pd
import numpy as np



df = pd.DataFrame({"email": ["sandro@estro.wine", "info@cantina.it", None]})

df["email_user"] = df["email"].astype("string").str.extract(r"([^@]+)")

print(df["email_user"], "\n" )

mask_ok = df["email"].astype("string").str.contains(r".+@.+", na=False)
df.loc[mask_ok, "email_user"] = df.loc[mask_ok, "email"].str.extract(r"([^@]+)")


print(df.loc[mask_ok])



df2 = pd.DataFrame({
    "timestamp": pd.date_range("2025-01-01", periods=6, freq="6h"),
    "temperature": [5,6,7,6,8,7]
})

df2["timestamp"] =pd.to_datetime(df2["timestamp"])
df2 = df2.set_index("timestamp")

df_giorno= df2.resample("D").mean()     
print("\n", df_giorno)                 



import pandas as pd 
import numpy as np

dati = ({"lunghezza": [7, 9, 3, 5, 10, 100],
        "larghezza": [9, 5, 7, 4, 3, 31]
        })



df_dati = pd.DataFrame(dati)

df_dati["area"] = df_dati["lunghezza"]*df_dati["larghezza"]

print(df_dati["area"])

# -----  one-hot encoding -----



df = pd.DataFrame({
    "Tipo": ["a", "r", "t", "e", "v", "i"],
    "Val": ["10", "3", "4", "5", "2", "3"]
})

df_ohe = pd.get_dummies(df["Tipo"], columns=["Tipo"], prefix="Tipo")

print(df_ohe, "\n")

# =========================
# ESERCIZIO 3
# =========================

rng = np.random.default_rng(42)

df3 = pd.DataFrame({
    "data": pd.date_range("2026-01-28", periods=10, freq="D"),
    "valore":rng.integers(10, 100, size=10)
})

df3["giorno_settimana"] = df3["data"].dt.dayofweek
df3["mese"] = df3["data"].dt.month

df3["diff_vs_ieri"] = df3["valore"].diff(1)

print("\n", df3)

lag_1 = df3["valore"].shift(1)

rolling_mean_3 = df3["valore"].shift(1).rolling(3).mean()

print(lag_1)

print()
print(rolling_mean_3)
# =========================
# Mini palestra : retail sales “time-safe”
# =========================

import pandas as pd
import numpy as np

rng = np.random.default_rng(42)

n_days = 120
stores = [1, 2, 3]
items = [101, 102, 103, 104]

df = pd.DataFrame(
    [(s, i, d) for s in stores for i in items
     for d in pd.date_range("2024-01-01", periods=n_days, freq="D")],
    columns=["store_id", "item_id", "date"]
)

print("\n",df, "\n")

print("\n DOW \n")
dow = df["date"].dt.dayofweek.values
print("\n", dow, "\n")

print("\n SEASON \n")

season = 10 + 3*np.sin(2*np.pi*dow/7)
print("\n", season, "\n")

print("\n STORE_EFF \n")

store_eff = df["store_id"].map({1: 0.0, 2: 2.0, 3: -1.0}).values
print("\n", store_eff, "\n")

print("\n ITEM_EFF \n")
item_eff = df["item_id"].map({101: 1.0, 102: -0.5, 103: 2.5, 104: 0.0}).values
print("\n", item_eff, "\n")

print("\n NOISE \n")
noise = rng.normal(0, 1.5, size=len(df)) # Cosa fa: aggiunge rumore casuale gaussiano (media 0, deviazione 1.5).
print("\n", noise, "\n")

print("\n SALES \n")
df["sales"] = np.maximum(0, season + store_eff + item_eff + noise)
print("\n", df["sales"], "\n")


df = df.sort_values(["store_id", "item_id", "date"]).reset_index(drop=True)
 
print(df)

df["month"] = df["date"].dt.month
df["day_of_week"] = df["date"].dt.dayofweek

df["dow_sin"] = np.sin(2 * np.pi * df["day_of_week"] / 7)
df["dow_cos"] = np.cos(2 * np.pi * df["day_of_week"] / 7)

g = df.groupby(["store_id", "item_id"])["sales"]
df["lag_1"] = g.shift(1)

df["rolling_mean_7"] = df.groupby(["store_id", "item_id"])["sales"].transform(
    lambda s: s.shift(1).rolling(7).mean()
)

df["rolling_std_7"]  = df.groupby(["store_id", "item_id"])["sales"].transform(
    lambda s: s.shift(1).rolling(7).std()
)

print("\n", df["rolling_std_7"], "\n")

df["store_item_mean_past"] = df.groupby(["store_id", "item_id"])["sales"].transform(
    lambda s: s.expanding().mean().shift(1)
)

df_fe = df.dropna(subset=["lag_1", "rolling_mean_7", "store_item_mean_past"]).copy()

print(df_fe[["store_id","item_id","date","sales","lag_1","rolling_mean_7","store_item_mean_past","dow_sin","dow_cos"]].head(10))

df["z_local"] = (df["sales"] - df["rolling_mean_7"]) / df["rolling_std_7"]

print("\n", df["z_local"], "\n")

df["delta_1d"] = df["sales"] - df["lag_1"]
print("\n", df["delta_1d"], "\n")