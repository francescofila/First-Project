# ---- Verificare se un numero è positivo o negativo ----

num = int(input("Inserisci il tuo numero : "))
print()

if num > 0:
    print("il numero", num , "è positivo.")
elif num < 0: 
    print("Il numero", num, "è negativo.")
else:
    print("Il numero è uguale a 0")


# ---- Maggiore di due numeri ----

print()
a = int(input("Inserisci un numero: "))
print()
b = int(input("Inserisci un altro numero: "))
print()
if a > b:
    print("a maggiore di b.")
elif a <b:
    print ("b maggiore di a.")
else:
    print("i due numeri sono uguali")

# ---- Controllo età ----

print()
eta = int(input("Inserisci la tua età: "))
print()
if eta >= 18:
    print("Sei maggiorenne.")
else:
    print("Sei minorenne.")

# ---- Esercizio 2 – Numero pari o dispari ----

print()

x = int(input("Inserisci un numero intero: "))
print()

if x % 2 == 0:
    print(x, "è un numero pari.")
else:
    print(x, "è dispari.") 
    print()

# ---- Esercizio 3 – Controllo ingresso nel locale (if annidati) ----

print()

eta = int(input("Inserisci la tua età: "))
print()
docu = input("Hai un documento valido? (s/n) : ").lower().strip()
print()

if eta < 18:
    print("Sei minorenne non puoi entrare.")
else:
    if docu == "s":
        print("Accesso consentito.")

    else:
        print("Sei maggiorenne ma senza documento non puoi entrare.") 

print()           


# ---- Esercizio 4 – Sconto sul totale (if + elif + else) ----

print()

basket = round(float(input("Inserisci il totale del carrello: ")), 2)
print()

if basket >= 200:
    sconto = (basket*20)/100
    print("Lo sconto applicato del 20% è pari a:", sconto)
    print()
    print("Il totale finale è: ", basket -sconto "€.")
elif basket >= 100 and basket < 200:
    sconto = (basket*10)/100
    print("Lo sconto applicato del 10% è pari a:", sconto)
    print()
    print("Il totale finale è: ", basket -sconto "€.")
else:
    print ("Non hai diritto a sconto")