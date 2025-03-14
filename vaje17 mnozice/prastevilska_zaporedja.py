from timeit import default_timer as timer
import threading

def eratostenovo_sito_mnozice(n:int):
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
    s = list(range(n+1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2,sqrtn+1):
        if s[i]:
            s[i*i : n+1 : i] = [0] * len(range(i*i, n+1, i))
    return set(filter(None, s))

pram = eratostenovo_sito_mnozice(100000)
pras = eratostenovo_sito_slice(100000)


def najdi(prastevila:list):
    M = 0
    Mab = (0, 0)
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            n=0
            while((n*n + i*n + j) in prastevila):
                n+=1
            if n > M:
                M = n
                Mab = (i, j)
    print(Mab, M)
    return Mab, M

def preveri(a:int):
    i = 2
    while i*i < a:
        if a % i == 0:
            return False
    return True

def najdi_pes():
    M = 0
    Mab = (0, 0)
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            n=0
            while(preveri(n*n + i*n + j)):
                n+=1
            if n > M:
                M = n
                Mab = (i, j)
    return Mab, M

t1 = threading.Thread(target=najdi, args=(pram, ))
t2 = threading.Thread(target=najdi, args=(sorted(list(pram)), ))
t3 = threading.Thread(target=najdi, args=(sorted(list(pras))), )
t4 = threading.Thread(target=najdi, args=(pras, ))
t5 = threading.Thread(target=najdi_pes)

# (-61, 971) 71

# 1
start1 = timer()
t1.start()
end1 = timer()

# 2
start2 = timer()
t2.start()
end2 = timer()

# 3
start3 = timer()
t3.start()
end3 = timer()

# 4
start4 = timer()
t4.start()
end4 = timer()

# 5
start5 = timer()
t5.start()
end5 = timer()


t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print(f"1. naloga {end1-start1}")
print(f"2. naloga {end2-start2}")
print(f"3. naloga {end3-start3}")
print(f"4. naloga {end4-start4}")
print(f"5. naloga {end5-start5}")