import numpy as np

# =========================
# PARTE 1 — Variabili base
# =========================

nome1 = "Mario"
cognome1 = "Rossi"
codice_fiscale1 = "RSSMRA80A01H501U"
eta1 = 45
peso1 = 78.5
analisi1 = ["emocromo", "glicemia", "colesterolo"]

nome2 = "Giulia"
cognome2 = "Bianchi"
codice_fiscale2 = "BNCGLI92C41F205Z"
eta2 = 33
peso2 = 61.2
analisi2 = ["glicemia", "trigliceridi", "creatinina"]

nome3 = "Luca"
cognome3 = "Verdi"
codice_fiscale3 = "VRDLCU75D15L736X"
eta3 = 50
peso3 = 84.0
analisi3 = ["colesterolo", "emocromo", "creatinina"]


# Range "inventati ma sensati" per valutare normalità (semplificazioni didattiche)
RANGE_NORMALI = {
    "glicemia": (70, 99),          # mg/dL (digiuno, semplificato)
    "colesterolo": (125, 200),     # mg/dL (totale, semplificato)
    "trigliceridi": (0, 150),      # mg/dL
    "emocromo": (12.0, 17.5),      # g/dL (interpretiamo "emocromo" = emoglobina)
    "creatinina": (0.6, 1.3),      # mg/dL
}


class Analisi:
    def __init__(self, tipo, risultato):
        self.tipo = str(tipo)
        self.risultato = float(risultato)

    def valuta(self):
        if self.tipo not in RANGE_NORMALI:
            return "N/D (range non definito)"
        minimo, massimo = RANGE_NORMALI[self.tipo]
        if self.risultato < minimo:
            return "FUORI NORMA (troppo basso)"
        if self.risultato > massimo:
            return "FUORI NORMA (troppo alto)"
        return "OK (nella norma)"


class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso):
        self.nome = str(nome)
        self.cognome = str(cognome)
        self.codice_fiscale = str(codice_fiscale)
        self.eta = int(eta)
        self.peso = float(peso)

        self.analisi_effettuate = []
        self.risultati_analisi = np.array([], dtype=float)

    def scheda_personale(self):
        return (
            f"Paziente: {self.nome} {self.cognome} | CF: {self.codice_fiscale} | "
            f"Età: {self.eta} | Peso: {self.peso:.1f} kg | "
            f"Analisi: {', '.join(self.analisi_effettuate) if self.analisi_effettuate else '—'}"
        )

    def aggiungi_analisi(self, analisi_obj):
        self.analisi_effettuate.append(analisi_obj.tipo)
        self.risultati_analisi = np.append(self.risultati_analisi, analisi_obj.risultato)

    def statistiche_analisi(self):
        if self.risultati_analisi.size == 0:
            return {"media": None, "minimo": None, "massimo": None, "deviazione_std": None}

        return {
            "media": float(np.mean(self.risultati_analisi)),
            "minimo": float(np.min(self.risultati_analisi)),
            "massimo": float(np.max(self.risultati_analisi)),
            "deviazione_std": float(np.std(self.risultati_analisi)),
        }

    def riepilogo_analisi(self):
        """
        Stampa (tipo -> valore -> OK/FUORI NORMA).
        Ricostruiamo oggetti Analisi usando l’allineamento:
        analisi_effettuate[i] <-> risultati_analisi[i]
        """
        righe = []
        for i in range(len(self.analisi_effettuate)):
            tipo = self.analisi_effettuate[i]
            valore = float(self.risultati_analisi[i])
            a = Analisi(tipo, valore)
            righe.append(f"- {tipo}: {valore} -> {a.valuta()}")
        return "\n".join(righe) if righe else "—"


class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = str(nome)
        self.cognome = str(cognome)
        self.specializzazione = str(specializzazione)

    def visita_paziente(self, paziente):
        print(f"Il Dr. {self.nome} {self.cognome} ({self.specializzazione}) visita {paziente.nome} {paziente.cognome}")


def statistiche_campione(valori):
    arr = np.array(valori, dtype=float)
    return {
        "media": float(np.mean(arr)),
        "massimo": float(np.max(arr)),
        "minimo": float(np.min(arr)),
        "deviazione_std": float(np.std(arr)),
    }


def main():
    # 3 medici
    medici = [
        Medico("Elena", "Sarti", "Medicina Interna"),
        Medico("Paolo", "Neri", "Endocrinologia"),
        Medico("Chiara", "Fabbri", "Cardiologia"),
    ]

    # 5 pazienti
    pazienti = [
        Paziente(nome1, cognome1, codice_fiscale1, eta1, peso1),
        Paziente(nome2, cognome2, codice_fiscale2, eta2, peso2),
        Paziente(nome3, cognome3, codice_fiscale3, eta3, peso3),
        Paziente("Sara", "Conti", "CNTSRA88E60H501K", 37, 59.8),
        Paziente("Davide", "Gallo", "GLLDVD90H12F205Q", 35, 74.3),
    ]

    # Ogni paziente: almeno 3 risultati
    dati_analisi = [
        [Analisi("emocromo", 13.4), Analisi("glicemia", 92), Analisi("colesterolo", 185)],
        [Analisi("glicemia", 104), Analisi("trigliceridi", 140), Analisi("creatinina", 1.0)],
        [Analisi("colesterolo", 215), Analisi("emocromo", 11.6), Analisi("creatinina", 1.2)],
        [Analisi("glicemia", 88), Analisi("colesterolo", 172), Analisi("trigliceridi", 165)],
        [Analisi("creatinina", 1.4), Analisi("emocromo", 15.1), Analisi("glicemia", 79)],
    ]

    for p, lista in zip(pazienti, dati_analisi):
        for a in lista:
            p.aggiungi_analisi(a)

    # PARTE 3: stesso esame su 10 pazienti (esempio: glicemia)
    glicemie_10 = [92, 88, 101, 76, 85, 97, 110, 90, 83, 95]
    stats_glicemia = statistiche_campione(glicemie_10)

    print("\n=== STATISTICHE CAMPIONE (glicemia su 10 pazienti) ===")
    print(
        f"Media: {stats_glicemia['media']:.2f} | "
        f"Min: {stats_glicemia['minimo']:.2f} | "
        f"Max: {stats_glicemia['massimo']:.2f} | "
        f"Std: {stats_glicemia['deviazione_std']:.2f}"
    )

    # 1) scheda pazienti
    print("\n=== SCHEDE PAZIENTI ===")
    for p in pazienti:
        print(p.scheda_personale())
        print("Valutazioni:")
        print(p.riepilogo_analisi())
        print()

    # 2) visite medico -> paziente (round-robin)
    print("\n=== VISITE ===")
    for i, p in enumerate(pazienti):
        medico = medici[i % len(medici)]
        medico.visita_paziente(p)

    # 3) statistiche per paziente
    print("\n=== STATISTICHE ANALISI PER PAZIENTE ===")
    for p in pazienti:
        s = p.statistiche_analisi()
        print(f"{p.nome} {p.cognome}: "
              f"media={s['media']:.2f}, min={s['minimo']:.2f}, max={s['massimo']:.2f}, std={s['deviazione_std']:.2f}")


if __name__ == "__main__":
    main()
