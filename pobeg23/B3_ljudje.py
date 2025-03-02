with open('B3_ljudje.txt', 'r') as datoteka:
    seznam_ljudi = []
    for vrstica in datoteka:
        podatki = vrstica.strip().split(' ')
        seznam_ljudi.append((podatki[0], int(podatki[1]), podatki[2], podatki[3]))
