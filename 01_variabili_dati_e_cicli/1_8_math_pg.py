# ---- Esercizio 1 – Calcolo totale spesa con sconto ----

print()
prezzo = float(input("Inserire il prezzo: "))
print()
quantita = int(input("Iserire la quantità acquistata: "))
print()

sconto = float(input("Inserire la percentuale di sconto: "))
print()


tot_lordo = prezzo * quantita
print("Il prezzo totale è: ",tot_lordo)
print()
val_sconto = ((tot_lordo*sconto)/100)

print("Lo sconto totale è: ",val_sconto)
print()

netto = tot_lordo - val_sconto
print("Il prezzo scontato totale è: " , netto)
print()


# ---- Esercizio 2 – Media aritmetica di tre numeri ----
num_1 = float(input("Inserisci primo numero: __"))
print()
num_2 = float(input("Inserisci secondo numero: __"))
print()
num_3 = float(input("Inserisci terzo numero: __"))
print()
media = (num_1 + num_2 + num_3)/3
print("La media è:", media)
print()



# ---- Esercizio 3 – Pari o dispari ----

numero = int(input("Inserire un numero: "))
print()
e_pari = (numero % 2 == 0)

if e_pari:
        print("Il numero", numero, "è pari")
else: 
        print("Il numero", numero, "è dispari")

print()

# ---- Esercizio 4 – Suddividere oggetti in scatole ----

n_oggetti = int(input("Quante penne ci sono? "))
print()
capacita = int(input("Quante penne contiene una scatola? "))
print()

n_scatole = n_oggetti // capacita

disavanzo = n_oggetti % capacita

print("Occorrono", n_scatole, "scatole e avanzeranno", disavanzo, "penne.")
print()

# ---- Esercizio 5 – Velocità media con controllo divisione per zero ----
print()

km = float(input("Quanti kilometri hai percosro? "))
print()
time = float(input("quanto tempo hai impiegato in ore? "))

print()

if time <= 0:
        print("Error! Il tempo non può essere pari a zero") 
else:
        print("hai viaggiato ad una velocità media di", km/time, "kilometri orari.")
print()        

# ---- Esercizio 6 – floor, ceil, trunc tutti insieme ----

import math

numero = float(input("Inseririsci il tuo numero decimale: "))
print()

arr_per_difetto = math.floor(numero)

arr_per_eccesso = math.ceil(numero)

intero = math.trunc(numero)

print("Il tuo numero arrotondato per difetto è ", arr_per_difetto, ".")
print()
print("Il tuo numero arrotondato per eccesso è ", arr_per_eccesso, ".")
print()
print("Il tuo numero arrotondato intero è: ", intero, ".")
print()

# ---- Esercizio 7 – abs vs math.fabs ----

import math

print()
num = int(input("Inserisci un numero intero (anche negativo): "))
print()

val_assoluto_1 = abs(num)        # int
val_assoluto_2 = math.fabs(num)  # float

print("Valore assoluto con abs():", val_assoluto_1, "->", type(val_assoluto_1))
print()
print("Valore assoluto con math.fabs():", val_assoluto_2, "->", type(val_assoluto_2))
print()


# ---- Esercizio 8 – Teorema di Pitagora ---- 

import math
print()

cateto_1 = float(input("Inserisci la misura del primo cateto in cm: "))
print()
cateto_2 = float(input("Inserisci la misura del secondo cateto in cm: "))
print()

ipotenusa = math.sqrt(cateto_1**2 + cateto_2**2)

print(f"L'ipotenusa del triangolo rettangolo è:  {ipotenusa:.3f} cm.")

print()

# ---- Esercizio 9 – Mini calcolatrice (riprendendo l’esempio) ---- 

print()

num_1 = float(input("Inserire il primo dei due numeri: "))
num_2 = float(input("Inserire il secondo dei due numeri: "))

print()

scelta = (input("Seleziona il numero per scegliere l'operazione da effettuare: " \
"  1) Somma" \
"  2) Sottrazione" \
"  3) Moltilicazione" \
"  4) Divisione "))
print()

if scelta == "1":
        print("La somma dei due numeri è: ", num_1 + num_2, )
elif scelta == "2":
        print("La differenza dei due numeri è: ", num_1 - num_2, )
elif scelta == "3":
        print("Il prodotto dei due numeri è: ", num_1 * num_2)
elif scelta == "4":
    if num_2 !=0: 
        print("La divisione dei due numeri è: ", num_1 / num_2)
    else:
          print("la divisione per 0 è impossibile!")    

print()

# ---- Esercizio 10 - Differenza tra due prezzi (con fabs) ---- 

import math
print()

prezzo_oggi = float(input(" Quale è il prezzo di listino di oggi? : "))
print()
prezzo_ieri = float(input(" Quale era il prezzo di listino di ieri? : "))
print()

dif_prezzo = prezzo_oggi - prezzo_ieri
dif_prezzo_abs = math.fabs(dif_prezzo)

print("La variazione è stata di: ", dif_prezzo_abs, "$.")
print()

dif_percentuale = round((dif_prezzo_abs / prezzo_ieri) * 100, 2 )
print("La variaziopne % di prezzo è: ", dif_percentuale, ".")
print()

if dif_prezzo > 0 :
        print("il prezzo è salito del" , dif_percentuale,  "%")
elif dif_prezzo < 0:
        print("Il prezzo è salito del" , dif_percentuale, "%")
else: 
        print(" Il prezzo è lo stesso")


