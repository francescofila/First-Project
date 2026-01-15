parola = "Venezia"

print(parola[6])
print()

print (parola[-4])



nome = "Francesco"
frase = "Ciao " + nome + " come stai?"

print(frase)
print()

eta = 40 
text = "La mia età è " + str(eta) + " anni."
print(text)
print()

risata = "ah" * 3 
print(risata)
print()


#    Linea lunga lunga e line tratteggiata

linea = "-" * 30
print(linea)
print()

linea2 = "- " * 15
print(linea2)
print()

# Comando len()

testo = "Francesco"

print(len(testo))
print()

testo2 = "Francesco è qui !"

print(len(testo2))
print()

# Slicing: prendi un pezzo di stringa

parola = "Francesco"

print(parola[-4])
print(parola[0:6])
print(parola[4:])
print()

testox = " Ciao Venezia "

print(testox.upper())
print(testox.lower())
print(testox.capitalize())
print(testox.casefold())
print(testox.replace("Venezia", "Mario"))
print(testox.strip())
print()


# ---- Multilinea 1 ----
print()

testo = """"Questo 
è un testo
su più righe."""

print(testo)
print()

# ---- Multilinea 2 ----

testonml = """"Ciao\nPython"""
print(testonml)
print()


# ---- Tabulazione  ----

print()
x = "Nome"
y = "Cognome"

nome = "Francesco"
cognome = "Fila"

print("x\ty")
print("nome\tcognome")
print()

# ---- Tabulazione  ----

print("Questo è un backslash: \\")

frase = "Lui ha detto: \"ciao\""
print(frase)

print("Il prof ha detto: \"Oggi studiamo le stringhe su Python\".")
print()

# ---- Multilinea e newline  ----

print()
multiriga = """Ciao Epicode,
questo è l'esercizo 
sulle multirighe."""
print()
print(multiriga)
print()


multiriga2 = "Ciao Epicode \nquesto è l'esercizio \nsulle multirighe."
print(multiriga2)

print()

# ---- Multilinea e newline  ----

print()
print("Prodotto\tprezzo")
print("Pane\t1.20 €")
print("Acqua\t2.5 €")
print("Vino\t11.90 €")

print()


# ---- Normalizza input ----

citta = input("Dimmi la tua città: ")

print(citta.lower())
print(citta.strip().capitalize())
print()


# ---- Pulizia frase ----

frase = "    oggi   bevo vIno Naturale  "

print(frase.strip())
print(frase.lower())
print(frase.strip(), frase.lower(),  frase.replace("vIno Naturale", "te verde" ))
print(frase.strip().lower().replace("vino naturale", "te verde.").lstrip())
print()


# ---- Censura parole ----

print()
frase = input("scrivi una frase che contenga la parola cavolo: ")
frase_censurata = frase.replace("cavolo", "****")
print(frase_censurata)
print()

# ---- Nome completo ----

pprint()
nome = input("Buongiorno, inserisci qui il tuo nome: ")
print()
cognome = input("Inserisci qui il tuo congnome: ")
print()
no_co = nome + " " + cognome
no_co_maius = no_co.upper()

print("Buongiorno", no_co_maius, "benvenuto in Python")
print()

print (f"Buongiorno {nome.upper()} {cognome.upper()}, benvenuto in Python. ")
print()

# ---- Risata e separatore ----

print()
risata = "ah" * 8
print (risata)
print()

separatore = "-" *40
print (separatore)
print()



# ---- info su parola ----
print()
parola = input("inserisci una parola di 7 lettere: ")
print()
print(parola)
print()
print(len(parola))
print()
print(parola[0])
print()
print(parola[-1])
print()

# ---- Gioca con python ---- 
print()
parola = "Python"

primo = parola[0]
ultimo= parola[-1]
centrali= parola[1:4]
inverso= parola[::-1]

print(primo)
print(ultimo)
print(centrali)
print(inverso)
print()

