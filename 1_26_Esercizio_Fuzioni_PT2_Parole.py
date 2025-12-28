# ---- Analisi del testo tramite l'implementazione di funzioni ----

# 1 Analizza e pulisci.

def pulisci_testo(testo):
    simboli = ",.;:!?()'"
    for s in simboli:
        testo = testo.replace(s, " ")
    return testo.lower()
    
# 2 Conta Parole

def conta_parole(testo):
    parole = testo.split()
    return len(parole)

# 3 Calcola la frequenza di ogni parola

def frequenza_parole(testo):
    parole = testo.split()
    freq = {}
    for p in parole:
        freq[p] = freq.get(p, 0) +1
    return freq

# 4 Estrarre le parole uniche usando un set

def parole_uniche(freq):
    return set(freq.keys())



def top_n_parole(freq, n =5 ):
    return sorted (freq.items(), key = lambda x: x[1], reverse= True)[:n]


def lunghezza_media(freq):
    tot_caratteri = sum(len(p)* occ for p, occ in freq.items())
    tot_parole = sum(freq.values())
    return tot_caratteri / tot_parole


testo = """Un esempio è stato presentato utilizzando una stringa di testo 
che descrive il linguaggio Python. Il codice implementa le funzioni 
sopra descritte per ripulire il testo, contare le parole, 
calcolare la frequenza e la lunghezza media delle parole, 
e identificare le parole più frequenti."""


# - stampa numero parole
pulito = pulisci_testo(testo)
print ("Il numero di parole è: ", conta_parole(pulito))
print()

# - stampa frenqueza parole
freq = frequenza_parole(pulito)
print("La frequenza delle parole è: ", freq)
print()

# - stampa le parole uniche
print("Le parole uniche sono: ", parole_uniche(freq))
print()

# -stampa le 5 parole più usate
print("Le 5 parole piu usate sono:", top_n_parole(freq))
print()


print("La lunghezza media delle parole è:", round(lunghezza_media(freq), 2))

