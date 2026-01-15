

class Animale:
    def __init__(self, nome):
        self.nome = nome

    def verso(self):
        print(f"Il verso di {self.nome} è ")

class Cane(Animale):

    def verso(self):
        print("Bau")

class Gatto(Animale):
    def verso(self):
        print("Miao")

a1 = Cane("Fido")
a2 = Gatto("Mimmo")

print(a1.nome, "fa", end=" ")
a1.verso()

print(a2.nome, "fa:", end=" ")
a2.verso()

# Polimorfismo: stessa funzione, animali diversi
def fai_parlare(animale):
    animale.verso()

animali = [a1, a2, Cane("Rex"), Gatto("Micia")]
for a in animali:
    fai_parlare(a)
