class Kvader():
    def __init__(self, visina:int, globina:int, sirina:int):
        # Preverimo validnost vnesenih argumentov
        if visina < 0:
            raise ValueError("Visina mora biti pozitivna.")
        if globina < 0:
            raise ValueError("Globina mora biti pozitivna.")
        if sirina < 0:
            raise ValueError("Sirina mora biti pozitivna")
        
        self._visina = visina
        self._globina = globina
        self._sirina = sirina

    def __mul__(self, x):
        if x <= 0:
            raise ValueError("Ne mores mnoziti s negativnim stevilom.")
        if isinstance(x, (int, float)):
            return Kvader(self._visina * x, self._globina * x, self._sirina * x)
    
    def __rmul__(self, x):
        return self.__mul__(x)
    
    def __str__(self):
        return f"visina = {self._visina}, globina = {self._globina}, sirina = {self._sirina}"

    # Definirani setterji in getterji ter metoda povrsina
    @property
    def visina(self):
        return self._visina
    
    @property
    def globina(self):
        return self._globina

    @property
    def sirina(self):
        return self._sirina
    
    @property
    def povrsina(self):
        """Vrne povrsino kvadrata."""
        return 2*self._globina*self._sirina + 2*self._globina*self._visina + 2*self._visina*self._sirina

    @property
    def ploscina(self):
        """Vrne ploscino osnovne ploskve."""
        return self._globina*self._sirina
    
    @visina.setter
    def visina(self, nova_visina:int):
        if nova_visina < 0:
            raise ValueError("Visina mora biti pozitivna")
        self._visina = nova_visina
    
    @sirina.setter
    def sirina(self, nova_sirina:int):
        if nova_sirina < 0:
            raise ValueError("Sirina mora biti pozitivna")
        self._sirina = nova_sirina
    
    @staticmethod
    def volumen(cls):
        """Vrne volumen razreda podanega kot argument"""
        return cls._visina*cls._globina*cls._sirina

    @classmethod
    def najnizji_kvadrat(cls, kvadrati):
        """Vrne najnizji kvadrat array-ju, ki je podan kot argument"""
        min_visina = min(kvadrat.visina for kvadrat in kvadrati)
        najnizji = next(kvadrat for kvadrat in reversed(kvadrati) if kvadrat.visina == min_visina)
        return cls(najnizji.visina, najnizji.globina, najnizji.sirina)

k = Kvader(5, 2, 3)
k2 = Kvader(10,14,20)
k3 = Kvader(150, 2, 1)
k4 = Kvader(5, 101, 100)

print(k.visina, k.globina, k.sirina)
k.sirina = 2
k.visina = 3
print(k.visina, k.globina, k.sirina, k.povrsina, Kvader.volumen(k), k.ploscina)

print(Kvader.najnizji_kvadrat([k, k2, k3, k4]))