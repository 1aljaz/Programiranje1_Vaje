import re

def druzabneStevke(niz:str):
    """
        Iz niza vrne število števk, ki ob njih ni nobene številke.
    """

    # Uporabil sem regularni izraz.
    reg_izraz1 = r'\d(?=\d)' # Najde števke, ki imajo števke na svoji desni
    reg_izraz2 = r'(?<=\d)\d' # Najde števke, ki imajo števke na svoji levi
    reg_izraz3 = r'(?<=\d)\d(?=\d)' # Najde števke, ki imajo števke na svoji levi in desni
    ustrezajo1 = re.findall(reg_izraz1, niz)
    ustrezajo2 = re.findall(reg_izraz2, niz)
    ustrezajo3 = re.findall(reg_izraz3, niz)
    return len(ustrezajo1) + len(ustrezajo2) - len(ustrezajo3) # Ko odštejem vse, ki imajo števke na obeh straneh preprečim duplikate v ustrezajo1 in ustrezajo2


