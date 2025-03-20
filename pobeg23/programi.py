from gesla import *
import math


def vsota_del(n: int):
    """
    Vrne vsoto vseh deliteljev števila n.
    """

    kopija = n
    delitelji = []
    i = 2
    sum = 0
    while i * i <= n: 
        if n % i == 0:
            sum += i
            delitelji.append(i)
        #    yield i
        i += 1
    for st in delitelji:
        #    yield n//st
        sum += n // st
    return sum


# print(vsota_del(ORGSECRET))


def eratostanovo_reseto(n: int):
    """
    Vrne seznam števil do n, kjer je True, če je število praštevilo, sicer pa False.
    """
    polje = [True for i in range(n + 1)]
    polje[0] = polje[1] = False
    p = 2

    while p * p <= n:
        if polje[p] == True:
            print(p)
            for i in range(p * p, n + 1, p):
                polje[i] = False
        p += 1
    return polje


def najdi_prastevilo(n: int):
    """
    Vrne prvo praštevilo, ki je večje od n, deli n in je liho.
    """
    polje = eratostanovo_reseto(10000)
    print("Najdi")
    for i in range(n):
        if polje[i] == True and i % 2 == 1 and n % i == 0:
            return i


def drugi_del(n: int, secret: int):
    """
    Vrne število, ki je sestavljeno iz števila secret in vsote števk števila n.
    """
    c = n
    n *= 100
    n -= c
    s = 0
    for ch in str(n):
        s += int(ch)

    return str(secret) + str(s)


# print(drugi_del(100, najdi_prastevilo(A2SECRET)))


def collatz(n: int):
    """
    Vrne število korakov, da dosežemo 1 pri Collatzovem postopku.
    """
    st = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        st += 1
    return st


print(collatz(A3SECRET))


def des_napis():
    """
    Vrne vsoto vrednosti črk v napisu, ki sta prisotni v obeh polovicah niza.
    """
    napis = "hBOLmjuEVBLaBKhcLeqApkRIxREFsf"
    mnozicaprva = set()
    mnozicadruga = set()
    male = "abcdefghijklmnopqrstuvwxyz"
    velike = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = 0

    for i in range(len(napis) // 2):
        mnozicaprva.add(napis[i])

    for i in range(len(napis) // 2, len(napis)):
        mnozicadruga.add(napis[i])

    skupne = mnozicaprva.intersection(mnozicadruga)

    for crka in skupne:
        if crka in male:
            s += ord(crka) - 96
        elif crka in velike:
            s += ord(crka) - 38

    return s


print(des_napis())
