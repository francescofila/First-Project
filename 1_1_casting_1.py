# ---- Esercizio Casting ----

# 1. Chiedi all'utente un numero intero
num_intero = int(input("Inserisci un numero intero: "))

# 2. Converti il numero in float e stampalo
num_float = float(num_intero)
print("Lo stesso numero come float è:", num_float)

# 3. Converti il numero in stringa e stampalo insieme a un messaggio
num_stringa = str(num_intero)
print("Hai inserito il numero " + num_stringa)



# ---- Esercizio 1 // conversione numero intero ----

numero_intero_1 = 10

numero_float_1 = float(numero_intero_1)

print (numero_intero_1)
print (numero_float_1)

print (numero_float_1, numero_intero_1)

print (numero_float_1, "//" , numero_intero_1)

# ---- Esercizio 2 // conversione numero decimale (float) ----

numero_float_2 = 9.867

print (int(numero_float_2))


# ---- Esercizio 3 // Conversione string in intero ----

n_stringa = "1234"

x = 1000

somma = x + int(n_stringa)

print (somma)


# ---- Esercizio 4 // Conversione interi e moltiplicazione ----

num_caffe = int(input("Ciao, qunati caffe bevi ogni giorno? " ))

num_giorni = int(input("Quanti gionri ci sono in una settimana? " ))

print ("in una settimana hai bevuto", num_caffe*num_giorni, "caffè.")

# ---- Esercizio 5 // Conversione float e divisione ----

num_chilometri = float(input("Buongiorno, quanti chilometri hai percorso oggi? " ).replace(',', '.'))

num_ore = float(input("In quante ore? " ).replace(',', '.'))

velocita = num_chilometri / num_ore

print("Allora hai camminato alla velocità di", round(velocita, 2) , "km/h.")
