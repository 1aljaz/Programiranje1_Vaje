import turtle

def bel_vzorec(zelva, n, strn):
    '''Nariše BV stopnje n s stranico
       strn.
       Zaèetni in konèni položaj želve sta enaka'''
    strn3 = strn/3
    if n == 0:
        for _ in range(4):
            zelva.fd(strn)
            zelva.left(90)
    else:
        bel_vzorec(zelva, n - 1, strn3)  # V levo spodaj
        # vzorec na sredini in desno zgoraj
        for _ in range(2):
            zelva.pu()
            zelva.fd(strn3)
            zelva.lt(90)
            zelva.fd(strn3)
            zelva.rt(90)
            zelva.pd()
            bel_vzorec(zelva, n - 1, strn3)
        # levo zgoraj
        zelva.pu()
        zelva.fd(-2 * strn3)
        zelva.pd()
        bel_vzorec(zelva, n - 1, strn3)
        # desno spodaj
        zelva.pu()
        zelva.fd(2 * strn3)
        zelva.rt(90)
        zelva.fd(2 * strn3)
        zelva.lt(90)
        zelva.pd()
        bel_vzorec(zelva, n - 1, strn3)
        # nazaj v izhodišce
        zelva.pu()
        zelva.fd(-2 * strn3)
        zelva.pd()       

# gl. program
vid = turtle.Turtle()
vid.speed("fastest")
vid.ht()
bel_vzorec(vid, 4, 400)
vid.st()
