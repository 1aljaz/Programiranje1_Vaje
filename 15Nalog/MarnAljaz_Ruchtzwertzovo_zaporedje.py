def Ruchtzwertzovo_zaporedje(tab, n:int) -> bool:
    """
        Program pove ali je podani array Ruchtzwertzovo zaporedje reda n.
    """

    # Racuna razliko med sosednjimi cleni in razliko zapise. array se sortita tako, da je najvisja razlika na prvem mestu. Potem pogledamo ce je dani red vecji ali enak najvecji razliki med cleni.
    rez=0

    if len(tab) == 0:
        return False

    for i in range(len(tab)-1):
        rez = abs(tab[i] - tab[i+1])
    
        if rez not in {0, 1, n}:
            return False
   
    return True


