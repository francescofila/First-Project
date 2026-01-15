# ---- Lista → Tupla + indexing ----
print()
giorni_lista = ["lun", "mar", "mer", "gio", "ven" ]

giorni_tupla = tuple(giorni_lista)

print(giorni_tupla)
print()

print("tipo giorni lista", type(giorni_lista))

print("tipo giorni tupla", type(giorni_tupla))

print()

print("Primo elemento: ", giorni_tupla[0])
print()
print("Secondo elemento: ", giorni_tupla[-1])


# ---- Tupla a elemento singolo ----

tupla = (42,)

print(tupla)
print (type(tupla))
print()
x = (42)
print(x)
print(type(x))
print()

# ---- Unpacking di una tupla ----

coordinate = (45.4408, 12.3155)

lat, lon = coordinate


print(f"Latitudine: {lat}, Longitudine: {lon}")
print()


# ---- Immutabilità vs mutabilità ----

numeri = [10, 20, 30]

# sostituzione secondo numero

numeri[1] = 99
print(numeri)

numeri_t = tuple(numeri)

print(numeri_t)

# ---- Slicing misto + conversione ----

numeri = list(range(1, 11))
print("Lista :", numeri)
print()

primi_tre = numeri[:3]
print("Primi tre:", primi_tre)
print()

ultimi_quattro = numeri[-4:]
print("Ultimi quattro:", ultimi_quattro)
print()

uno_si_uno_no = numeri[0::2]
print("Uno sì e uno no:", uno_si_uno_no)
print()

ultimi_quattro_tupla = tuple(ultimi_quattro)
print("Ultimi quattro (tupla):", ultimi_quattro_tupla)
print("Tipo:", type(ultimi_quattro_tupla))
print()

# ---- Tupla di coppie → stringhe leggibili ----

print()

# Esercizio 7

prodotti = [("Prosecco", 10), ("Raboso", 4), ("Manzoni", 12)]

for nome, quantita in prodotti:   # unpack diretto nella for
    print(f"Prodotto: {nome} - Quantità: {quantita}")


# ---- Da tupla a lista + enumerate ----

# Esercizio 8

nomi = ("Anna", "Luca", "Marta")

# 1. Trasforma in lista
nomi_lista = list(nomi)

# 2. Aggiungi un nuovo nome
nomi_lista.append("Francesco")

# 3. Itera con enumerate
for indice, nome in enumerate(nomi_lista, start=1):
    print(f"{indice}. {nome}")

