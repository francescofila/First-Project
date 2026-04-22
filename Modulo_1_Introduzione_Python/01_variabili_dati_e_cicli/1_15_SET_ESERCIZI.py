# ---- Studenti due corsi diversi

corso_a = {"Anna", "Luca", "Marco", "Giulia", "Sara", "Paolo"}
corso_b = {"Marco", "Giulia", "Elena", "Davide", "Paolo", "Marta"}

# 1) Chi frequenta entrambi i corsi (intersezione)
entrambi = corso_a & corso_b

# 2) Chi frequenta solo il corso A (differenza)
solo_a = corso_a - corso_b

# 3) Chi frequenta solo il corso B (differenza)
solo_b = corso_b - corso_a

# 4) Chi frequenta almeno un corso (unione)
almeno_uno = corso_a | corso_b

# 5) Quanti studenti unici in totale
totale_unici = len(almeno_uno)

print()

print("Entrambi (A ∩ B):", entrambi)
print()

print("Solo A (A - B):", solo_a)
print()

print("Solo B (B - A):", solo_b)
print()

print("Almeno uno (A ∪ B):", almeno_uno)
print()

print("Totale studenti unici:", totale_unici)
print()

# ---- Intersezione Frigo e Cantina ----

cantina = {
    "Raboso frizzante Asja Rigato",
    "Prosecco Gregoletto",
    "Malvasia rifermentata Lusenti",
    "Franciacorta Ca' dai Pazzi",
    "Bidon Bidon (Fora Wines)",
    "Trebbiano macerato (Orange)"
}

frigo_mescita = {
    "Prosecco Gregoletto",
    "Malvasia rifermentata Lusenti",
    "Rosato di Sangiovese",
    "Trebbiano macerato (Orange)",
    "Metodo classico Rosé",
    "Sidro secco"
}

# 1) In entrambi: già in cantina + già pronto in frigo (intersezione)
entrambi = cantina & frigo_mescita

# 2) Solo in cantina: disponibili ma NON pronti al servizio (differenza)
solo_cantina = cantina - frigo_mescita

# 3) Solo in frigo: presenti in frigo ma NON risultano in cantina (anomalia/inventario da controllare)
solo_frigo = frigo_mescita - cantina

# 4) Almeno uno dei due: tutto ciò che "esiste da qualche parte" (unione)
almeno_uno = cantina | frigo_mescita

# 5) Totale etichette uniche complessive
totale_uniche = len(almeno_uno)

print("✅ Presenti sia in cantina che in frigo:", sorted(entrambi))
print()
print("📦 Solo in cantina (da raffreddare/spostare):", sorted(solo_cantina))
print()
print("⚠️ Solo in frigo (da verificare inventario):", sorted(solo_frigo))
print()
print("🧾 Tutte le etichette presenti almeno in uno:", sorted(almeno_uno))
print()
print("🔢 Totale etichette uniche:", totale_uniche)


print(
    f"✅ Presenti sia in cantina che in frigo: {sorted(entrambi)}\n\n"
    f"📦 Solo in cantina (da raffreddare/spostare): {sorted(solo_cantina)}\n\n"
    f"⚠️ Solo in frigo (da verificare inventario): {sorted(solo_frigo)}\n\n"
    f"🧾 Tutte le etichette presenti almeno in uno: {sorted(almeno_uno)}\n\n"
    f"🔢 Totale etichette uniche: {totale_uniche}"
)