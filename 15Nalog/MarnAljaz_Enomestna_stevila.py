import re

def Enomestna_Stevila(niz:str):
    """
        Iz niza vrne število števk, ki ob njih ni nobene številke.
    """

    # Uporabil sem regularni izraz. (?<!\d) - ne sme biti stevil pred zdajsnjo pozicijo. (?!\d) ne sme biti stevil po tej poziciji. Vmes pa mora biti stevilo.
    reg_izraz = r'(?<!\d)\d(?!\d)'
    ustrezajo = re.findall(reg_izraz, niz)
    return len(ustrezajo)

