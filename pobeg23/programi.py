from gesla import *
import math

# A del

def vsota_del(n:int):
    kopija = n
    delitelji = []
    i = 2
    sum = 0
    while i * i <= n:
        if n % i == 0:
            sum+=i
            delitelji.append(i)
        #    yield i
        i+=1
    for st in delitelji:
    #    yield n//st
        sum+=n//st
        delitelji.append(n//st)
    print(delitelji)
    return sum

print(vsota_del(ORGSECRET))


def eratostanovo_reseto(n:int):
    polje = [True for _ in range(n+1)]
    polje[0] = polje[1] = False
    p = 2
    print('zacetek')
    while (p*p <= n):
        if polje[p] == True:
            print(p)
            for i in range(p*p, n+1, p):
                polje[i] = False
        p+=1
    return polje

def najdi_prastevilo(n:int, secret:int):
    polje = eratostanovo_reseto(n)
    for i in range(n):
        if polje[i] and i % 2 == 1 and secret % i == 0:
            return i

def drugi_del(n:int):
    secret = najdi_prastevilo(n, A2SECRET)
    c = n
    n *= 100
    n -= c
    s = 0
    for ch in str(n):
        s+= int(ch)
    return str(secret) + str(s)


def collatz(n:int):
    s = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        s += 1
    return s

print(collatz(A3SECRET))

# B del






