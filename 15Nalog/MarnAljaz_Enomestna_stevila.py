import re

def Enomestna_Stevila(niz:str):
    """
        Iz niza vrne stevilo stevk, ki ob njih ni nobene stevilke.
    """

    # Uporabil sem regularni izraz. (?<!\d) - ne sme biti stevil pred zdajsnjo pozicijo. (?!\d) ne sme biti stevil po tej poziciji. Vmes pa mora biti stevilo.
    reg_izraz = r'(?<!\d)\d(?!\d)'
    ustrezajo = re.findall(reg_izraz, niz)
    return len(ustrezajo)

def test_enomestna_stevila():
    assert Enomestna_Stevila("9to6") == 2, "Odgovor je 2"
    assert Enomestna_Stevila("123h123213jh23kj22k2l1l23l4l5") == 4, "Odgovor je 4"
    assert Enomestna_Stevila("    5       l 5\n245") == 2, "Odgovor je 2"
    assert Enomestna_Stevila("2 do treh") == 1, "Odgovor je 1"

    print("Resitev je sprejemljiva")

test_enomestna_stevila()
