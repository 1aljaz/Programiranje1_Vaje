from timeit import default_timer as timer
import threading

def eratostenovo_sito_mnozice(n:int):
    """Vrne množico praštevil zgenerirano s pomočjo množic."""
    kandidati = set(range(2, n+1))
    p = 2
    while p < n:
        while not p in kandidati and p <= n:
            p += 1
        veckr = set(range(2*p, n+1, p))
        kandidati = kandidati - veckr
        p += 1
    return kandidati

def eratostenovo_sito_slice(n:int):
    """Vrne množico praštevil zgenerirano s pomočjo slicou."""
    s = list(range(n+1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2,sqrtn+1):
        if s[i]:
            s[i*i : n+1 : i] = [0] * len(range(i*i, n+1, i))
    return set(filter(None, s))

pram = eratostenovo_sito_mnozice(100000)
pras = eratostenovo_sito_slice(100000)

def preveri(a:int):
    """Vrne True če je a praštevilo, drugače False."""
    if a < 2:
        return False
    i = 2
    while i*i <= a:
        if a % i == 0:
            return False
        i += 1
    return True

def najdi(prastevila, rezultati, indeks, maks=100):
    """
        Nič me vrne. Zapiše pa v rezultati optimalna a in b, ter maksimalno dolžino zaporedja, čigar elementi so praštevila.
        Za ugotavljanje ali je št. praštevilo uporabimo množico/list prastevila.
    """
    start_time = timer()
    
    M = 0
    Mab = (0, 0)
    dokoncano = 0
    maks_ponovitve = (2*maks)**2
    
    for i in range(-maks, maks):
        for j in range(-maks, maks):
            n = 0
            while((n*n + i*n + j) in prastevila):
                n += 1
            if n > M:
                M = n
                Mab = (i, j)
            
            dokoncano += 1
            if dokoncano % 1000 == 0:
                procent = (dokoncano / maks_ponovitve) * 100
                print(f"Thread {indeks+1}: {procent:.1f}% konec. Trenutno: {Mab}, {M}")
    
    end_time = timer()
    rezultati[indeks] = (Mab, M, end_time - start_time)
    print(f"Thread {indeks+1} konec: {Mab}, {M}, time: {end_time - start_time:.2f}s")

def najdi_pes(rezultati, indeks, maks=100):
    """
        Nič me vrne. Zapiše pa v rezultati optimalna a in b, ter maksimalno dolžino zaporedja, čigar elementi so praštevila.
        Za ugotavljanje ali je št. praštevilo uporabimo funkcijo preveri.
    """
    start_time = timer()
    
    M = 0
    Mab = (0, 0)
    dokoncano = 0
    maks_ponovitve = (2*maks)**2
    
    for i in range(-maks, maks):
        for j in range(-maks, maks):
            n = 0
            while(preveri(n*n + i*n + j)):
                n += 1
            if n > M:
                M = n
                Mab = (i, j)
            
            dokoncano += 1
            if dokoncano % 100 == 0:
                procent = (dokoncano / maks_ponovitve) * 100
                print(f"Thread {indeks+1}: {procent:.1f}% konec. Trenutno: {Mab}, {M}")
    
    end_time = timer()
    rezultati[indeks] = (Mab, M, end_time - start_time)
    print(f"Thread {indeks+1} konec: {Mab}, {M}, time: {end_time - start_time:.2f}s")

maks = 100

rezultati = [None] * 5

t1 = threading.Thread(target=najdi, args=(pram, rezultati, 0, maks))
t2 = threading.Thread(target=najdi, args=(sorted(list(pram)), rezultati, 1, maks))
t3 = threading.Thread(target=najdi, args=(sorted(list(pras)), rezultati, 2, maks))
t4 = threading.Thread(target=najdi, args=(pras, rezultati, 3, maks))
t5 = threading.Thread(target=najdi_pes, args=(rezultati, 4, maks))

total_start = timer()

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

total_end = timer()

print("\nKoncni rezultati:")
print("==============")
for i, result in enumerate(rezultati):
    if result:
        (ab, m, execution_time) = result
        print(f"{i+1}: {ab}, {m}, cas: {execution_time:.4f}s")

print(f"\nSkupaj casa: {total_end - total_start:.4f}s")

"""
    POROČILO:


    Ker traja to kar dolgo, sem se odločil, da bom za vsak test uporabim svoj thread, ki se bodo izvajali pararelno.
    Tako sem čas izvajanja znatno zmanjšal.

    Najhitrejša sta bila 1. in 4. thread. Iz tega sklepam, da če je seznam urejen potrebuje program veliko več časa, da pogleda, če je stvar praštevilo.
    Menim da bi bil še hirejši način ta, da bi namesto množice uporabil boolean seznam. Indeks tega seznama bi bil številka sama. Tako bi lahko pogledal
    samo indeks tega seznama in bi videl če je true/false.
    V 1. in 4. threadu sem uporabil množice namesto urejenih seznamou in se je izkazalo, da sta bila močno hitejša kot ostali threadi.
    Najpočasnejsi je bil 5. thread ker smo za števila pregledovali sproti, če je praštevilo.

    Koncni rezultati:
    ==============
    1. Set množice: (-61, 971), 71, cas: 34.9596s
    2. Sorted list množice: (-61, 971), 71, cas: 812.3798s
    3. Sorted list slice: (-61, 971), 71, cas: 835.6667s
    4. Set slice: (-61, 971), 71, cas: 34.8990s
    5. Preveri funkcija: (-61, 971), 71, cas: 838.3804s

    Vsi so prišli do istega rezultata, samo 1. in 4. način sta prišla do rezultata prva, zato sta najboljša.

"""