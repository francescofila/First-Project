#Esempio 2 – Serie temporali con calcoli avanzati

import pandas as pd
import numpy as np

date_rng = pd.date_range(start="2026-01-01", end="2026-01-27", freq="d")
df = pd.DataFrame({
    "Data": date_rng,
    "Vendite": np.random.randint(50, 500, size=len(date_rng))
})

# Conversione e calcoli temporali
df["Data"] = pd.to_datetime(df["Data"])
df["Settimana"] = df["Data"].dt.isocalendar().week
df["Giorno_settimana"] = df["Data"].dt.day_name()
df["Vendite_cumulative"] = df["Vendite"].cumsum()
df["Delta_gg"] = (df["Data"] - df["Data"].min()).dt.days

# Resampling settimanale e mensile
df.set_index("Data", inplace=True)
settimanale = df[["Vendite"]].resample("W").sum()
mensile = df["Vendite"].resample("ME").mean()
print(settimanale.head())
print(mensile.head())

#Esempio 3 – Analisi combinata stringhe e tempo

data = {
    "Cliente": ["anna r.", "LUCA B.", "marta v.", "Paolo n."],
    "Email": ["anna@mail.com", "lucaa@", "marta@test", "paolo@mail.com"],
    "Data_ordine": ["2023-01-05", "2023-02-10", "2023-02-20", "2023-03-01"],
    "Importo": [120.5, 340.0, 215.7, 99.9]
}
df = pd.DataFrame(data)

# Pulizia nomi
df["Cliente"] = df["Cliente"].str.title().str.replace(r"\.", "", regex=True)

# Conversione date e calcolo giorni dall'ordine più recente
df["Data_ordine"] = pd.to_datetime(df["Data_ordine"])
df["Giorni_dall_ordine"] = (df["Data_ordine"].max() - df["Data_ordine"]).dt.days

# Validazione email e estrazione dominio
df["Email_valida"] = df["Email"].str.contains(r"@\w+\.\w+")
df["Dominio"] = df["Email"].str.extract(r"@(\w+\.\w+)")

print(df)