# =========================
# PROGETTO 3
# Analisi di un Sistema di Prenotazione Viaggi
# (Python, funzioni, OOP, NumPy, Pandas, Matplotlib)
# =========================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------- Parte 1: Variabili e tipi di dati --------
nome = "Joseph Cooper"
eta = 34 
saldo_conto = 2500.75
vip = True

destinazioni = ["Roma", "Parigi", "Tokyo", "New York", "Il Cairo", "Città del Capo"]

prezzi_medi = {
    "Roma": 450,
    "Parigi": 650,
    "Tokyo": 1400,
    "New York": 1300,
    "Il Cairo": 800,
    "Città del Capo": 1200
}

# -------- Parte 2: Programmazione ad Oggetti (OOP) --------
class Cliente:
    def __init__(self, nome, eta, vip):
        self.nome = nome
        self.eta = eta
        self.vip = vip

    def stampa_info(self):
        print(f"Cliente: {self.nome} | Età: {self.eta} | VIP: {self.vip}")

class Viaggio:
    def __init__(self, destinazione, prezzo, durata_giorni):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata_giorni = durata_giorni

class Prenotazione:                                     # collega cliente e viaggio
    def __init__(self, cliente, viaggio, giorno_partenza):
        self.cliente = cliente
        self.viaggio = viaggio
        self.giorno_partenza = giorno_partenza
    
    def importo_finale(self):
        if self.cliente.vip:
            return self.viaggio.prezzo * 0.9            # sconto 10 se cliete vip
        return self.viaggio.prezzo
    
    def dettagli(self):
        importo = self.importo_finale()
        print(
            f"Prenotazione| Cliente: {self.cliente.nome} | Destinazione: {self.viaggio.destinazione} |"
            f"Prezzo: {self.viaggio.prezzo:.2f} | Durata: {self.viaggio.durata_giorni} giorni |"
            f"Partenza: {self.giorno_partenza.date()} | Incasso: {importo:.2f} € "
        )

# -------- Parte 7 (parziale): funzione richiesta --------

def top_n_clienti(df, n):                               # funzione che lavora su DataFrame e restituisce top N clienti
    conteggi = df["Cliente"].value_counts()
    return conteggi.head(n)

# -------- Simulazione + conversione a DataFrame --------

def genera_clienti():
    nomi = [
        "Anna Bianchi", "Luca Verdi", "Giulia Neri", "Marco Gallo", "Sara Conti",
        "Paolo Riva", "Elena Fontana", "Davide Costa", "Marta Greco", "Stefano Longo",
        "Ilaria Sala", "Franco De Santis", "Chiara Martini", "Andrea Ricci", "Valentina Moretti"
    ]

    clienti = []
    for n in nomi:                                      # ciclo su ogni nome
        eta_random = int(np.random.randint(18,70))
        vip_random = bool(np.random.choice([True, False], p=[0.25, 0.75]))
        clienti.append(Cliente(n, eta_random, vip_random))

    return clienti

def simula_prenotazioni(n, clienti, destinazioni):      # crea n prenotazioni simulate
    prezzi = np.random.uniform(200, 2000, size=n)       # array NumPy con prezzi casuali (Parte 3)
    durate = np.random.randint(3, 15, size=n)           # durate 3 - 14 gg

    giorni_possibili = pd.date_range(start="2026-01-01", periods=30, freq="D")
    giorni = np.random.choice(giorni_possibili, size=n)

    prenotazioni = []
    for i in range(n):
        cliente = np.random.choice(clienti)
        destinazione = np.random.choice(destinazioni)
        viaggio = Viaggio(destinazione, float(prezzi[i]), int(durate[i]))
        prenotazione = Prenotazione(cliente, viaggio, pd.Timestamp(giorni[i]))
        prenotazioni.append(prenotazione)


    return prenotazioni, prezzi

def prenotazioni_to_dataframe(prenotazioni):            # Convertiamo oggetti in DataFrame (Parte 4).
    righe = []
    for p in prenotazioni:
        righe.append(                                   # Costruiamo la riga con colonne richieste: Cliente/Destinazione/Prezzo/Giorno/Durata/Incasso
            {
                "Cliente" : p.cliente.nome,
                "Destinazione" : p.viaggio.destinazione, 
                "Prezzo": p.viaggio.prezzo,
                "Giorno_Partenza": p.giorno_partenza,
                "Durata" : p.viaggio.durata_giorni,
                "Incasso": p.importo_finale()
            }
        )

    return pd.DataFrame(righe)


def main():
    np.random.seed(42)

    cliente_demo = Cliente(nome, eta, vip)
    cliente_demo.stampa_info()
    print("Destinazioni disponibili:", destinazioni)
    print("Prezzi medi:", prezzi_medi)
    print()

    # -------- Simulazione --------
    clienti = genera_clienti()
    prenotazioni, prezzi_array = simula_prenotazioni(100, clienti, destinazioni)

    # --------- Parte 3 ------------
    prezzo_medio = np.mean(prezzi_array)
    prezzo_min = np.min(prezzi_array)
    prezzo_max = np.max(prezzi_array)
    std = np.std(prezzi_array)

    sopra_media= np.sum(prezzi_array > prezzo_medio)
    perc_sopra_media = (sopra_media / len(prezzi_array)) *100

    print("\n === STATISTICHE NUMPY (Prezzi base 200-2000) ===\n")
    print(f"Prezzo medio: {prezzo_medio:.2f}€")
    print(f"Prezzo minimo: {prezzo_min:.2f}€ | Prezzo massimo: {prezzo_max:.2f}€")
    print(f"Deviazione standard: {std:.2f}")
    print(f"% prenotazioni sopra la media: {perc_sopra_media:.2f}%")
    print()

    # -------- Parte 4: Pandas --------
    df = prenotazioni_to_dataframe(prenotazioni)

    incasso_totale = df["Incasso"].sum()
    incasso_medio_dest = df.groupby("Destinazione")["Incasso"].mean().sort_values(ascending=False)
    top3_dest = df["Destinazione"].value_counts().head(3)

    print("=== Analisi Pandas ===")
    print(f"Incasso totale agenzia: {incasso_totale:.2f} €\n " )
    print("Incasso medio per destinazione:\n ")
    print(incasso_medio_dest.round(2), "\n")
    print("Top 3 destinazioni più vendute:\n ")
    print(top3_dest, "\n" )


    df_preview = df.copy()
    df_preview["Prezzo"] = df_preview["Prezzo"].round(2)
    df_preview["Incasso"] = df_preview["Incasso"].round(2)

    print(df_preview.head())



    # -------- Parte 5: Matplotlib --------

    incasso_per_dest = df.groupby("Destinazione")["Incasso"].sum().sort_values(ascending=False)

    plt.figure()
    incasso_per_dest.plot(kind="bar")
    plt.title("Incasso totale per destinazione")
    plt.xlabel("Destinazione")
    plt.ylabel("Incasso (€)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    incasso_giornaliero = df.groupby("Giorno_Partenza")["Incasso"].sum().sort_index()

    plt.figure()
    plt.plot(incasso_giornaliero.index, incasso_giornaliero.values, marker="o")
    plt.title("Andamento giornaliero degli incassi")
    plt.xlabel("Giorno di partenza")
    plt.ylabel("Incasso (€)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    vendite_per_dest = df["Destinazione"].value_counts()

    plt.figure()
    plt.pie(vendite_per_dest.values, labels=vendite_per_dest.index, autopct="%1.1f%%")
    plt.title("Percentuale vendite per destinazione")
    plt.tight_layout()
    plt.show()


    # -------- Parte 6: Analisi Avanzata (categorie) --------
    categorie = {
        "Roma": "Europa",
        "Parigi": "Europa",
        "Tokyo": "Asia",
        "New York": "America",
        "Il Cairo": "Africa",
        "Città del Capo": "Africa"
    }

    df["Categoria"] = df["Destinazione"].map(categorie)

    incasso_per_cat = df.groupby("Categoria")["Incasso"].sum().sort_values(ascending=False)
    durata_media_cat = df.groupby("Categoria")["Durata"].mean().sort_values(ascending=False)

    print("\n === ANALISI PER CATEGORIA ===\n ")
    print("Incasso totale per categoria:\n")
    print(incasso_per_cat.round(2), "\n")
    print("Durata media viaggi per categoria:")
    print(durata_media_cat.round(1), "\n")

    df.to_csv("prenotazioni_analizzate.csv", index=False)
    print("CSV salvato: prenotazioni_analizzate.csv\n")

    # -------- Parte 7: Estensioni --------
    print("=== TOP CLIENTI PER NUMERO PRENOTAZIONI ===")
    print(top_n_clienti(df, 5), "\n")

    incasso_medio_cat = df.groupby("Categoria")["Incasso"].mean()
    durata_media_cat = df.groupby("Categoria")["Durata"].mean()

    categorie_ordinate = incasso_medio_cat.sort_values(ascending=False).index
    incasso_medio_cat = incasso_medio_cat.loc[categorie_ordinate]
    durata_media_cat = durata_media_cat.loc[categorie_ordinate]

    fig, ax1 = plt.subplots()
    ax1.bar(incasso_medio_cat.index, incasso_medio_cat.values)
    ax1.set_title("Incasso medio (barre) + durata media (linea) per categoria")
    ax1.set_xlabel("Categoria")
    ax1.set_ylabel("Incasso medio (€)")
    ax1.tick_params(axis="x", rotation=0)

    ax2 = ax1.twinx()
    ax2.plot(durata_media_cat.index, durata_media_cat.values, marker="o", color="tab:orange")
    ax2.set_ylabel("Durata media (giorni)")

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()

