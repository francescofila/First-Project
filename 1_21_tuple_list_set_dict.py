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

# ---- 5 - Zippare due liste in una lista di tuple (zip) ----

etichette = ["Prosecco", "Raboso", "Manzoni"]
qta = [6, 3, 9]

accoppiate = list(zip(etichette, qta))

print(accoppiate)
