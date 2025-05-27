from math import sqrt
def dolzina_vektorja(vektor):
    dolzina = 0
    for komponenta in vektor:
        dolzina += komponenta ** 2
    return sqrt(dolzina)
