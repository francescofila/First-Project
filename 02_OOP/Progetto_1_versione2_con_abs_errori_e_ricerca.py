"""
PROGETTO: Gestione Biblioteca Digitale (upgrade semplice, SOLO libri cartacei)

Include:
- Parte 1: variabili e tipi di dati
- Parte 2: strutture dati (lista, dict, set)
- Parte 3: OOP con ABC + sottoclasse (LibroCartaceo)
- Parte 4: prestiti con eccezioni + gestione errori (try/except)
- Ricerca parziale da input utente (titolo/autore) che gira quando esegui il file

Nota:
- Docstring (""" """) per spiegare "cosa fa" classi/funzioni.
- Commenti (#) per spiegare "perché" o dettagli operativi.
"""

from abc import ABC, abstractmethod


# -------------------------------------------------------------------
# PARTE 1 — Variabili e tipi di dati
# -------------------------------------------------------------------
titolo = "Il nome della rosa"       # str
copie = 5                           # int
prezzo = 9.90                       # float
disponibile = copie > 0             # bool (True se copie > 0)

print(" -- Parte 1 --")
print("Titolo:", titolo)
print("Copie disponibili:", copie)
print("Prezzo:", prezzo)
print("Disponibile:", disponibile)
print()


# -------------------------------------------------------------------
# PARTE 2 — Strutture dati
# -------------------------------------------------------------------
print(" -- Parte 2 --")

# Lista: collezione ordinata
lista_titoli = [
    "Il nome della rosa",
    "Le città invisibili",
    "Corso intensivo di Python (2ª ed.)",
    "Storytelling con i dati",
    "Logica della scoperta scientifica",
]

# Dizionario: titolo -> copie
copie_per_titolo = {
    "Il nome della rosa": 5,
    "Le città invisibili": 1,
    "Corso intensivo di Python (2ª ed.)": 0,
    "Storytelling con i dati": 2,
    "Logica della scoperta scientifica": 1,
}

# Set: insieme di nomi unici
utenti_registrati = {"Sandro", "Beatrice", "Luca", "Marta"}

print("Lista titoli:", lista_titoli)
print("Dizionario copie:", copie_per_titolo)
print("Set utenti:", utenti_registrati)
print()


# -------------------------------------------------------------------
# PARTE 3 — OOP (ABC + sottoclasse + eccezioni)
# -------------------------------------------------------------------
print(" -- Parte 3 --")


class BibliotecaError(Exception):
    """Eccezione base per tutti gli errori della biblioteca."""
    pass

# queste ereditano da BibliotecaError (ereditano tutti i metodi e proprietà)

class DuplicatoError(BibliotecaError):
    """Elemento duplicato (codice materiale o id utente già presente)."""
    pass


class UtenteNonTrovatoError(BibliotecaError):
    """ID utente non presente nella biblioteca."""
    pass


class MaterialeNonTrovatoError(BibliotecaError):
    """Codice libro non presente nel catalogo."""
    pass


class CopieInsufficientiError(BibliotecaError):
    """Libro non disponibile (copie = 0)."""
    pass


class GiorniNonValidiError(BibliotecaError):
    """Giorni prestito non validi (deve essere int positivo)."""
    pass


class Prestabile(ABC):
    """
    ABC (Abstract Base Class): contratto per oggetti prestabili.
    """

    def __init__(self, codice, titolo, autore, anno):
        self.codice = codice
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

    @property
    @abstractmethod
    def disponibile(self):
        """True/False: prestabile ora?"""
        raise NotImplementedError

    @abstractmethod
    def presta_una_copia(self):
        """Logica prestito (es. decremento copie)."""
        raise NotImplementedError

    @abstractmethod
    def restituisci_una_copia(self):
        """Logica restituzione (es. incremento copie)."""
        raise NotImplementedError

    @abstractmethod
    def info(self):
        """Stringa descrittiva pronta da stampare."""
        raise NotImplementedError


class LibroCartaceo(Prestabile):
    """Libro fisico: disponibile se copie_disponibili > 0."""

    def __init__(self, codice, titolo, autore, anno, copie_disponibili):
        super().__init__(codice, titolo, autore, anno)
        self.copie_disponibili = copie_disponibili

    @property
    def disponibile(self):
        """True se ci sono copie disponibili, False altrimenti."""
        return self.copie_disponibili > 0

    def presta_una_copia(self):
        """Decrementa le copie se possibile, altrimenti solleva un'eccezione."""
        if not self.disponibile:
            raise CopieInsufficientiError(
                f"Copie finite: '{self.titolo}' (codice {self.codice})."
            )
        self.copie_disponibili -= 1

    def restituisci_una_copia(self):
        self.copie_disponibili += 1

    def info(self):
        return (f"[LIBRO] '{self.titolo}' — {self.autore} ({self.anno}) "
                f"| codice={self.codice} | copie={self.copie_disponibili}")


class Utente:
    """Utente registrato alla biblioteca."""

    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        """Stampa una scheda utente."""
        print(f"Utente: {self.nome} | età: {self.eta} | ID: {self.id_utente}")


class Prestito:
    """Collega un utente a un materiale per un certo numero di giorni."""

    def __init__(self, utente, materiale, giorni):
        self.utente = utente
        self.materiale = materiale
        self.giorni = giorni

    def dettagli(self):
        """Stampa dettagli del prestito."""
        print(
            f"Prestito -> Utente: {self.utente.nome} (ID: {self.utente.id_utente}) | "
            f"Libro: {self.materiale.titolo} (codice {self.materiale.codice}) | "
            f"Giorni: {self.giorni}"
        )


class Biblioteca:
    """
    - catalogo: codice -> materiale
    - utenti: id_utente -> utente
    - prestiti: lista prestiti effettuati
     + metodi per registrare, prestare e cercare.
    """

    def __init__(self, nome):
        self.nome = nome
        self.catalogo = {}   # dict: codice -> Materiale
        self.utenti = {}     # dict: id_utente -> Utente
        self.prestiti = []   # list: Prestito

    def aggiungi_materiale(self, materiale):
        """Aggiunge un libro al catalogo. Errore se codice già presente."""
        if materiale.codice in self.catalogo:
            raise DuplicatoError(f"Codice già presente nel catalogo: {materiale.codice}")
        self.catalogo[materiale.codice] = materiale

    def registra_utente(self, utente):
        """Registra un utente. Errore se id già presente."""
        if utente.id_utente in self.utenti:
            raise DuplicatoError(f"ID utente già presente: {utente.id_utente}")
        self.utenti[utente.id_utente] = utente

    def presta(self, id_utente, codice_materiale, giorni):
        """Effettua un prestito con controlli e solleva eccezioni se qualcosa non va."""
        if not isinstance(giorni, int) or giorni <= 0:
            raise GiorniNonValidiError("I giorni devono essere un intero positivo.")

        if id_utente not in self.utenti:
            raise UtenteNonTrovatoError(f"Utente non trovato: {id_utente}")

        if codice_materiale not in self.catalogo:
            raise MaterialeNonTrovatoError(f"Libro non trovato: {codice_materiale}")

        utente = self.utenti[id_utente]
        materiale = self.catalogo[codice_materiale]

        # Polimorfismo (qui sempre LibroCartaceo, ma la biblioteca non lo deve sapere)
        materiale.presta_una_copia()

        prestito = Prestito(utente, materiale, giorni)
        self.prestiti.append(prestito)
        return prestito

    # -------------------------
    # Ricerca parziale (come prima)
    # -------------------------
    def _normalizza(self, testo):
        """
        - casefold: più robusto di lower() per confronto case-insensitive
        - rimuove punteggiatura => spazi
        - collassa spazi multipli
        """
        testo = testo.casefold()
        pulito = []
        for ch in testo:
            if ch.isalnum() or ch.isspace():
                pulito.append(ch)
            else:
                pulito.append(" ")
        return " ".join("".join(pulito).split())

    def cerca(self, query, campo="all"):
        """
        Cerca nel catalogo per match parziale su titolo/autore.
        - query: una o più parole
        - campo: "all" | "titolo" | "autore"
        Regola: tutte le parole (token) devono comparire nel testo normalizzato.
        """
        query_norm = self._normalizza(query)
        if not query_norm:
            return []

        tokens = query_norm.split()
        risultati = []

        for materiale in self.catalogo.values():
            parti = []
            if campo in ("all", "titolo"):
                parti.append(materiale.titolo)
            if campo in ("all", "autore"):
                parti.append(materiale.autore)

            testo_norm: str = self._normalizza(" ".join(parti))
            ok: bool = all(tok in testo_norm for tok in tokens)

            if ok:
                risultati.append(materiale)

        return risultati


# -------------------------------------------------------------------
# PARTE 4 — Esecuzione: setup + prestiti + ricerca da input (GIRA ALL'AVVIO)
# -------------------------------------------------------------------
print(" -- Parte 4 --\n")

biblio = Biblioteca("Biblioteca Digitale — Demo")

# --- Utenti
u1 = Utente("Sandro", 25, "U001")
u2 = Utente("Beatrice", 22, "U002")
u3 = Utente("Luca", 30, "U003")

print("Schede utenti:")
u1.scheda()
u2.scheda()
u3.scheda()
print()

# --- Libri (SOLO cartacei)
m1 = LibroCartaceo("L001", "Il nome della rosa", "Umberto Eco", 1980, copie_disponibili=2)
m2 = LibroCartaceo("L002", "Le città invisibili", "Italo Calvino", 1972, copie_disponibili=1)
m3 = LibroCartaceo("L003", "Corso intensivo di Python (2ª ed.)", "Eric Matthes", 2020, copie_disponibili=0)
m4 = LibroCartaceo("L004", "Storytelling con i dati", "Cole Nussbaumer Knaflic", 2017, copie_disponibili=2)
m5 = LibroCartaceo("L005", "Logica della scoperta scientifica", "Karl Popper", 1934, copie_disponibili=1)

# --- Registrazioni (con gestione errori)
try:
    for u in (u1, u2, u3):
        biblio.registra_utente(u)

    for m in (m1, m2, m3, m4, m5):
        biblio.aggiungi_materiale(m)

except DuplicatoError as e:
    print("ERRORE REGISTRAZIONE:", e)

print("Catalogo iniziale:")
for prest in biblio.catalogo.values():
    print("-", prest.info())
print()

# --- Prestiti: 3 tentativi (uno fallisce per copie=0)
print("Prestiti (con try/except):")
tentativi = [
    ("U001", "L001", 7),   # OK
    ("U002", "L002", 14),  # OK
    ("U003", "L003", 5),   # NO (copie=0)
]

prestiti_ok = []

for idu, cod, gg in tentativi:
    try:
        prestito = biblio.presta(idu, cod, gg)
        prestiti_ok.append(prestito)
        print("OK:", prestito.materiale.titolo)
    except BibliotecaError as e:
        print("NO:", e)

print("\n== COPIE AGGIORNATE ==")
for mat in biblio.catalogo.values():
    print("-", mat.info())

print("\n== DETTAGLI PRESTITI ==")
for p in prestiti_ok:
    p.dettagli()


# -------------------------------------------------------------------
# RICERCA DA INPUT UTENTE (parte interattiva che gira in esecuzione)
# -------------------------------------------------------------------
print("\n== RICERCA (input utente, match parziale) ==")
print("Scrivi una parola o più parole. Esempi: 'rosa', 'popper', 'python', 'dati'")
print("Prefissi: 't:' solo titolo, 'a:' solo autore. Esempi: t: dati   |   a: eco")
print("Invio vuoto per uscire.\n")

while True:
    try:
        q = input("Cerca > ").strip()
    except KeyboardInterrupt:
        # Se premi Ctrl+C, esci pulito senza stacktrace
        print("\nUscita ricerca.")
        break

    if q == "":
        print("Uscita ricerca.")
        break

    campo = "all"
    if q.casefold().startswith("t:"):
        campo = "titolo"
        q = q[2:].strip()
    elif q.casefold().startswith("a:"):
        campo = "autore"
        q = q[2:].strip()

    risultati = biblio.cerca(q, campo=campo)

    if not risultati:
        print("Nessun risultato.\n")
    else:
        print(f"Trovati {len(risultati)} risultati:")
        for r in risultati:
            print("-", r.info())
        print()
