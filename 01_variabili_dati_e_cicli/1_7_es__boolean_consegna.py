# ---- Esercizio 1 - Può guidare? ----

print()
eta = int(input("Inserisci qua la tua età: "))
print()
patente = input("Hai la patente? : (s/n)").lower().strip()
print()

puo_guidare = eta >= 18 and patente == "s"

print("Può guidare: ", puo_guidare)
print()


if puo_guidare:
        print("Non guidare se hai bevuto.")

else:
        print("Allora non puoi guidare.")

print()

# ---- Esercizio 11 – Ingresso in biblioteca ----

print()

ritardo = input("Sei in ritardo con la consegna libri? (s/n) : ").lower().strip()
print()

premium = input("Hai un abbonamento premium? (s/n) : ").lower().strip()
print()

accesso_consentito = ritardo == "n" or premium == "s"

print("Puo entrare? : ", accesso_consentito)
print()
if accesso_consentito: 
        print("Buona lettura!")
else:
        print("Accesso negato.")