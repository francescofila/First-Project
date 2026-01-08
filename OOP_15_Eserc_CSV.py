import csv

class GestoreLibri:
    def leggi_libri(self):
        try:
            with open("libri.csv", "r",) as f:
                lettore = csv.DictReader(f, delimiter=";")
                return list(lettore)
        except FileNotFoundError:
            print(f"file non trovato")
            return[]

    def stampa_titoli(self):
        libri = self.leggi_libri()
        for riga in libri:
            print(riga["titolo"])

    def filtra_per_autore(self, autore):
        libri = self.leggi_libri()
        autore = autore.lower().strip()

        risultati = []
        for riga in libri:
            if autore in riga["autore"].lower():
                risultati.append(riga)

        return risultati


if __name__ == "__main__":
    g = GestoreLibri()

    print("=== TITOLI ===")
    g.stampa_titoli()

    chiave = input("\nFiltra per autore: ").strip()
    trovati = g.filtra_per_autore(chiave)

    print("\n=== RISULTATI ===")
    for r in trovati:
        print(f'{r["titolo"]} — {r["autore"]} ({r["anno"]})')
