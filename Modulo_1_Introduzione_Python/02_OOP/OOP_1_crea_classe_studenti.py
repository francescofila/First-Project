# ---- Crea una classe Studente con attributi nome e corso ----

class Studente:
    def __init__(self, nome, corso):
        #attributi (stato)
        self.nome = nome
        self.corso = corso 

    # metodo (comportamento)
    def presentati_self(self):
        print(f"Ciao sono {self.nome} e sto seguendo il corso {self.corso}.")


# creazione oggetti (istanze)

s1 = Studente("Francesco", "Python & AI")
s2 = Studente("Gianna", "Python & AI")

s1.presentati_self()

# ---- 2: Generalizzazione (Persona → Studente) ---- 

# - crea una classe persona

class Persona:
    def __init__(self, nome):
        self.nome = nome

    def presentati(self):
        print(f"Ciao, sono {self.nome}.")


class Studente(Persona):
    def __init__(self, nome, corso):
        super().__init__(nome)
        self.corso = corso

    def presentati(self):
        print(f"Ciao, sono {self.nome} e frequento il corso {self.corso}.")


p = Persona("Mick")
p.presentati()  # Ciao, sono Mick.

s = Studente("Mick", "Data Analisi")
s.presentati()  # Ciao, sono Mick e frequento il corso Data Analisi.


# ---- ATTRIBUTI E METODI ----




print()

class Studente:
    # - attributo di classe condiviso
    scuola = "Liceo Classico" 

    def __init__(self, nome):
        self.nome = nome # - attributo di istanza
        

    def presentati(self): # - metodo di istanza
        print(f"Ciao, sono {self.nome} e frequento {Studente.scuola}.")


# - metodo di classe

    @classmethod 
    def cambia_scuola(cls, nuova_scuola):
        cls.scuola = nuova_scuola

# - test

s1 = Studente("Francesco")
s2 = Studente("Mario")

s1.presentati()
s2.presentati()

Studente.cambia_scuola("Liceo Scientifico")

s1.presentati()
s2.presentati()

s1.scuola = "Scuola Segreta"
print(s1.scuola)        # "Scuola Segreta" (istanza)
print(Studente.scuola)  # "Liceo Scientifico" (classe)
print(s2.scuola)        # "Liceo Scientifico" (classe)


# ---- OOP — Istanze, attributi e metodi di istanza ----

