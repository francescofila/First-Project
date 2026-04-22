
import numpy as np

A = np.arange(1,7).reshape(2,3)
B = np.array([[7 ,8 ,9 ]])
C = np.array([[100], [200]])

print("A: \n", A)
print("B: \n", B)
print("C: \n", C)

# E1) Unisci A e B per righe (risultato (3,3))

E1 = np.concatenate([A, B], axis=0)
print("\n E1 (righe A+B): \n", E1, E1.shape)

# E2) Unisci A e C per colonne (risultato (2,4))
E2 = np.hstack([A,C])
print("\n E2 (colonne A+C):\n ", E2, E2.shape)

# E3) Crea due vettori x e y, poi mettili come colonne in una matrice
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

E3 = np.column_stack([x, y])
print(" \n E3 vettori in matrice:", E3, E3.shape)

# E4) Dividi un vettore in 4 parti uguali

v = np.arange(16)
parts = np.split(v, 4)
print("\n v slplittato in 4 eccolo qui: \n", [p.shape for p in parts], parts)

# E5) Dividi una matrice 4x6 in sinistra/destra (3 colonne + 3 colonne)
M = np.arange(24).reshape(4,6)
left, right = np.hsplit(M,2)

print("\n E5 M.", M)
print("\n left: \n", left)
print("\n right: \n", right)

# E6) Challenge: ricostruisci M usando hstack dei pezzi

M2 = np.hstack([left, right])
print("\nE6 ricostruzione uguale?", np.array_equal(M, M2))

# E7 Maschera: seleziona vini con prezzo >= 16

nomi = np.array(["Bianco", "Rosso", "Orange", "PetNat", "Rosato"])
prezzi = np.array([14.0, 22.0, 18.0, 12.0, 16.5])
punteggi = np.array([86, 91, 88, 84, 90])

mask_prezzo = prezzi >= 16
print("\n E7 nomi:", nomi[mask_prezzo])
print("\n E7 prezzi", prezzi[mask_prezzo])

# E8 Maschera composta: prezzo tra 13 e 19 inclusi

mask_range = (prezzi >=13) & (prezzi <=19)
print("\n E8:", nomi[mask_prezzo], prezzi[mask_prezzo])

# E9 np.where (if vettoriale): crea una categoria prezzo
# - "economico" se < 14
# - "medio" se tra 14 e 19
# - "alto" se >= 19

categoria = np.where(prezzi < 14, "economico",
            np.where(prezzi < 19, "medio", "alto"))
print("\nE3 categoria:", categoria)

# E10 np.where (indici): trova gli indici dei punteggi >= 90
idx_top = np.where(punteggi >=90)
print("\nE10 indici top:", idx_top)
print("\nE10 vini top:",nomi[idx_top], prezzi[idx_top])

# E11 Ordina per prezzo crescente e riordina anche nomi e punteggi
ord_idx = np.argsort(prezzi)
print("\nE5 prezzi ordinati:", prezzi[ord_idx])
print("E5 nomi ordinati:", nomi[ord_idx])
print("E5 punteggi ordinati:", punteggi[ord_idx])

# E12stampa i 2 vini più economici (nome + prezzo)
# TODO: usare argsort e slicing
two_cheapest_idx = ord_idx[:2]
print("\nE6 due più economici:", nomi[two_cheapest_idx], prezzi[two_cheapest_idx])


# ======= RANDOM =======

print("\n ======= RANDOM =======\n")

rng = np.random.default_rng(42)

# E13 Genera 10 numeri uniformi in [0, 1)

u01 = rng.random(10)
print("\n E13 u01:", u01)

# E14 Genera 8 INTERI tra 50 e 101 (50..100) 
intero = rng.integers(50, 101, size=8)
print("\nE14 : 8 numeri interi tra 50 e 100: ", intero)

# E15 Genera 1000 valori normali con media 100 e std 15 (tipo “punteggi”)
scores = rng.normal(loc=100, scale=15, size=1000)
print("\nE15 mean/std:", scores.mean(), scores.std())

# E16 Campiona 3 elementi senza ripetizione da un array 
arr = np.array([10, 20, 30, 40, 50, 60])
sample = rng.choice(arr, size=3, replace=False)
print("\nE4 sample:", sample)

# E17 Mescola arr in-place (ma senza rovinare l’originale: copia!)
arr2 = arr.copy()
rng.shuffle(arr2)
print("\nE5 originale:", arr)
print("E5 mescolato:", arr2)


# E18 Challenge: crea un dataset sintetico 2D (100 righe, 2 colonne)

# col0 ~ uniforme [0, 1) => tutti numeri distribuiti tra = e 1
# col1 ~ normale (0, 1) => numeri a distribuzione gaussiana a media 0 e dev stand 

X0 = rng.random(100)
X1 = rng.normal(0, 1, size=100 )
X = np.column_stack([X0, X1])

print("\n E18 X shape:", X.shape)
print (X)

# E19: prendi 5 righe random di X senza ripetizione (indici)

idx_1 = rng.choice(np.arange(X.shape[0]), size=5, replace=False)
print("\n E19 righe scelte idx:", idx_1)
print(X[idx_1])

# ======= UNFC ========= 
# - UNIVERSAL FUNCTION -

rng = np.random.default_rng(42)

# setup dati random

X2 = rng.normal( loc = 0, scale = 2, size = (4,5))

print("\n X: \n ", X2)
      
# E20) UFUNC: calcola valore assoluto e poi radice dei valori assoluti + 1

A1 = np.abs(X2)

print("\n", A1)

B = np.sqrt(A1 + 1 )
print("\nE1 B:\n", B)

# E21) Broadcasting: centra X sottraendo la media per colonna

mu = X2.mean(axis=0)
X2_centered = X2 - mu

print("\n E20: media colonna dopo centratura (≈0).\n", X2_centered)