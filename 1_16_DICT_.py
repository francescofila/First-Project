# ---- Esercizio 1 — Rubrica mini ----

# dizionario

rubrica = {
    "Mario Rossi" : "123456",
    "Luigi bianchi" : "654321",
    "Anna Verdi" : "112233"
}

print("Rubrica iniziale:", rubrica)
print() 

# aggiungere un contatto
rubrica["Carla Neri"] = "445566"    
print("Dopo aver aggiunto Carla Neri:", rubrica)
print()

# modificare un contatto
rubrica["Luigi bianchi"] = "999999"  
print("Dopo aver modificato Luigi bianchi:", rubrica)
print()

# eliminare un contatto
del rubrica["Anna Verdi"]      
print("Dopo aver eliminato Anna Verdi:", rubrica)
print()

# cercare un contatto
numero_mario = rubrica.get("Mario Rossi")  
print("Numero di Mario Rossi:", numero_mario)
print()

# stampare tutti i contatti
print("Tutti i contatti nella rubrica:")
for nome, numero in rubrica.items():
    print(f"{nome}: {numero}")
print()

# contare i contatti    
totale_contatti = len(rubrica)  
print("Totale contatti nella rubrica:", totale_contatti)
print()

# chiedi contatto con defoult "non trovato"
contatto_cercato = "Giulia Bianchi"
numero_cercato = rubrica.get(contatto_cercato, "Non trovato")
print(f"Numero di {contatto_cercato}:", numero_cercato)
print() 

  

# ---- Esercizio 2 — Contatore facile (frequenze) ----

# lista di parole       

parole = ["vino", "birra", "acqua", "vino", "succo", "birra", "vino"]

frequenze = {}

for p in parole:
    frequenze[p] = frequenze.get(p, 0) + 1 

print("Frequenze delle parole:", frequenze)

# ---- Esercizio 4 — Filtra con if + items() ----

eta = { "Luca": 17, "Marta": 22, "Giulia" : 18, "Paolo": 15 }

maggiorenni = {}

for nome, anni in eta.items():
    if anni >= 18:
        maggiorenni [nome] = anni


for nome, anni in maggiorenni.items():
    print(f"{nome}: {anni}")
