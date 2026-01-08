    # Versione A - con None, creo ogetto vuoto e poi lo riempio.

class StudenteA:
    def __init__(self, nome: str | None = None, eta: int | None = None):
        self.nome = nome
        self.eta = eta

    
        # Input da utente: riempie gli attributi dell'oggetto
    def chiedi_dati(self) -> None:
        self.nome = input("Inserisci il tuo nome: ").strip()

        while True:
            testo = input("Inserisci la tua eta: ").strip()
            try:
                self.eta = int(testo)
                break
            except ValueError:
                print("Inserisci un numero intero")

        #  Output: stampa una frase usando lo stato dell'oggetto
    def presentati(self) -> None:
        if self.nome is None or self.eta is None:
            print("Dati mancanti: prima chiama chiedi_dati().")
            return
        
        print(f"Ciano, sono {self.nome} e ho {self.eta} anni.")


if __name__ == "__main__":
    s = StudenteA()
    s.chiedi_dati()
    s.presentati()



    # Versione B - cre l'oggetto già completo

class StudenteB:
    def __init__(self, nome :str, eta :int):
        self.nome = nome
        self.eta = eta

    def presentati(self):
        print(f"Ciao sono {self.nome} e ho {self.eta} anni.")

nome = input("Nome: ").strip()

while True:
    try:
        eta = int(input("Età: ").strip())
        break
    except ValueError:
        print("Età non valida, devi inserire un nuomero intero")

s = StudenteB(nome, eta)
s.presentati()



# Versione C - OOP + metodo stringa

class StudenteC:
    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta = eta


    @classmethod
    def da_input(cls):
        nome = input("Nome: ").strip()

        while True:
            try:
                eta = int(input("Inserisci la tua età: ").strip())
                return cls(nome, eta) # creazione dell'oggetto
            except ValueError:
                print("Età non valida, inserisci un numero intero.")

    def presentati(self):
        print(f"Ciao sono {self.nome} e ho {self.eta} anni.")

    def __str__(self):
        return f"Studente(nome={self.nome}, eta={self.eta})"
    

# --- uso ---
s = StudenteC.da_input()
s.presentati()
print(s)

class Diario:
    def __init__ (self, nome_file="diario.txt"):
        self.nome_file = nome_file

    def salva_messaggio_da_utente(self):
        messaggio = input("Scrivi un messaggio da salvere sul diario: ").strip()
        if not messaggio:
            print("Messaggio vuoto, nulla da salvare")
            return
        
        with open(self.nome_file, "a") as f:
            f.write(messaggio + "\n")

        print("Messaggio salvato")

if __name__ == "__main__":
    d = Diario("diario.txt")
    d.salva_messaggio_da_utente()