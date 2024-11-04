import random

class Masa():
    # definiramo dovoljene enote in njihovo vrednost v g
    dovoljene_enote = {
        "kg" : 1000,
        "dag" : 10,
        "funt" : 453.592,
        "g" : 1
    }

    zaokrozitvena_napaka = 2

    def __init__(self, kolicina:int, enota:str):
        """
            Preveri validnost vnesenih argumentov
        """
        if enota not in self.dovoljene_enote:
            raise TypeError (f"Enota '{enota}' ni dovoljena. Dovoljene enote so: {list(self.dovoljene_enote)}.")
        
        if kolicina < 0:
            raise ValueError (f"Kolicina mora biti vecja od 0.")

        self._enota = enota
        self._kolicina = kolicina

    def __str__(self):
        return f"{self.kolicina} {self.enota}"
    
    def __add__(self, other):
        return Masa(self.kolicina + other.pretvori_kolicino_v_novo_enoto(self.enota), self.enota)
    
    def __mul__(self, x):
        if x <=0:
            raise ValueError("Ne mores mnoziti s stevilom, manjsim ali enakim 0.")
        if isinstance(x, (int, float)):
            return Masa(self.kolicina * x, self._enota)
    
    def __rmul__(self, x):
        return self.__mul__(x)
    
    def __lt__(self, other):
        if isinstance(other, Masa):
            return self.pretvori_kolicino_v_novo_enoto('g') < other.pretvori_kolicino_v_novo_enoto('g')

    def pretvori_kolicino_v_novo_enoto(self, nova_enota):
        """Pretovri kolicino v katerokoli drugo dovoljeno enoto"""
        return round(self._kolicina * (self.dovoljene_enote[self._enota] / self.dovoljene_enote[nova_enota]), self.zaokrozitvena_napaka)

    # Definirani getterji in setterji
    @property
    def enota(self):
        return self._enota
    
    @property
    def kolicina(self):
        return self._kolicina
    
    @enota.setter
    def enota(self, nova_enota):
        if nova_enota not in self.dovoljene_enote:
           raise TypeError (f"Enota '{nova_enota}' ni dovoljena. Dovoljene enote so: {list(self.dovoljene_enote)}.") 
        
        self._kolicina = self.pretvori_kolicino_v_novo_enoto(nova_enota)
        self._enota = nova_enota
    
    @kolicina.setter
    def kolicina(self, nova_kolicina):
        if nova_kolicina < 0:
            raise ValueError (f"Kolicina mora biti vecja od 0.")
        self._kolicina = nova_kolicina
    
    def faktor(self):
        return round(self.kolicina * self.dovoljene_enote[self.enota], self.zaokrozitvena_napaka)

    @classmethod
    def najvecja_masa(cls, mase):
        najvecja = max(mase, key = lambda masa: masa.pretvori_kolicino_v_novo_enoto("g"))
        return Masa(najvecja.kolicina, najvecja.enota)
    
    @classmethod
    def sestej(cls, mase):
        # sesteje vse mase v array-ju podane kot argument in jih vrne v najpogosteji enoti, ter kot nov objekt tipa cls
        enote = {}
        for masa in mase:
            enota = masa._enota
            try:
                enote[enota] +=1
            except:
                enote[enota] = 1
        skupna_enota = max(enote, key=enote.get)
        sestevek = sum(masa.pretvori_kolicino_v_novo_enoto(skupna_enota) for masa in mase)

        return cls(sestevek, skupna_enota)


# Definiramo dovoljene enote in randomiziramo kolicino in enoto
dovoljene = ["kg", "dag", "funt", "g"]
mase = [Masa(random.randint(1, 1000), dovoljene[random.randint(0, 3)]) for i in range(10)]

# Sestavimo mase in obrnjen array mase
mase = mase + mase[::-1]

print(Masa.sestej(mase))
mase[0] *= 3
print(Masa.sestej(mase))





