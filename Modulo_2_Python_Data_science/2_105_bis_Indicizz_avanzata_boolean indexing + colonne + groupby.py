import pandas as pd
import numpy as np

df_dip = pd.DataFrame({
    "Dipendente": ["Elena", "Giorgio", "Nadia", "Simone", "Chiara", "Fabio", "Riccardo", "Miriam", "Alessio", "Laura"],
    "Reparto": ["IT", "HR", "Sales", "IT", "Finance", "Sales", "IT", "HR", "Finance", "Sales"],
    "Età": [29, 41, 33, 26, 38, 31, 36, 28, 45, 34],
    "Stipendio": [2100, 2300, 1950, 1800, 2600, 2050, 3200, 1900, 2800, 2400],
    "AnniServizio": [2, 10, 5, 1, 8, 4, 12, 3, 15, 6]
})

# 1) Categoria Junior/Senior
df_dip["Categoria"] = np.where(df_dip["Età"] <= 35, "Junior", "Senior")

# 2) Filtro boolean
mask = ((df_dip["Età"] > 30) & (df_dip["Stipendio"] > 2000)) | (df_dip["Reparto"] == "IT")
selezionati = df_dip.loc[mask].copy()

# 3) Mostra solo alcune colonne
vista = selezionati.loc[:, ["Dipendente", "Età", "Stipendio"]]

# 4) Groupby: stipendio medio per Reparto e Categoria
stip_medio = (df_dip.groupby(["Reparto", "Categoria"], as_index=False)["Stipendio"]
              .mean()
              .rename(columns={"Stipendio": "Stipendio medio"})
              .sort_values("Stipendio medio", ascending=False)
              .reset_index(drop=True))

print("Selezionati (vista ridotta):\n", vista)
print("\nMedia stipendio per Reparto e Categoria (ordinata):\n", stip_medio)
