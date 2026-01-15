class ErroreScuola (Exception):

    pass


class EtaNonValidaError(ErroreScuola):
    def __init__(self, eta:int):
        super().__init__(f"Età non valida. {eta}.")
        self.eta = eta


class Studente:
    def __init__(self, nome: str, eta: int):
        if eta < 0:
            raise EtaNonValidaError(eta)
        
        self.nome = nome
        self.eta = eta


    def __str__(self) -> str:
        return f"{self.nome} ({self.eta} anni)"

if __name__ == "__main__":
    try:
        s1 = Studente("Luca", 20)
        print("Creato:", s1)

        s2 = Studente("Paolo", -5)  # EtaNonValidaError
        print("Creato:", s2)        # non verrà eseguito
    except EtaNonValidaError as e:
        print("Errore studente:", e)
        print("Età che ha causato l'errore:", e.eta)