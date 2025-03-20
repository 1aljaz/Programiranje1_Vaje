import math

def ena(mn, k):
    """Razdeli na pol z uporabo slicinga.
       Razlaga:
        velikost mnozice razdelimo na polovico in zaokrožimo navzgor.
        Npr. 7/2 = 3.5 math.ceil(3.5) = 4 - Ceil zaokroži navzgor.
        Potem pa z pomočjo rezov razdelimo množico na 2 dela. Oba
        dela vrnemo.
    """
    mn = list(mn)
    rez = []
    velikost_vsakega = [(n // k) + (1 if i < (n % k) else 0) for i in range(k)]
    for i in range(k):
        m = set()
        for j in range(ktina):
            m.add(mn[j+i*ktina])
        rez.append(m)
    return rez

print(ena({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 3))
            

