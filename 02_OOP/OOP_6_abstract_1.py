from abc import ABC, abstractmethod

class Veicolo(ABC):
    @abstractmethod
    def muovi(self):
        pass

class Auto(Veicolo):
    def muovi(self):
        print("L'auto si muove su strada")

class Aeroplano(Veicolo):
    def muovi(self):
        print("L'aeroplano sta volando")

class Bicicletta(Veicolo):
    def muovi(self):
        print("La bicicletta sta pedalando")

class Barca(Veicolo):
    def muovi(self):
        print("La barca sta navigando in mare")


def fai_muovere(veicolo: Veicolo):
    veicolo.muovi()

veicoli = [Auto(), Aeroplano(), Bicicletta(), Barca()]

for v in veicoli:
    fai_muovere(v)
    print()

