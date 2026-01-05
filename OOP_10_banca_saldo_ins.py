class SaldoInsufficienteError(Exception):
    pass

class Banca:
    def __init__(self, saldo_iniziale=0.0):
        if saldo_iniziale < 0:
            raise ValueError ("Il saldo iniziale non può essere negativo.")
        self.saldo = float(saldo_iniziale)

    def preleva(self, importo):
        if importo <=0:
            raise ValueError ("L'importo da prelevare deve essere positivo")
        
        if importo > self.saldo:
            raise SaldoInsufficienteError(
                f"Saldo insufficiente: saldo={self.saldo:.2f}, richiesto={importo:.2f}"
            )
        
        self.saldo -= importo
        return self.saldo
    
    def deposita(self, importo):
        if importo <0:
            raise ValueError("L'importo deposito non può esssere minore di 0.")
        self.saldo += importo
        return self.saldo
    
    def __str__(self):
        return f"Conto(saldo={self.saldo:.2f})"
    
if __name__ == "__main__":
    conto = Banca(100)
    print("Stato iniziale:", conto)

    try:
        print("Prelevo 30 -> saldo:", conto.preleva(30))
        print("Prelevo 90 -> saldo:", conto.preleva(90))  # qui scatta l'eccezione custom
    except SaldoInsufficienteError as e:
        print("Errore banca:", e)
    except ValueError as e:
        print("Errore input:", e)

    print("Stato finale:", conto)
