import pandas as pd
import numpy as np

dati = {"a" : [1, 2, 3, 4, 5,],
        "b": [10, 20, 30, 40, 50]
        }

df = pd.DataFrame(dati)

print("\n", df, "\n")

df["c"] = df ["a"] + df ["b"]

print("\n", df[["c"]])

df["d"] = df["a"] *2
df["e"] = np.log(df["c"])

print(df["d"], "\n")

print(df["e"])


# ==== PULIZIA dati =====

import pandas as pd

df = pd.DataFrame({"eta": [-5, 18, 130, 42]})


mask = df["eta"].between(0, 120)
df.loc[~mask, "eta"] = pd.NA


print(mask)


import pandas as pd

df = pd.DataFrame({"data": ["2025-01-10", "10/01/2025", "boh", None]})
df["data"] = pd.to_datetime(df["data"], errors="coerce")
print(df)
print(df["data"].dtype)

df["anno"] = df["data"].dt.year
df = df.sort_values("data")
mask = df["data"].between("2025-01-01", "2025-12-31")
print(mask)

im