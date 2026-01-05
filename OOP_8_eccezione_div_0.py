# 02_persona.py

class Persona:
    def __init__(self, nome, eta):
        if eta < 0:
            raise ValueError("L'età non può essere negativa.")
        self.nome = nome
        self.eta = eta

    def __str__(self):
        return f"{self.nome} ({self.eta} anni)"


if __name__ == "__main__":
    try:
        p1 = Persona("Mario", 25)
        print("OK:", p1)

        p2 = Persona("Anna", -3)  # qui scatta l'eccezione
        print("OK:", p2)          # questa riga non verrà eseguita
    except ValueError as e:
        print("Errore:", e)
