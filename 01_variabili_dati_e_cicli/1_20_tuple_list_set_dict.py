# ---- Esercizio 1  - Somma di numeri pari all'interno di una lista ----

print()
numeri = [12, 7, 4, 37, 23, 20, 6]

sommma_pari = sum([ n for n in numeri if n  % 2 ==0 ])

print ("Somma di numeri pari:", sommma_pari)
print()



# ---- Esercizio 2: Creare una lista senza duplicati ----

print()

vini = ["prosecco", "raboso", "nebbiolo", "tairosso",  "prosecco", "manzoni", "prosecco" , "manzoni"]

senza_dup = []

for vino in vini:
    if vino not in senza_dup:
        senza_dup.append(vino)

print(senza_dup)
print()


# ---- Esercizio 3 — Rotazione di una lista di k posizioni a destra (slicing) ----

print()
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k = 3

k = k % len(lista)

print(k)
ruotata = lista[-k:] + lista[:-k]

print("Originale:", lista)
print()
print("Ruotata:", ruotata)
print()

# ----  Esercizio 4 — Intersezione di due liste (senza set) ----

a = [2, 4, 6, 8, 9, 3, 6 ]
b = [1, 1, 3, 6, 8, 9, 7, 10]

intersezione = []

for x in a :
    if x in b and x not in intersezione:
        intersezione.append(x)

print(intersezione)
print()

# ----  Esercizio 5 — Da lista di tuple a dizionario (dict())

dati = [("Frigo", 36), 
        ("Cantina", 60),
        ("Magazzino", 120),
]

dizionario = dict(dati)

print(dizionario)


# ---- Esercizio 6 — Somma di tutte le tuple in una lista di tuple ----

print()
lista_di_tuple = [(3, 5), (4, 7), (5, 4), (3, 7)]

tot = 0 
for t in lista_di_tuple:
    tot += sum(t)
    print(tot)

print(tot)
print()

totale = sum(sum(t) for t in lista_di_tuple)
print(totale)

# ---- Esercizio 7 — Tupla con minimo e massimo di una lista ---- 

print()

valori = [5, 12, 7, 20, 13, 8, 9, 16]

minimo = min(valori)
massimo = max(valori)

min_max = (minimo, massimo)

print(min_max)




