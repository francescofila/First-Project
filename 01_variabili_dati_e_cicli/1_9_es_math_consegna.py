# ---- Esercizio Lezione Operazioni Aritmetiche e Matematiche ----


print()

euro = float(input("Quanti euro hai? "))
print()
prezzo = float(input("Quanto costa una birra? "))
print()
birre = euro // prezzo

resto = round(euro % prezzo, 3)

print("Allora puoi comprare", int(birre), "birre.")
print()
print("Devi avere", resto, "euro di resto." )
print() 