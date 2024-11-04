import os.path as op

def pretvori(imeVhodna:str, imeIzhodna:str):
    """
        Metoda pretvori podatke iz csv v asociaticni seznam. Predpostavljam, da datoteki obstajata.
    """
    headder = []
    h = True
    vrstice = 1

    if not op.isfile(imeVhodna):
        raise FileExistsError(f"Vhodna datoteka z imenom {imeVhodna} ne obstaja.")


    with open(imeVhodna, "r") as fo:
        with open(imeIzhodna, "w") as fw:
            for l in fo:
                vrstice+=1 
                if h: # Sprocesiramo 1. vrstico
                    headder = l.strip().split(',')
                    h = False
                else:
                    asoc = []
                    data = [] 
                    data = l.strip().split(',')
                    if len(data) != len(headder): # ce je vec ali manj elementov v vrstici, vrzemo error
                        raise IndexError(f"Premalo/preveliko elementov v vrstici {vrstice}. z vsebino '{l.strip()}' v datoteki '{imeVhodna}'.")
                    print(data)
                    for i in range(len(headder)): # Zdruzimo elemente v touple
                        asoc.append((headder[i], data[i]))
                    # Naredimo string, v katerega damo vse stvari in ga napisemo v file
                    line = "[ " 
                    for i in asoc:
                        line += (str(i)+" ")
                    line += "]\n"
                    fw.write(line)
        fw.close()
    fo.close()