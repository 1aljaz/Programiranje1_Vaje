class sedmica():

    def __init__(self, tab):
        self.tab = tab

    def PoisciVII(self):
        """
            V tabeli poisce sedmice in jih izbrise. Funkcije vrne st. stevil, ki so deljiva s 7 in vsoto tistih, ki niso.
            Predpostavljam, da so v tabeli stevila.
        """
        rez = [0, 0]
        stevec = 0

        # For gre od 0-tega elementa do konca seznama in ce najde stevilo, ki je deljivo s 7 ga zbrise iz podanega seznama in poveca rez[0] za 1, v nasprotnem primeru poveca rez[1] za velikost stevila
        for i in self.tab:
            if i % 7 == 0:
                self.tab.pop(stevec)
                rez[0]+=1
            else:
                rez[1]+=i
            stevec+=1

        print(self.tab)
        return rez

s = sedmica([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17])

print(s.PoisciVII())

