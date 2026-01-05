

class Forma:
    def area(self):
        pass

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza


class Cerchio(Forma):
    PI = 3.14

    def __init__(self, r):
        self.r = r

    def area(self):
        return self.PI *(self.r **2)    
        

forme = [Rettangolo(10, 2), Cerchio(3), Rettangolo(4, 5)]
for f in forme:
    print(f"{f.__class__.__name__}: {f.area():.2f}")
