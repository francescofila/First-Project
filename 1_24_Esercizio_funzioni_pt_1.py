rubrica = [] # - creo la lista 'rubrica'

# - creo la funzione 'aggiungi_contatto' dove contatto sarà un dizionario

def aggiungi_contatto(nome, numero, email):  
    contatto = {
        "nome": nome,
        "numero": numero,
        "email": email
    }
    rubrica.append(contatto)
    print()
    print(f"Contatto {nome} aggiunto!")
    print()


aggiungi_contatto("Mario Rossi", "3331234567", "mario@example.com")
aggiungi_contatto("Lucia Bianchi", "3400000000", "lucia@example.com")
print(rubrica)

# - creo la funzione 'modifica_contatto' - 

def modifica_contatto(nome, nuovo_numero=None, nuova_email=None):
    for c in rubrica:
        if c ["nome"].lower() == nome.lower():
            if nuovo_numero is not None:
                c["numero"] = nuovo_numero
            if nuova_email is not None:
                c["email"] = nuova_email

            print(f"Contatto {nome} modificato !")   
            return
    print()
    print("Contatto non trovato.")

# --- mini test ---


modifica_contatto("mario rossi", nuovo_numero="3339999999")
print(rubrica)


# - creo la funzione 'elimina contatto' - 

def elimina_contatto (nome):
    for c in rubrica:
        if c["nome"].lower().strip() == nome.lower().strip():
            rubrica.remove(c)
            print(f'Contatto {nome} rimosso.')
            return
    
    print("Contatto non trovato.")


# - mini test -


elimina_contatto("lucia bianchi")
print(rubrica)


# - funzione cerca contatto -
print()

def cerca_contatto(nome):
    for c in rubrica:
        if c["nome"].lower().strip() == nome.lower().strip():
            # stampa dizionario
            print("Contatto trovato", c )
            print()
            # stampa pulita
            print(f"Nome: {c['nome']}")
            print(f"Numnero: {c['numero']}") 
            print(f"Email: {c['email']}")
            return
    print("Contatto non trovato.")

cerca_contatto("mario rossi")
cerca_contatto("lucia bianchi")

# - funzione mostra - 

def mostra_contatti():
    if not rubrica:
        print("Rubrica vuota!")
        return
    
    ordinati = sorted(rubrica, key=lambda x: x["nome"].lower())

    for c in ordinati:
        print(f"{c['nome']} - {c['numero']} - {c['email']}")


mostra_contatti()
