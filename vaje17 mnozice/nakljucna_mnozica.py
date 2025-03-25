import random
from timeit import default_timer as timer

def gen1(n: int):
    """Vrne množico, katere el. zgeneriramo tako, da števila zaporedoma
        generiramo in jih dodajamo v množico.
    """
    mn = set()
    for i in range(n):
        mn.add(random.randint(1, 100))
    return mn

def gen2(n: int):
    """Vrne množico, katere el. zgeneriramo tako, da zgeneriramo kateri
    elementi ne bodo v množici.
    """
    ne = set()
    mn = set([i for i in range(1, n)])
    for i in range(100-n):
        ne.add(random.randint(1, 100))
    return mn - ne

def gen3(n: int):
    """Vrne množico, ki je bila zgenerirana s pomočjo random.sample."""
    st = [i for i in range(1, n + 10)]  
    mn = set(random.sample(st, n))
    return mn

def gen4(n:int):
    if n >= 50:
        return gen2(n)
    return gen1(n)

def test():
    timer1 = {10: 0, 50: 0, 90: 0}
    timer2 = {10: 0, 50: 0, 90: 0}
    timer3 = {10: 0, 50: 0, 90: 0}
    koliko = [10, 50, 90]
    
    for n in koliko:
        for i in range(1000):
            start = timer()
            gen1(n)
            end = timer()
            timer1[n] += end - start

            start = timer()
            gen2(n)
            end = timer()
            timer2[n] += end - start

            start = timer()
            gen3(n)
            end = timer()
            timer3[n] += end - start

    print('Povprečni časi (timer1): ')
    for n, cas in timer1.items():
        print(f"{n} - povprečni čas: {cas / 1000}")

    print('Povprečni časi (timer2): ')
    for n, cas in timer2.items():
        print(f"{n} - povprečni čas: {cas / 1000}")

    print('Povprečni časi (timer3): ')
    for n, cas in timer3.items():
        print(f"{n} - povprečni čas: {cas / 1000}")

test()

"""
POROČILO:


Rezultati:

Povprečni časi (timer1): 
10 - povprečni čas: 9.29961772635579e-06
50 - povprečni čas: 4.386240104213357e-05
90 - povprečni čas: 7.718700123950839e-05
Povprečni časi (timer2):
10 - povprečni čas: 7.743050018325448e-05
50 - povprečni čas: 4.822689667344093e-05
90 - povprečni čas: 1.961220847442746e-05
Povprečni časi (timer3):
10 - povprečni čas: 8.787403348833323e-06
50 - povprečni čas: 2.9367491137236358e-05
90 - povprečni čas: 5.343491164967418e-05

gen1 in gen3 naraščata z n-jem, gen2 pada z n-jem. Najboljša funkcija je ali hibrid med gen1 in gen2 ali pa gen3.
"""
