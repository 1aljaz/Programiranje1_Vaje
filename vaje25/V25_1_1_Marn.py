import turtle as tu

def stranica(t, n, d):
    """Nariše stranico izbočenega kvadrata reda n"""
    if n == 1:
        t.fd (d)
        return d
    else:
        t.fd (d / 3)
        t.lt(90)
        t.fd (d / 3)
        t.rt(90)
        rek_dolz = stranica(t, n - 1, d / 3)
        t.rt(90)
        t.fd (d / 3)
        t.lt(90)
        t.fd (d / 3)
        return rek_dolz + 4 * d / 3

def kvadrat(t, n, d):
    """Nariše izbočen kvadrat reda n"""
    o = 0
    for i in range(4):
        o += stranica(t, n, d)
        t.rt(90)
    return o

def izracunaj_ploscino(n, d):
    """Izračuna ploscino izbočenega kvadrata reda n"""
    if n == 1:
        return d ** 2
    else:
        p = izracunaj_ploscino(n - 1, d / 3)
        return 5 * p

def izbocen_kvadrat(t, n, d):
    """Nariše izbočen kvadrat reda n in vrne obseg in ploscino"""
    o = kvadrat(t, n, d)
    pl = izracunaj_ploscino(n, d)
    return (o, pl)


t = tu.Turtle()
n = 4
d = 200  

t.speed(0)
rezultat = izbocen_kvadrat(t, n, d)
print(f"obseg: {rezultat[0]}, ploscina: {rezultat[1]}")

tu.done()