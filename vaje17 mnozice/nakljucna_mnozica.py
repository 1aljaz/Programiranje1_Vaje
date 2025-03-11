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
    for i in range(n):
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
