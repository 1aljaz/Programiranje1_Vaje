class Dolzina():
    dovoljene_enote = {
        "m" : 1000,
        "dm" : 100,
        "cm" : 10,
        "mm" : 1 
    }


    def __init__(self, koliko: int, enota: str):
        """Konstruktor, ki preveri ce so vhodni podatki vredu. Ce niso sprozi izjemo."""
        if koliko < 0:
            raise ValueError("Dolzina mora biti vecja od 0")

        if enota not in self.dovoljene_enote:
            raise TypeError(f"Enota je lahko samo tipa: m, dm, cm ali mm. Ne pa '{enota}'")

        self._enota = enota
        self._koliko = koliko

    # enota getter
    @property
    def enota(self):
        return self._enota
    #koliko getter
    @property
    def koliko(self):
        return self._koliko

    @koliko.setter
    def koliko(self, koliko):
        if koliko < 0:
            raise ValueError("Kolicina ne more biti negativna")
        self._koliko = koliko

    def __str__(self):
        return f"{self.koliko:.1f} {self.enota}"
    
    def __mul__(self, x):
        # Preveri validnost x-a (ni manjsi od 0 in je celo stevilo ali realno)
        if x < 0:
            raise ValueError("Ne mores mnoziti z negativnim stevilom")
        if isinstance(x, (int, float)):
            return Dolzina(self.koliko*x, self.enota)
    
    def __rmul__(self, x):
        return self.__mul__(x)
    
    def pretvori(self):
        """Pretvori katero koli enoto v mm"""
        return self.koliko * self.dovoljene_enote[self.enota]


    def __lt__(self, other):
        if isinstance(other, Dolzina):
            return self.pretvori() < other.pretvori()

    @classmethod
    def najkrajsa_razdalija(cls, dolzine):
        """Najde najkrajso razdalijo v array-ju podanemu kot parameter"""
        min_razdalija = min(dolzina.pretvori() for dolzina in dolzine)
        najkrajsa =  next(dolzina for dolzina in reversed(dolzine) if dolzina.pretvori() == min_razdalija)
        return cls(najkrajsa.koliko, najkrajsa.enota)

d = Dolzina(100.5, "cm")
d2 = Dolzina(11, "dm")
d3 = Dolzina(1, "m")

print(Dolzina.najkrajsa_razdalija([d, d2, d3]))


