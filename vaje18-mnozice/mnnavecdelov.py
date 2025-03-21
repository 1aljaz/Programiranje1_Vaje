import math

def ena(mn, k):
    """Razdeli mn. mn na k-delov z uporabo slicinga.

       Razlaga:
       Množico mn pretvorimo v seznam. V velikost_vsake izračunamo kako se mora množica razdeliti.
       Ker vemo da je sum(velikost_vsakega) == len(mn), se lahko sprehodimo po
       velikosti_vsakega in vzamemo vrednost, ki je zapisana v seznamu. Nato iz seznama mn vzamemo
       toliko elementov kot jih moramo.
    """
    mn = list(mn)
    rez = []
    velikost_vsakega = [(len(mn) // k) + (1 if i < (len(mn) % k) else 0) for i in range(k)]
    s = 0
    for v in velikost_vsakega:
        rez.append(set(mn[s:s+v]))
        s+=v
    return rez
 
def dve(mn, k):
    """Funkcija razdeli množico na pol s pomočjo funkcije enumerate.

       Razlaga:
       V velikost_vsakega izracunamo koliko el. bo v vsaki podmnozici. Potem izracunamo
       komulativno vsoto zato, da bomo vedeli kdaj nehati dajati stvari v prejsnjo podmnožico.
       Potem pa z uporabo funkcije enumerate, damo stvari v pravilne podmnožice.
    """
    rez = []
    velikost_vsakega = [(len(mn) // k) + (1 if i < (len(mn) % k) else 0) for i in range(k)]
    komul = [0 for _ in range(k)]
    komul[0] = velikost_vsakega[0]
    for i in range(1, k):
        komul[i] = komul[i-1] + velikost_vsakega[i]
    s = 0
    t = set()
    for i, m in enumerate(mn):
        t.add(m)
        if i >= komul[s]-1:
            rez.append(t)
            t = set()
            s+=1

    return rez

def tri(mn, k):
    """Razdeli mn. na pol v dve mnozici mnA in mnB.
       
       Razlaga:
       Izracunamo koliko elementov mora biti v vsaki množici. Potem pa dodajamo elemente iz
       mnozice mn v t, ko imamo enkrat dovolj elementov v t, t dodamo med rezultate in 
       t odstejemo od ostanka.
    
    """
    velikost_vsakega = [(len(mn) // k) + (1 if i < (len(mn) % k) else 0) for i in range(k)]
    rez = []
    ostanek = mn.copy()

    for i in range(k-1):
        t = set()
        for el in ostanek:
            t.add(el)
            if len(t) == velikost_vsakega[i]:
                break
        rez.append(t)
        ostanek = ostanek - t
    
    rez.append(ostanek)

    return rez













def pomozna_funkcija_za_testiranje(tab:list, k:int, dol:int):
    """
        Pomožna funkcija za testiranje množic na več delov.
        Funkciaj sprejme razdeljeno množico tab, koliko delov k in
        koliko el. je bilo originalno v njej.

        Vrne True, če je pravilno razdeljeno, drugače False.
        Kriteriji:
            - Število el. v podmožicah mora biti enako št. el. v množici.
            - Število podmnožic mora biti enako številu delitev.
            - Maksimalna razlika med št. elemntov v množicah mora biti 1
    """

    a = sum([len(sub) for sub in tab]) == dol
    b = len(tab) == k
    c = max(len(s) for s in tab) - min(len(s) for s in tab) <= 1

    return a and b and c

