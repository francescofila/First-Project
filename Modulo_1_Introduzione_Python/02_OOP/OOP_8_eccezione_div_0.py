
class Divisione:
    def dividi(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Errore: divisione per zero non consentita.")
            return None


if __name__ == "__main__":
    d = Divisione()

    print("10 / 2 =", d.dividi(10, 2))
    print("10 / 0 =", d.dividi(10, 0))
