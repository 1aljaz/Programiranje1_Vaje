import math

def enaa(mn):
    """Razdeli na pol z uporabo slicinga.
       Razlaga:
        velikost mnozice razdelimo na polovico in zaokrožimo navzgor.
        Npr. 7/2 = 3.5 math.ceil(3.5) = 4 - Ceil zaokroži navzgor.
        Potem pa z pomočjo rezov razdelimo množico na 2 dela. Oba
        dela vrnemo.
    """
    mn = list(mn)
    sredina = math.ceil(len(mn)/2)
    return set(mn[:sredina]), set(mn[sredina:])


def dvee(mn):
    """Funkcija razdeli množico na pol s pomočjo funkcije enumerate.

       Razlaga:
       Fuknciaj enumerate vsakemu elementu doda njegovo zaporedno številko.
       Množici se doda vsak element dokler je njegova zaporedna številka manjša
       od polovice dolžine originalne množice.
    """
    return set([x for i, x in enumerate(mn) if i < len(mn)/2]), mn - set([x for i, x in enumerate(mn) if i < len(mn)/2])
def trii(mn):
    """Razdeli mn. na pol v dve mnozici mnA in mnB.
       
       Razlaga:
       Polovico elementov mn. mn dodamo v mnA, ostale elemente vrnemo kot razliko
       originalne mn. in mn. mnA.
    
    """
    mnA = set()
    n = len(mn) // 2 + len(mn) % 2
    for el in mn:
        mnA.add(el)
        if len(mnA) == n:
            break
    return mnA, mn - mnA
