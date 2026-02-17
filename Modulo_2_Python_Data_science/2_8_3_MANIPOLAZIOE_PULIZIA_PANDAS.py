import pandas as pd
import numpy as np
import re

# ---- dalla libreria re ( regular expression creo regex che usero con funzione più volte)

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

# ---- Creo funnzione per il calcolo della memoria che usero più volte
# -   quanta RAM occupa un DataFrame, in kilobyte (KB)
 
  
def mem_kb(df: pd.DataFrame) -> float:
    return df.memory_usage(deep=True).sum()/1024

# ---- creo funzione che calcola i “limiti” dell’IQR 

def irq_bounds(s: pd.Series, k:float =1.5):
    s= s.dropna()
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    irq = q3-q1
    return (q1-k * irq, q3 + k*irq)

# ---- crea funzione che crea la maschera booleana degli outlier 

def flag_iqr_outliers(s:pd.Series, k: float= 1.5) -> pd.Series:
    low, high = irq_bounds(s, k=k)
    return(s<low) | (s>k)


#    =======================================


# ---- ESERCIZIO 2 — Dataset vendite
# 1) dataset clienti "sporco"

print("\n =======\n")
print(" ESERCIZIO 3 — Dataset completo misto (pipeline) ")
print("\n =======\n")



dataset = pd.DataFrame({
    "Nome": ["  Sandro", "Beatrice  ", "Luca", "Marta", "Giulia"],
    "Email": ["sandro@mail.com", "beatrice@mail.it", "luca@@mail.com", None, "giulia@mail.it "],
    "Data_iscrizione": ["2025-12-01", "01/12/2025", "2026-01-05", "rotto", "2026-01-20"],
    "Età": [31, 33, 35, None, 36],
    "Stipendio": ["1800", "2500", "2200", "1700", "99999"],
    "Città": ["Venezia ", " Venezia", "Milano", "milano", "Venezia"],
    "Prodotto": ["Libro: Solaris", "Vino: Raboso", "Saggio: Popper", "Vino: Raboso", "Libro: Solaris"],
    "Categoria": ["Libri", "Vini", "Saggistica", "Vini", "Libri"],
    "Vendite": ["25,00", "60", None, "10,00", "12.50"],
    "Giorni_attivi": [120, 45, 10, None, 200]
})

dataset_raw = dataset.copy()

print("\n", dataset, "\n")

print("\n Memoria iiniziale (KB): ", round(mem_kb(dataset_raw), 2), "\n")

df = dataset_raw.copy()

#  1) Pulisci stringhe (Nome/Città/Prodotto/Categoria) + normalizza

def clean_text(s: pd.Series, title: bool = True) -> pd.Series:
    s = (s.astype("string")
         .str.strip()
         .str.replace(r"\s+", " ", regex=True))
    return s.str.title() if title else s

df["Nome"] = clean_text(df["Nome"], title=True)
df["Città"] = clean_text(df["Città"], title=True)
df["Prodotto"] = clean_text(df["Prodotto"], title=False)
df["Categoria"] = clean_text(df["Categoria"], title=True)

#  2) Email valida (regex) -> email_valida

df["Email"] = df["Email"].astype("string").str.strip().str.lower()
df["email_valida"] = df["Email"].apply(lambda x: bool(EMAIL_RE.match(x)) if pd.notna(x) else False)

#  3) Date: Data_iscrizione -> datetime (errors="coerce")

df["Data_iscrizione"] = pd.to_datetime(df["Data_iscrizione"], errors="coerce", dayfirst=True)

#  4) Numerici: Età, Stipendio, Vendite, Giorni_attivi

df["Età"] = pd.to_numeric(df["Età"], errors="coerce")
df["Stipendio"] = pd.to_numeric(df["Stipendio"], errors="coerce")

vend = (df["Vendite"].astype("string")
        .str.replace("€", "", regex=False)
        .str.replace(r"\s+", "", regex=True)
        .str.replace(",", ".", regex=False))
df["Vendite"] = pd.to_numeric(vend, errors="coerce")

df["Giorni_attivi"] = pd.to_numeric(df["Giorni_attivi"], errors="coerce")

#  5) Missing: imputazioni ragionate (mediana per numerici, moda per Città/Categoria)

for col in ["Età", "Stipendio", "Vendite", "Giorni_attivi"]:
    df[col] = df[col].fillna(df[col].median())

for col in ["Città", "Categoria"]:
    moda = df[col].mode(dropna=True)
    df[col] = df[col].fillna(moda.iloc[0] if len(moda) else "Mancante")

#  6) Outlier: stipendio e vendite (IQR) -> colonne booleane

df["is_outlier_stipendio"] = flag_iqr_outliers(df["Stipendio"])
df["is_outlier_vendite"] = flag_iqr_outliers(df["Vendite"])


#  7) Feature (almeno 2 usando apply/map/lambda combinando variabili):
#   - valore_giornaliero = Vendite / (Giorni_attivi + 1)
df["valore_giornaliero"] = df["Vendite"] / (df["Giorni_attivi"] + 1)


#   - segmento = f"{Città}-{Categoria}" (apply)
df["segmento"] = df.apply(lambda r: f"{r['Città']}-{r['Categoria']}", axis=1)

#   - mesi_da_iscrizione = differenza tra oggi e Data_iscrizione in mesi circa
today = pd.Timestamp.today().normalize()
df["mesi_da_iscrizione"] = ((today - df["Data_iscrizione"]).dt.days / 30.44).round(1)

#  8) Analizza memoria prima/dopo e ottimizza: category + float32/Int16 dove sensato

df["Città"] = df["Città"].astype("category")
df["Categoria"] = df["Categoria"].astype("category")
df["Prodotto"] = df["Prodotto"].astype("category")
df["segmento"] = df["segmento"].astype("category")

df["Età"] = df["Età"].round().astype("Int16")
df["Giorni_attivi"] = df["Giorni_attivi"].round().astype("Int16")

for col in ["Stipendio", "Vendite", "valore_giornaliero"]:
    df[col] = df[col].astype("float32")

print("Memoria (KB) dopo:", round(mem_kb(df), 2))

print("\n", df, )