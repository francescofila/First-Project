# ---- Funzione 'Media' ----

numeri = input("Inserisci una lista di numeri separati da spazio: ")

parti = numeri.split()

print(parti)

valori = [float(x) for x in parti]

def media(valori):
    return sum(valori) / len(valori)

print(media(valori))

