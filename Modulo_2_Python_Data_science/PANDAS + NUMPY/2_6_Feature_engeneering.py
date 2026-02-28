import pandas as pd

df = pd.DataFrame({
    "citta": ["Venezia", "Milano", "Venezia", "Roma", "Roma", "Venezia"]
})

print("Unici:", df["citta"].nunique())
print("Mem (object) MB:", df["citta"].memory_usage(deep=True) / 1024**2)

df["citta"] = df["citta"].astype("category")

print("Mem (category) MB:", df["citta"].memory_usage(deep=True) / 1024**2)
print("Categorie:", df["citta"].cat.categories.tolist())


import pandas as pd

df = pd.DataFrame({
    "eta": [19, 35, 42, 28],
    "prezzo": [12.50, 9.90, 18.00, 7.20],
})

# interi non negativi -> unsigned (uint8/uint16/...)
df["eta"] = pd.to_numeric(df["eta"], downcast="unsigned")

# float -> float32 se possibile
df["prezzo"] = pd.to_numeric(df["prezzo"], downcast="float")

print(df.dtypes)
