from pathlib import Path

def razmerje_soglasnikov(mesta:list[str]):
    soglasniki = 'bcdfghjklmnprstvz'
    samoglasniki = 'aeiou'
    par = ["", 0]
    for mesto in mesta:
        samo = 0
        sog = 0
        copy = mesto
        mesto = mesto.lower()
        for crka in mesto:
            if crka in soglasniki:
                sog += 1
            elif crka in samoglasniki:
                samo += 1
        try:
            razmerje = samo / sog
        except ZeroDivisionError:
            continue
        if razmerje >= par[1]:
            par = [copy, razmerje]
            print(par)
    return par[0], par[1]


### Tega dela kode ne spreminjaj! ###
with open(Path(__file__).parent / 'B1_kraji.txt', 'r') as datoteka:
    kraji = datoteka.read()
    seznam_krajev = kraji.split(' ')

    print(razmerje_soglasnikov(seznam_krajev))