class ErroreMagazzino(Exception):
    """Classe base per errori del dominio 'magazzino'."""
    pass



class ProdottoEsauritoError(ErroreMagazzino):
    def __init__(self, nome: str, richiesti: int, disponibili: int):
        super().__init__(
            f"Prodotto esaurito: '{nome}'. Richiesti = {richiesti}, Disponibili = {disponibili}"
        )
        self.nome = nome 
        self.richiesti = richiesti
        self.disponibili = disponibili

class Magazzino:
    def __init__(self):
        self._stock = {}    # dizionario: nome_prodotto -> quantità

    def aggiungi_prodotto(self, nome: str, quantita: int) -> None:
        if quantita <=0:
            raise ValueError("La quantità inserita non puo essere minore o uguale di zero.")
        
        self._stock[nome] = self._stock.get(nome, 0) + quantita

    def rimuovi_prodotto(self, nome: str, quantita: int):
        if quantita <=0:
            raise ValueError("La quantita da rimuovere non puo essere uguale o minore di zero.")
        
        disponibili = self._stock.get(nome, 0)

        if quantita > disponibili:
            raise ProdottoEsauritoError(nome, quantita, disponibili)

        self._stock[nome] = disponibili - quantita

        # opzionale: pulizia se arriva a 0
        if self._stock[nome] == 0:
            del self._stock[nome]

    def __str__(self) -> str:
        return f"Magazzino(stock={self._stock})"            


if __name__ == "__main__":
    m = Magazzino()
    m.aggiungi_prodotto("Vino Bianco", 10)
    m.aggiungi_prodotto("Vino Rosso", 3)

    print("Prima:", m)

    try:
        m.rimuovi_prodotto("Vino Rosso", 2)
        print("Dopo rimozione 2 Vino Rosso:", m)

        m.rimuovi_prodotto("Vino Rosso", 5)  # boom: ProdottoEsauritoError
    except ProdottoEsauritoError as e:
        print("Errore magazzino:", e)
        print("Dettagli:", e.nome, e.richiesti, e.disponibili)
    except ErroreMagazzino as e:
        # qui cattureresti eventuali altri errori di magazzino futuri
        print("Errore magazzino (generico):", e)

    print("Fine:", m)
