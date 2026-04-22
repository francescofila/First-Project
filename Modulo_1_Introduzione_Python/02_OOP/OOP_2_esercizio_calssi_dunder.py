


print()

class Studente:
    # - attributo di classe condiviso
    scuola = "Liceo Classico" 

    def __init__(self, nome, eta=None):
        self.nome = nome # - attributo di istanza
        self.eta = eta 

    def presentati(self): # - metodo di istanza
        print(f"Ciao, sono {self.nome} e frequento {Studente.scuola}.")

    def introduce_yourself(self):
        print(f"Ciao sono {self.nome} ed ho {self.eta} anni.")


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


# ---- Istanze, attributi, metodi + attributo dinamico “al volo” ----

print()


s3 = Studente("Luca", 22)
s4 = Studente("Anna", 34)

s3.corso = "Python"

print("Il corso di s3 è: ", s3.corso)


