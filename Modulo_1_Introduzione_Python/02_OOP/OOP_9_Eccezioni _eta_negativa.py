class Persona:
    def __init__(self, nome, eta):
        if eta < 0:
            raise ValueError("L'età non può essere negativa")
        self.nome = nome
        self.eta = eta

    def __str__(self):
        return f"{self.nome} ({self.eta} anni)"
    


if __name__ =="__main__":
    try:
        p1 = Persona("Mario", 25)
        print("ok", p1)

        p2 = Persona("Anna", -3)
        print("ok", p2)
    except ValueError as e :
        print("Errore", e )