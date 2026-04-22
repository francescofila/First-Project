class Appunti: 
    def __init__(self, nome_file = "appunti.txt"):
        self.nome_file = nome_file

    def aggiungi(self, riga: str) -> None:
        riga = riga.strip()

        with open(self.nome_file, "a",) as f:
            f.write(riga + "\n")

    def aggiungi_da_utente(self) -> None:
        riga = input("Scrivi una riga: ")
        if not riga:
            print("Non hai scritto nulla.")
            return
        self.aggiungi(riga)
        print("riga salvata")

    def mostra(self) -> None:
        try:
            with open(self.nome_file, "r") as f:
                contenuto = f.read()

        except FileNotFoundError:
            print("File non trovato")
            return
        
        if contenuto.strip() == "":
            print("File vuoto.")
            return

        print("\n--- APPUNTI ---")
        print(contenuto, end="")  # end="" per non aggiungere righe extra
        print("--------------\n")

        
    def cancella(self) -> None:
        with open(self.nome_file, "w", ) as f:
            pass
        print("File svuotato")

def menu():
    print("\n ---- Appunti ---- ")
    print()
    print("1) Aggiungi riga")
    print("2) Mostra appunti")
    print("3) Cancella file")
    print("0) Esci")

if __name__ == "__main__":
    app = Appunti("appunti.txt")

    while True:
        menu()
        scelta = input("Fai la tua scelta: ").strip()

        if scelta == "1":
            app.aggiungi_da_utente()
        elif scelta == "2":
            app.mostra()
        elif scelta == "3":
            conferma = input("Sei sicuro di svuotare il file? (s/n): ").strip().lower()
            if conferma == "s":
                app.cancella()
            else:
                print("Anullato")
        elif scelta == "0":
            print("Arrivederci")
            break
