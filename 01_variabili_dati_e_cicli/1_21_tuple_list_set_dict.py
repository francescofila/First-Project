# ---- TUPLE ----
# ---- 1  -  Ordinare una lista di tuple ----
print()

vini = [("Raboso", 16), ("Prosecco", 8), ("Manzoni", 12), ("Tai", 10)]

ordinati = sorted(vini, key=lambda x: x[1] )

print(ordinati)
print()

# ---- 2 - Creare una tupla con numeri pari (da una tupla) ----
print()

numeri = [2, 4, 5, 7, 19, 6]

pari = tuple( n for n in numeri if n % 2 == 0)

print(pari)
print()


# ---- 3 - Invertire una tupla (con reversed)) ----
print()

depositi = ("frigo", "cantina", "magazzino")

inverso = tuple(reversed(depositi))

print(inverso)
print()

# ---- 4 - Stringa → tupla di caratteri unici (con set)

codice = "BOTTIGLIA-VENETO"

unici_ordinati = sorted(tuple(set(codice)))

print(unici_ordinati)
print()

# ---- 5 - Zippare due liste in una lista di tuple (zip) ----

print()
etichette = ["Prosecco", "Raboso", "Manzoni"]
qta = [6, 3, 9]

accoppiate = list(zip(etichette, qta))

print(accoppiate)
print()

# ---- Differenza Simmetrica tra Set --- 

a = {1, 2, 3}
b = {3, 4, 5}
c = {5, 6}
differenza = a.symmetric_difference(b).symmetric_difference(c)

differenza_1 = a^b^c
print(differenza_1)
print()
print("Symmetric difference:", differenza)
print()

# ---- 7 Parole uniche in una frase (split + set) ---- 
print()

frase = "vino naturale vino buono naturale"

parole = frase.split()
uniche = set(parole)

print(uniche)

# ---- 8 Unione di set da lista di liste (senza duplicati) ---- 
print()

liste = [
    [1, 2, 2, 3],
    [3, 4],
    [4, 5, 6]
]

unione = set()

for lst in liste:
    # aggiungi tutti gli elementi di lst dentro unione
    pass

print(unione)


# --- oppure ---- 
print()
liste = [[1, 2, 3], [3, 4, 5], [6, 7]]
unione = set.union(*map(set, liste))
print("Union:", unione)
print()

