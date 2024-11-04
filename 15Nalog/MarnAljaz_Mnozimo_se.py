def neokrajsan(ime_datoteke:str):
    """
        Iz datoteke preberem ulomke/cela stevila in jih zmnozim z ulomkom. Ce so vrstice napacne (prazne, stringi), po koncu branja izpisem stevilo takih vrstic.
    """

    glavni_stevec = 1
    glavni_imenovalec = 1
    napacne_vrstice = 0
    # Gre cez datoteko vrstico po vrstico in jih ustrezno pretvori v stevilke. Ce najde neustrezno vrstico izpise koliko neustreznih vrstic je v datoteki do te vrstice vkljucno.
    with open(ime_datoteke, "r") as f:
        for l in f:
            try:
                stevec, imenovalec = map(int, l.split("/"))
                glavni_stevec*=stevec
                glavni_imenovalec*=imenovalec
            except:
                try:
                    celo = int(l)
                    glavni_stevec*=celo
                except:
                    napacne_vrstice+=1
                    raise ValueError(f"V datoteki je {napacne_vrstice} napacnih vrstic.")   
    # Ce se slucajno zgodi, da sta stevec in imenovalec v ulomku oba negativna ali pa je imenovalec negativen, oba pomnozim z -1
    if (glavni_stevec < 0 and glavni_imenovalec < 0) or (glavni_stevec > 0 and glavni_imenovalec < 0):
        glavni_imenovalec*=-1
        glavni_stevec*=-1
    return f"{glavni_stevec}/{glavni_imenovalec}"