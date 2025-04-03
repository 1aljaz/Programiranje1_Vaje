import random
from timeit import default_timer as timer

STPONOV = 1000


def izberi_navadno(arr:list, vsaj_koliko:int=10000)->list:
    """Vrne seznam, tistih el. kateri imajo št. prebivalcov večje od
    vsaj_koliko, in čas izvajanja.
    S pomočjo for in appenda.
    """
    start = timer()
    rez = []
    for kraj, st in arr:
        if st>=vsaj_koliko:
            rez.append(kraj)
    return rez, timer()-start


def izberi_filter(arr:list, vsaj_koliko:int=10000)->list:
    """Vrne seznam, tistih el. kateri imajo št. prebivalcov večje od
    vsaj_koliko, in čas izvajanja.
    S pomočjo filter funkcije.
    """
    start = timer()
    return list(filter(lambda x: x[1] >= vsaj_koliko, arr)), timer() - start


def genIme(st:int)->str:
    """Vrne seznam st besed, ki so nakljucno generirane."""
    rez = []
    for _ in range(st):
        beseda = ""
        for _ in range(random.randint(5, 10)):
            if beseda == "":
                beseda+= chr(ord('A') + random.randint(0, 25))
            else:
                beseda+= chr(ord('a') + random.randint(0, 25))
        rez.append(beseda)
    return rez


def genPrimere(st_krajev:int, procenti:int):
    """Vrne seznam primerov izmed katerimi je procenti procentov vecjih od 10000."""
    rez = []
    n = st_krajev * procenti // 100
    kraji = genIme(st_krajev)
    for i, kraj in enumerate(kraji):
        if i >= n:
            break
        rez.append((kraj, random.randint(10000, 200000)))

    for i in range(n+1, st_krajev):
        rez.append((kraji[i], random.randint(12, 9999)))
    
    return rez

koliko_krajev = [100, 200, 400, 800, 1600, 3200, 6400]
procenti = [10, 20, 50, 80, 100]


time_navadno = [[0, 0, 0, 0, 0] for _ in range(7)]
time_filter = [[0, 0, 0, 0, 0] for _ in range(7)]

for i in range(len(koliko_krajev)):
    for j in range(len(procenti)):
        tabela = genPrimere(koliko_krajev[i], procenti[j])
        s = 0
        for _ in range(STPONOV):
            s += izberi_navadno(tabela)[1]

        time_navadno[i][j] = s / STPONOV

        s = 0
        for _ in range(STPONOV):
            s += izberi_filter(tabela)[1]

        time_filter[i][j] = s / STPONOV

for i in range(len(koliko_krajev)):
    print(f"Za {koliko_krajev[i]} krajev:")
    print("Filtriranje s for stavkom:")
    for j in range(len(procenti)):
        print(f"{procenti[j]}%: {time_navadno[i][j]:.10f}s", end="   |   ")
    print("\nFiltriranje s funkcijo filter:")
    for j in range(len(procenti)):
        print(f"{procenti[j]}%: {time_filter[i][j]:.10f}s", end="   |   ")
    print("\n")

"""
Rezultati:

Za 100 krajev:
Filtriranje s for stavkom:
10%: 0.0000038198s   |   20%: 0.0000043690s   |   50%: 0.0000056427s   |   80%: 0.0000088443s   |   100%: 0.0000113425s   |   
Filtriranje s funkcijo filter:
10%: 0.0000096124s   |   20%: 0.0000097312s   |   50%: 0.0000097642s   |   80%: 0.0000124437s   |   100%: 0.0000131390s   |

Za 200 krajev:
Filtriranje s for stavkom:
10%: 0.0000096825s   |   20%: 0.0000103994s   |   50%: 0.0000161877s   |   80%: 0.0000173807s   |   100%: 0.0000226909s   |
Filtriranje s funkcijo filter:
10%: 0.0000183283s   |   20%: 0.0000184284s   |   50%: 0.0000225952s   |   80%: 0.0000250453s   |   100%: 0.0000255582s   |

Za 400 krajev:
Filtriranje s for stavkom:
10%: 0.0000190480s   |   20%: 0.0000184913s   |   50%: 0.0000270639s   |   80%: 0.0000378570s   |   100%: 0.0000443812s   |
Filtriranje s funkcijo filter:
10%: 0.0000362982s   |   20%: 0.0000389074s   |   50%: 0.0000440068s   |   80%: 0.0000511213s   |   100%: 0.0000515385s   |

Za 800 krajev:
Filtriranje s for stavkom:
10%: 0.0000416777s   |   20%: 0.0000464745s   |   50%: 0.0000552513s   |   80%: 0.0000772584s   |   100%: 0.0000929984s   |
Filtriranje s funkcijo filter:
10%: 0.0000760138s   |   20%: 0.0000781499s   |   50%: 0.0000871048s   |   80%: 0.0001070452s   |   100%: 0.0001175072s   |

Za 1600 krajev:
Filtriranje s for stavkom:
10%: 0.0000788078s   |   20%: 0.0000778449s   |   50%: 0.0001429626s   |   80%: 0.0001911230s   |   100%: 0.0002242717s   |
Filtriranje s funkcijo filter:
10%: 0.0001504634s   |   20%: 0.0001560981s   |   50%: 0.0002123452s   |   80%: 0.0002444558s   |   100%: 0.0002733323s   |

Za 3200 krajev:
Filtriranje s for stavkom:
10%: 0.0001585178s   |   20%: 0.0001823270s   |   50%: 0.0002314474s   |   80%: 0.0003439552s   |   100%: 0.0003024434s   |
Filtriranje s funkcijo filter:
10%: 0.0003312006s   |   20%: 0.0003310037s   |   50%: 0.0003635656s   |   80%: 0.0004579997s   |   100%: 0.0004036010s   |

Za 6400 krajev:
Filtriranje s for stavkom:
10%: 0.0002632355s   |   20%: 0.0003652256s   |   50%: 0.0004364344s   |   80%: 0.0005188498s   |   100%: 0.0005186242s   |
Filtriranje s funkcijo filter:
10%: 0.0006027777s   |   20%: 0.0006884346s   |   50%: 0.0007100138s   |   80%: 0.0007297214s   |   100%: 0.0007066419s   |

Pri vseh primerjih je bilo klasicno filtirianje s for-om in append-om hitrejse od filtriranja s filter funkcijo.
"""