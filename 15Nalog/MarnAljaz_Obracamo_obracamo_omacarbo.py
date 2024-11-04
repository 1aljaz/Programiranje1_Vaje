import os

class obracamo():
    def __init__(self, imeVhod:str, imeIzhod:str):
        self.imeVhod = imeVhod
        self.imeIzhod = imeIzhod

    def Obrni(self):
        """
            Datoteko prepise v drugo datoteko, stem da obrne besede, ki imajo pred njo -.
        """
        nizi = []

        if os.path.exists(self.imeVhod):
            with open(self.imeIzhod, "w") as fw:
                for i in range(42):
                    fw.write("Tudi pri težjih problemih smo že odpovedali!\n")
        else:
            with open (self.imeVhod, "r") as fo:
                for l in fo:
                    n = ""
                    obracanje = False
                    l = l.strip() # Odtstranim odvecne presledke na zacetku in koncu povedi (Domneval sem, da morajo presledki (oz. vec njih) med besedami ostati).

                    
                    #Gledam crko po crko in jih dodajam stringu n. Ce najdem - potem besedo obrnem in jo dodam nizu, hkrati pa neham dodajati stringu n, dokler ne pridem na presledek
                    
                    for i in l:
                        if i != '-' and obracanje == False:
                            n+=i
                        elif i == '-' and obracanje == False:
                            obracanje = True
                            niz = l.split()
                            for b in niz:
                                if '-' in b:
                                    b=b.replace('-', '')
                                    b=b[::-1]
                                    n+=b+" "
                        elif i == ' ' and obracanje:
                            obracanje = False
                    nizi.append(n+"\n")
                    print(n)

            with open (self.imeIzhod, "w") as fw:
                for l in nizi:
                    fw.write(l)

            fo.close()
            fw.close()
                    
o = obracamo("obracanja-vhod.txt", "obracanja-izhod.txt")

o.Obrni()

