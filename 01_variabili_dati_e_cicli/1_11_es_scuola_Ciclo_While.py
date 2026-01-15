# Esercizio 1: contare da 1 a 5

i = 1

while i <= 5:
    print(i)
    i += 1
print()

# Esercizio 2: Contare numeri pari da 2 a 10

i = 2 

while i <=10:
    print(i)
    i += 2
print()

# Esercizio 3 – Sommare numeri da 1 a 10

i = 1
somma = 0
while i <= 10:
    somma = somma + i
    i += 1

print (f"La somma dei numeri da uno a 10 è {somma}.")
print()

# Esercizio 4 – Tabellina del numero 7

n = 7
i = 1

while i <= 10:
    prodotto = n * i
    print (f"Il prodotto di {n} * {i} è {prodotto}.")
    i += 1 

    print()

# Esercizio 5 – Somma dei numeri inseriti dall’utente    

somma = 0 
num = int(input("Ins numero da sommare (0 per terminare)"))

while num != 0:
    somma = somma + num
    num = int(input("inserisci altro numero o 0 per uscire: "))

print (f"la somma è {somma}")
print()

# Esercizio 6 – Indovinare il numero

tentativo = None
segreto = 31 

while tentativo != segreto:
    tentativo = int(input("inserisci il numero da 0 a 100 indovinare: "))
    print()
    if tentativo < segreto:
        print (f"Il numero {tentativo} è piu piccolo del numero nascosto. ")

    elif tentativo > segreto:
        print(f"Il numero {tentativo} è piu grande del numero nascosto.")

else:
    print("Hai indovinato")

    print()


#  Esercizio 7 – Numeri dispari fino a 15
print()
i = 1

while i <= 15:
    print(i)
    i += 2 

# ---- Esercizio: somma delle cifre di un numero ----

print()
num = int(input("Inserisci un numero intero positivo: "))

somma = 0

# se vuoi essere robusto, consideri anche l'eventuale segno:
num = abs(num)

while num > 0:
    cifra = num % 10      # prendo l'ultima cifra
    somma += cifra        # somma = somma + cifra
    num = num // 10       # tolgo l'ultima cifra al numero

print(f"La somma delle cifre è: {somma}")
