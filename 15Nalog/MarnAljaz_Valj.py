import math

class Valj:

    zaokrozitvena_napaka = 2

    def __init__(self, polmer:int, visina:int):
        # Pregledamo validnost argumentov
        if polmer < 0:
            raise ValueError("Polmer mora biti pozitive!")
        if visina < 0:
            raise ValueError("Visina mora biti pozitivna!")
        
        self._polmer = polmer
        self._visina = visina

    def __mul__(self, x):
        if x < 0:
            raise ValueError("Ne mores mnoziti z negativnim stevilom!")
        if isinstance(x, (int, float)):
            return Valj(self._polmer, self._visina*x)
    
    def __str__(self):
        return f"Valj z visino: {self._visina}, in polmerom: {self._polmer}"
    
    def __rmul__(self, x):
        return self.__mul__(x)
    
    # Definirani setterji in getterji ter obseg
    @property
    def polmer(self):
        return self._polmer
    
    @property
    def visina(self):
        return self._visina
    
    @property
    def obseg(self):
        return round(self._polmer*2*math.pi, self.zaokrozitvena_napaka)
    
    @visina.setter
    def visina(self, nova_visina):
        if nova_visina < 0:
            raise ValueError("Nova visina mora biti pozitivna")
        self._visina = nova_visina

    @staticmethod
    def volumen(cls):
        # Vrne volumen zaokrozen na zaokrozitveno napako
        return round(2*math.pi*cls._polmer*cls._visina, cls.zaokrozitvena_napaka)

    @classmethod
    def najnizji_val(cls, valji):
        # Vrne zadnji najnizji valj med podanimi v array-ju
        min_visina = min(valj.visina for valj in valji)
        najnizji = next(valj for valj in reversed(valji) if valj.visina == min_visina)
        return cls(najnizji.polmer, najnizji.visina)
    
    def povrsina(self):
        # Vrne povrsino valja, zaokrozenega na zaokrozitveno napako
        return round(2*math.pi*self._polmer + self._polmer*self._visina, self.zaokrozitvena_napaka)

v = Valj(5, 6)
v1 = Valj(1, 2)
v2 = Valj(10, 100)
v3 = Valj(15, 150)
v4 = Valj(1500, 2)
print(v)
v = v * 2
print(v)

print(Valj.najnizji_val([v, v1, v2, v3, v4]))

print(v.povrsina(),  Valj.volumen(v), v.obseg)
    
