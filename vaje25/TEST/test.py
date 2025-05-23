import os
def koliko_datotek(imenik):
    
    ''' prepðšteje vse navadne datoteke v tem imeniku in vseh podimenikih'''
    vse_datoteke = os.listdir(imenik)
    stevec = 0
    for datoteka in vse_datoteke:
        # ali je to navadna datoteka
        if os.path.isfile(imenik + '\\' + datoteka):
            stevec += 1
        else: # je imenik
            stevec += koliko_datotek(imenik + '\\' + datoteka)
    return stevec


    