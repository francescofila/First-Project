# ---- Esercizio 1 – Maggiorenne in città ----
print()

nome = input("Buongiorno, inserisci qui il tuo nome: ")
print()

eta = input("Ora inserisci la tua età: ")
print()

citta = input("Inserisci ora la città in cui vivi: ")
print()

maggiorenne_a_Roma = (int(eta)>=18) and (citta == "Roma") 

print(maggiorenne_a_Roma)
print()

if maggiorenne_a_Roma:
        print("Accesso contensito.")
else :
        print("Accesso negato.")

print()

# ---- 2 – Accesso al sito ----

print()
username_ok = "admin"
password_ok = "Python123"

username = input("Inserire l'username: ")
print()
passsword = input("Inserire la password: ")
print()
login_ok = (username==username_ok) and (passsword==password_ok)

if login_ok:
       print("Login effettuato")
else:
       print("Credenziali errate")


# ---- Esercizio 3 – Divisione sicura (short-circuit con and) ----

print()
num = int(input("Inserisci il numeratore della divisione: "))
divisore = int(input("Inserisci il divisore della divisiione: "))
print()

print()
divisione_valida = (divisore !=0) and (num/divisore >1)

print("Divisione valida?", divisione_valida)
print()

if divisione_valida:
        risultato = num / divisore
        print("Risultato della divisione: ", risultato)
else:
        print("Divisione non valida")
print()


# ---- Esercizio 4 – Campi obbligatori (truthy/falsy) ----

print()
nome = input("Inserisci il tuo nome: ")
email = input("Inserisci la tua email: ")

nome_valido = bool (nome)
email_valida = bool (email)

form_valido = nome_valido and email_valida

print()
print("nome_valido: ", nome_valido)
print("email_valida: ", email_valida)
print("form_valido: ", form_valido)
print()

if not nome_valido and not email_valida :
        print("Nome ed email mancanti")

elif not email_valida :
        print("Email mancante")

elif not nome_valido: 
        print("Nome mancante")

else:
        print("Accesso completato")        


print()
print()

# ---- Esercizio 5 – Ingredienti disponibili ( in ) ----

print()
lista_spesa = input("Scivi qui la tua lista della spesa: ")
print()

Lista_ingredienti = lista_spesa.lower().split()
print(Lista_ingredienti)
print()

ingrediente = input("Inserisci un ingrediente: ").lower()
print()

print (ingrediente in Lista_ingredienti)

if ingrediente in Lista_ingredienti:
        print ("ingrediente disponiblile")
else:
        print("Ingrediente non disponibile")
print()

# ---- Esercizio 6 – is e None ----
print()

codice_sconto = None

rischiesta_codice = input("Hai un codice sconto? (s/n)")
print()

if rischiesta_codice == "s":
        codice_sconto = input("Inserisci il tuo codice: ")
print()

if codice_sconto is None:
        print("Nessun codice inserito")
else:
        print("Hai inserito il codice: ", codice_sconto)   

        # ---- Esercizio 7 – Allenamento con not, and, or - Cinema Gratis ----

print()

eta = int(input("Benvenuto al cinema Python! Inserisci la tua età: "))

richiesta_tessera = input("Hai la tessera studente? (s/n)").lower()
print()


studente = richiesta_tessera == "s"

entra_gratis = (studente) or (eta < 10) or (eta > 65)

if entra_gratis:
        print("\"Ingresse gratutio\"")
else:
        print("\"Devi pagare il biglietto\"")

print()
     