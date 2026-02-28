# #Esempio 1 – Pulizia e trasformazione di dati testuali

import pandas as pd

data = {
     "Clienti": ["  Anna Rossi", "LUCA Bianchi", "mArTa Verdi  ", "Paolo  Neri"],
     "Email": ["anna@mail.com", "lucaa@", "marta@test", "paolo@mail.com"],
     "Telefono": ["+39 345 678 9012", "345678901", "0039-333-222-1111", "333 444 555"]
 }

df = pd.DataFrame(data)

 # Pulizia e uniformazione dei nomi

df["Clienti_puliti"] = df["Clienti"].str.strip().str.title()

print("\n", df)
print("\n", df["Clienti_puliti"])

# Valido email - estrazione dominio 

df["email_valida"] = df["Email"].str.contains(r"@\w+\.\w+")

print("\n", df["email_valida"])

df["dominio"] = df["Email"].str.extract(r"@(\w+\.\w+)")

print("\n", df["dominio"], "\n")

# Standardizzazione numeri di telefono

df["Telefono_pulito"] = df["Telefono"].str.replace(r"[^\d]", "", regex=True)

print("\n", df["Telefono_pulito"])

email_re = r"^[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}$"
df["email_valida"] = df["Email"].astype("string").str.match(email_re, na=False)

print("\n", df["email_valida"])
print(df.loc[df["email_valida"], "Email"])

# ------ ESEMPIO 2 ----


