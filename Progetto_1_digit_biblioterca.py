# PROGETTO: Gestione Biblioteca Digitale
# Obiettivo: usare variabili, strutture dati, OOP, funzioni, controlli.

# -------------------------
# PARTE 1 — Variabili e tipi di dati

titolo = "Il nome della rosa"       #str
copie = 5                           #int
prezzo = 9.90                       #float
disponibile = copie > 0             #bool

print(" -- Parte 1 --")
print("Titolo: ", titolo)
print("Copie disponibili: ", copie)
print("Disponibile: ", disponibile)
print()

# Parte 2 - Strutture dati

print()
print(" -- Parte 2 --")


#list
lista_titoli = [
    "Il nome della rosa",
    "Logica della scoperta scientifica",
    "Corso intensivo di python",
    "Le cosmicomiche",
    "Manuale operativo per nave spaziale terra"
]

# dict
copie_per_titolo = { "Il nome della rosa": 5,
    "Logica della scoperta scientifica": 3,
    "Corso intensivo di python": 2,
    "Le cosmicomiche": 0,
    "Manuale operativo per nave spaziale terra": 1
}

# set
utenti_registrati = {"Sandro", "Beatrice", "Luca", "Marta"}


# Parte 3 - OOP
print()
print(" -- Parte 3 --")

print("Lista titoli:", lista_titoli)
print("Dizionario copie:", copie_per_titolo)
print("Set utenti:", utenti_registrati)
print()

class Libro:

    def __init__ (self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    @property
    def disponibile(self):
        return self.copie_disponibili > 0

    def info(self):
        return (
            f"' {self.titolo}' di {self.autore} ({self.anno})"
            f" - copie disponibili: {self.copie_disponibili}"
        )


class Utente:
    def __init__ (self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        print(f"Utente: {self.nome} | eta: {self.eta} | ID: {self.id_utente}")

class Prestito:
    def __init__ (self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        print(
            f"Prestito -> Utente: {self.utente.nome} (ID: {self.utente.id_utente}) | "
            f"Libro: {self.libro.titolo} | Giorni: {self.giorni}"
        )

# ---- Parte 4 – Funzionalità | Prestito
print()
print(" -- Parte 4 --")

def presta_libro(utente, libro, giorni):
    # verifica almeno se ha una copia disponibile
    # Se sì → riduca il numero di copie e crei un nuovo oggetto Prestito
    # Se no → stampi un messaggio di errore
    if libro.disponibile:
        libro.copie_disponibili -= 1
        return Prestito(utente, libro, giorni)
    else:
        print(f"ERRORE: '{libro.titolo}' non è disponibile (copie = 0).")

# ---- Simulazione ----

print()
print(" -- Simulazione -- ")

libro1 = Libro("Il nome della rosa", "Umberto Eco", 1980, 2)
libro2 = Libro("Le città invisibili", "Italo Calvino", 1972, 1)
libro3 = Libro("Corso intensivo di python", "Eric Matthes", 2020, 0)


u1 = Utente("Sandro", 25, "U001")
u2 = Utente("Beatrice", 22, "U002")
u3 = Utente("Luca", 30, "U003")

print("Schede utenti")
u1.scheda()
u2.scheda()
u3.scheda()
print()

prestiti = []      #lista vuota dove mettiamo i prestiti

p1 = presta_libro(u1, libro1, 7)
if p1 is not None:
    prestiti.append(p1)

p2 = presta_libro(u2, libro2, 14)
if p2 is not None:
    prestiti.append(p2)

p3 = presta_libro(u3, libro3, 5)   # fallirà: copie = 0
if p3 is not None:
    prestiti.append(p3)


print()
print("== COPIE AGGIORNATE ==")
for libro in [libro1, libro2, libro3]:
    print(libro.info())

print()
print("== DETTAGLI PRESTITI ==")
for p in prestiti:
    p.dettagli()
