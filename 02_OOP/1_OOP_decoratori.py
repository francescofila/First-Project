class Studente:
    ANNO_CORRENTE = 2026  # costante di classe

    def __init__(self, nome, eta, corso):
        self.nome = nome 
        self.eta = eta      # passa dal setter
        self.corso = corso 

    @classmethod
    def from_string(cls, s):
        nome, eta, corso = s.split("-")
        return cls(nome, int(eta), corso)

    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, valore):
        self._eta = valore

    @property
    def anno_nascita(self):
        return self.ANNO_CORRENTE - self.eta


# --- test ---
s = Studente.from_string("Luca-20-Matematica")
print(s.nome, s.eta, s.corso)        # Luca 20 Matematica
print(s.anno_nascita)                # 2006 (se ANNO_CORRENTE=2026)

