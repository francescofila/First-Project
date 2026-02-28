import pandas as pd

df_clienti = pd.DataFrame({"cliente": [1, 2, 3], "nome": ["Anna", "Luca", "Paolo"]})
df_trans   = pd.DataFrame({"cliente": [1, 2, 2], "importo": [100, 150, 200]})
df_promo   = pd.DataFrame({"cliente": [1, 3], "sconto": [10, 15]})
df_bonus   = pd.DataFrame({"cliente": [2, 3], "bonus": [5, 7]})

merge1 = pd.merge(df_clienti, df_trans, on="cliente", how="outer", validate="one_to_many")
merge2 = pd.merge(merge1, df_promo, on="cliente", how="outer")  # validate dipende dalle regole del dominio
df_final = pd.merge(merge2, df_bonus, on="cliente", how="outer")

print("Join complesso multiplo:\n", df_final)
