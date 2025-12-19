# ---- Esercizio 1: Operazioni con i Set ----

a = [1, 2, 3, 5, 5, 9]
b = (4, 5, 6, 7, 8, 9)

set_a = set(a)
set_b = set(b)
print(set_a)
print(set_b)

intersezione = set_a & set_b

print("Intersezione : ", intersezione)
print()

differenza = set_a - set_b

differenza_2 = set_b - set_a

print("Differenza A - B :", differenza)
print()
print("Differenza B - A : ", differenza_2)
print()

unici_totali = len (set_a | set_b)
print("Unici: ", unici_totali)
print()

# ---- Esercizio 2 : Generazione di Numeri Casuali ---- 
# con randint

print()
import random

numeri ={random.randint(1,20) for _ in range (10)}

print ("set casuale", numeri)
print()

# con sample

print("-")

import random
numeri = random.sample(range(1, 21), 10)  # 10 numeri tutti diversi tra 1 e 20

numeri_2 = sorted(random.sample(range(1, 21), 10))
print("Set casuale di 10 numeri:",  numeri_2)
print()


intersezione = set(numeri_2) & set(numeri)
intersezione_ord = sorted(intersezione)

print("Intersezione ordinata:" , intersezione)


# ---- Esercizio 3: Conteggio delle Occorrenze delle Parole ----

frase = "gatto cane gatto pesce cane gatto"

parole = frase.split()
conteggi = {}

for p in parole:
    conteggi[p] = conteggi.get(p, 0) + 1
    pass

print(conteggi)


# ---- Esercizio 4: Inversione di Chiavi e Valori nei Dizionari ----

d = {"a" :1, "b":2, "c":3}

inverso = {v:k for k,v in d.items()}

print(inverso)
print("-")

# ---- Esercizio 5: Creazione di un Dizionario da Due Liste ----


chiavi = ["x", "y", "z"]
valori = [10, 20, 30]

diz = dict(zip(chiavi, valori))

print(diz)
print("-")
# ---- Esercizio 6: Raggruppamento per Lunghezza delle Parole ---- 

parole = ["casa", "sole", "mare", "a", "luna", "pianeta", "re"]

gruppi = {}

for p in parole:
    L = len(p)
    gruppi.setdefault(L, []).append(p)

print(gruppi)
print("-")

# ---- Esercizio 7: Frequenza delle Lettere in una Parola ----

print()

parola = "mississipi"

freq = {}

for ch in parola:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)



