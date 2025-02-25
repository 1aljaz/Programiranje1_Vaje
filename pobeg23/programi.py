from gesla import *
import math

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
    return sum

# print(vsota_del(ORGSECRET))


def eratostanovo_reseto(n:int):
    polje = [True for i in range(n+1)]
    polje[0] = polje[1] = False
    p = 2

    while (p*p <= n):
        if polje[p] == True:
            print(p)
            for i in range(p*p, n+1, p):
                polje[i] = False
        p+=1

def najdi_prastevilo(n:int):
    polje = eratostanovo_reseto(n)
    print('Najdi')
    for i in range(n):
        if polje[i] == True and i % 2 == 1:
            return i


print(najdi_prastevilo(A2SECRET))

def drugi_del(n:int):
    c = n
    n *= 100
    n -= c
    s = 0
    for ch in str(n):
        s+= int(ch)
    
    return s
