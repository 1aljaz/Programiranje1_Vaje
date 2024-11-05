import os

def Obrni(imeVhod:str, imeIzhod:str):
    """
        Datoteko prepise v drugo datoteko, stem da obrne besede, ki imajo pred njo -.
    """
    nizi = []
    if not os.path.exists(imeVhod):
        with open(imeIzhod, "w") as fw:
            for i in range(42):
                fw.write("Tudi pri težjih problemih smo že odpovedali!\n")
    else:
        with open (imeVhod, "r") as fo:
            with open(imeIzhod, "w") as fw:
                for l in fo:
                    nizi = l.strip().split(' ') # Odtstranim odvecne presledke na zacetku in koncu povedi (Domneval sem, da morajo presledki (oz. vec njih) med besedami ostati).
                    for n in nizi:
                        if n[:1] == '-':
                            n = n[1:]    
                        fw.write(n+" ")
                    fw.write("\n")
        fo.close()
        fw.close()
                    
Obrni("15Nalog/obracanja-vhod.txt", "15Nalog/obracanja-izhod.txt")



