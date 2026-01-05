
import math

class Frazione:
    def __init__(self, numeratore, denominatore):
        if denominatore == 0:
            raise ValueError("Il denominatore non può essere zero.")
        self.n = numeratore
        self.d = denominatore
        self._semplifica()
        
    def __str__(self):
        return f"{self.n}/{self.d}"
    
    def __add__(self, altro):
        nuovo_numeratore = self.n * altro.d + altro.n * self.d
        nuovo_denominatore = self.d * altro.d
        return Frazione(nuovo_numeratore, nuovo_denominatore)
    
    def _semplifica(self):
        m = math.gcd(self.n, self.d)
        self.n //= m
        self.d //= m

    def __eq__(self, altro):
        return self.n == altro.n and self.d == altro.d
    
# --- test rapidi come quelli che ti chiederebbero in consegna ---
f1 = Frazione(1, 2)
f2 = Frazione(1, 4)

print(f1)          # 1/2
print(f2)          # 1/4
print(f1 + f2)     # 3/4

print(Frazione(1, 2) == Frazione(2, 4))   # True (perché 2/4 diventa 1/2)
print(Frazione(3, 6) == Frazione(1, 2))   # True

