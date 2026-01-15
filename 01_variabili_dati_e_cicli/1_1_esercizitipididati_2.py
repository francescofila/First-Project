# Esercizio #1 - Somma di due numeri da input

a = float(input('Inserisci il primo numero: '))
b = float(input('Inserisci il secondo numero: '))

somma = a+b

print ("La somma dei due numeri é:", somma )

# Esercizio #2 Stampa anno di nascia

nome = input("Buongiorno, come ti chiami? ")

eta = int(input("Ciao "  + nome  +  " quanti anni hai? "))

adn = 2025 - eta #adn -> anno di nascita

print ("Allora", nome, "se hai", eta, "anni, sei nato nel", adn, ".")


# Esercizio 3 – Maggiorenne o no

eta = int(input("Quanti anni hai? "))
maggiorenne = eta >= 18
print("Sei maggiorenne?", maggiorenne)

if maggiorenne:
    print("Puoi entrare a bere")

else: 
    print("Solo patatine per te")