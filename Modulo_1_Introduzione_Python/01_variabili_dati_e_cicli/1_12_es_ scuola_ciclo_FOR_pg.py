# Stampa dei Numeri da 1 a 10
print()
for i in range (1 , 11):
    print(i)

print()

# Stampa dei Numeri Pari da 1 a 20

print()

for i in range (2, 21, 2):
    print (i)
print()

# Stampa di Ogni Lettera di una Parola
print()

parola = "francesco"

for c in parola:
    print(c)

print()

for x in parola:
    print (x)
print()

# Esrcizio 4 Somma dei Numeri da 1 a 100


print()
somma = 0 

for i in range (1, 101):
    somma += i

print (f"La somma dai numeri da 1 a 100 è : {somma}.")
print()

# Stampa della Tabellina del 3

for i in range (1, 11):
    print(f"3 x {i} è uguale a {3 * i}" )

print()

# Calcolo del Fattoriale di un Numero

n = 5
fattoriale = 1
for i in range(1, n+1):
    fattoriale = fattoriale * i

print (f"Il fattoriale di {n} è : {fattoriale} ")

# Conteggio delle Vocali in una Parola

parola = "Francesco"

vocali = "aeiou"
conta = 0

for x in parola:
    if x in vocali:
        conta +=1

print (conta)

# Stampa Matrice

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for riga in matrice:
    for elemento in riga:
        print(elemento, end=" ")
    print()

# Stampare i numeri da 1 a 10 saltando il 5 con if e continue.
print()

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print()

# Stampare i numeri da 1 a 10 e fermarsi al 7 includendo il 7 con if e break

print()

for i in range(1, 11):
    if i == 8:
        break
    print(i)

print()


# ---- Stampa lista nomi  con ordine, con enumerate ----
nomi = ["Alice", "Bob", "Carlo", "Diana"]

for i in range(len(nomi)):
    numero_ordine = i + 1          # perché i parte da 0
    nome = nomi[i]                 # prendo l'i-esimo elemento
    print(f"{numero_ordine}. {nome}")



print()
print()

for numero_ordine, nome in enumerate(nomi, start=1):
    print(f"{numero_ordine}. {nome}")

print()
print()

# ---- Stampa lista con ordine ----

lista = ["edu", "comp", "eco", "care"]

for i in range(len(lista)):
    numero_ordine = i +1 
    nome = lista[i]

    print(f"{numero_ordine} , {nome} ")






# ---- Matrice Prodotti x Giorni e somma


prodotti = ["Prosecco", "Raboso", "Manzoni"]
giorni = ["Lun", "Mar", "Mer"]

giacenze = [
    [10, 8, 6],   # Prosecco
    [4, 3, 2],    # Raboso
    [12, 11, 9]   # Manzoni
]

w_prod = 10      # larghezza colonna "Prodotto"
w_num = 8        # larghezza numeri (giacenze)

print(f"{'Prodotto':<{w_prod}}", end="")

for g in giorni:
    print(f"{g:>{w_num}}", end="")

print(f"{'Totale':>{w_num}}")  # colonna totale prodotto


for nome_prodotto, riga in zip(prodotti, giacenze):
    print(f"{nome_prodotto:<{w_prod}}", end="")

    totale_prodotto = 0

    for qta in riga:
        print(f"{qta:>{w_num}}", end="")
        totale_prodotto += qta

    print(f"{totale_prodotto:>{w_num}}")

print("-" * (w_prod + w_num * (len(giorni) + 1)))  # linea di separazione

print(f"{'Tot Giorno':<{w_prod}}", end="")

for col in range(len(giorni)):
    somma_colonna = 0
    for riga in giacenze:
        somma_colonna += riga[col]
    print(f"{somma_colonna:>{w_num}}", end="")

# Totale generale
totale_generale = sum(sum(riga) for riga in giacenze)
print(f"{totale_generale:>{w_num}}")
