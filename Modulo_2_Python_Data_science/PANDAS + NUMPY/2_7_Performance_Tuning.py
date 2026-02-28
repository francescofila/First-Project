import pandas as pd

df = pd.DataFrame({
    "quantita": [1, 2, 3, 4, 5, ] * 20000, 
    "prezzo": [12.5, 9.9, 18.0, 7.2, 15.3] * 20000
})

print(df.dtypes)
print("MB prima:", df.memory_usage(deep=True).sum()/1024 **2)

df["quantita"] = pd.to_numeric(df["quantita"], downcast="unsigned")
df["prezzo"] = pd.to_numeric(df["prezzo"], downcast="float")

print(df.dtypes)
print("\nMB dopo downcast:", df.memory_usage(deep=True).sum()/ 1024 **2)


# =======
# Esercizio 2 — object ripetitivo → category
print("\n Esercizio 2 \n")
# =======

import pandas as pd

df = pd.DataFrame({
    "citta" :(["Venezia", "Milano", "Roma", "Torino"]* 50000)
})


print("\n dtype:", df["citta"].dtype)
print("MB object:", df["citta"].memory_usage(deep=True)/1024**2)




df["citta"] = df["citta"].astype("category")
print("dtype:", df["citta"].dtype)
print("MB category:", df["citta"].memory_usage(deep=True) / 1024**2)
print("categorie:", df["citta"].cat.categories.tolist())


# =======
# Esercizio  3 - Mixed dataset + trade-off
print("\n Esercizio 3 \n")
# =======

import pandas as pd
n = 100000

df = pd.DataFrame({
    "eta": list(range(n)),
    "prezzo": [10.0 + (i%7)*0.1 for i in range(n)],
    "categoria": ["vino", "vino", "libro", "vino", "libro"]* (n//5),
    "codice_ordine": [f"ORD{i:06d}" for i in range(n)],
    "data": ["31/01/2026"] * n 

})

print(df.info(memory_usage="deep"))