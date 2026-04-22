#    ---- Esercizio 1 - Crea 3 variabili ----
print()
print()

nome = "Francesco"
eta = 41
citta = "Venezia"
print (nome, eta, citta,)
print()

#    ---- Esercizio 2 - Update di variabili ----

x = 5
print(x)
x=10
print(x)
print()

#    ---- Esercizio 3 - Somma 2 variabili ----

x = 10
y = 6
somma = x+y
print(somma)
print()

#    ---- Esercizio 4 - inversione valori ----

x = 4 
y = 9

x,y = y , x
print(x,y)
print()

#    ---- Esercizio 5 - Calcola area rettango ----

base = 7
altezza = 3
area = base * altezza

print("L'area del rettangolo è: ", area,  " cmq.")
print()

#    ---- Esercizio 6 - Somma interi e decimali ----

a=float(input("Buongiorno, inserica il primo numero a: "))
b=float(input("Ed ora inserisca il secondo numero b: "))
somma = a+b 
print("Allora la somma è:", somma)

#    ---- Esercizio 7 - Calcolare la media di tre numeri ----

x, y, z, = 7, 34, 128
average = ( x+y+z )/ 3 

print ("La media di questi tre numeri è: ", average )
print()


#    ---- Esercizio 8 - Concatenazione di stringhe ----

s1 = "Mi piace leggere"
s2 = "libri di filosofia"

print(s1+s2)
print()

#    ---- Esercizio 9 - Ripetizione di stringhe ----

print("Ciao" * 3)
print()

#    ---- Esercizio 10 - Utilizzo Boolen ----

a = 18
b = 40 
c = 5

print(a < b)
print(b > c) 
print(a < c)  
print()

#    ---- Esercizio 11 - Casting 1.1 ----

x = 13.58

y = int (x)

print(y)
print()

#    ---- Esercizio 12 - Casting 1.2 ----

num ="3000"

k = int(num)

print (k)
print ()



#    ---- Esercizio 13 - Boolean ----

print (bool(10))
print (bool(0))
print (bool(-100))
print (bool(""))