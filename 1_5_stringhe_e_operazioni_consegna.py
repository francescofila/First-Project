# Esercizio 1 ---- Chiedi una frase e inverti l'ordine delle parole ----
    #     Frase = Oggi studio python con Epicode
print()
frase = input ("inserisci qui la tua frase: ")
print()

parole = frase.split()
print(parole)

parole_invertite = parole [::-1]

frase_invertita = " ".join(parole_invertite)

print()
print(frase_invertita)
print()


# Esercizio 2 ---- Controllare che la frase non è un palindromo ----

print()
frase_pulita = frase.lower().replace(" ","")
print(frase_pulita)
print()

frase_invertita_pali = frase_pulita[::-1]
print(frase_invertita_pali)

# Confronto
if frase_pulita == frase_invertita_pali:
    print("La frase è un palindromo.")
else:
    print("La frase NON è un palindromo.")







