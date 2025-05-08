# Potrebno je najti in določiti velikost vseh datotek, ki se končajo z .py in vsebujejo črko a v imenu

import os

def velikostPyDatSCrkoA(imenik):
    """V imeniku najde vse datoteke, ki vsebujejo črko a in imajo končnico .py in izpiše njihovo skupno velikost."""
    skupno_taki = 0
    skupna_velikost = 0
    try:
        datoteke = os.listdir(imenik)
    except PermissionError:
        return 0, 0 

    for d in datoteke:
        ime = os.path.join(imenik, d)
        if os.path.isfile(ime):
            _, koncnica = os.path.splitext(d)
            if 'a' in d and koncnica == '.py':
                velikost = os.path.getsize(ime)
                skupna_velikost += velikost
                skupno_taki += 1
        elif os.path.isdir(ime):
            velikost, taki = velikostPyDatSCrkoA(ime)
            skupna_velikost += velikost
            skupno_taki += taki

    return skupna_velikost, skupno_taki
