def izracunaj(st, operatorji):
    """
        Vrne izračunan izraz (število), ki mu ga poda funkcija reši.
    """
    izraz = list(st)
    i = 0
    # Najprej izračunamo množenje/deljenje potem pa še seštevanje/odštevanje
    while i < len(operatorji):
        # Preveri operatorje z višjo prioriteto (množenje in deljenje)
        if operatorji[i] in ['*', '/']:
            if operatorji[i] == '*':
                izraz[i] = izraz[i] * izraz[i+1]
            else:
                # Preveri deljenje z 0
                if izraz[i+1] == 0:
                    izraz[i] = float('inf')
                else:
                    izraz[i] = izraz[i] // izraz[i+1]
            # Odstrani uporabljeno število in operator
            izraz.pop(i+1)
            operatorji.pop(i)
        else:
            i+=1
    
    i=0
    # Izračunaj še operatorje z nižjo prioriteto (seštevanje in odštevanje)
    while i < len(operatorji):
        if operatorji[i] == '+':
            izraz[i] = izraz[i] + izraz[i+1]
        else:
            izraz[i] = izraz[i] - izraz[i+1]
        izraz.pop(i+1)
        operatorji.pop(i)
    
    return izraz[0]

def resi(n):
    """
        Vrne izraz, ki ga reši število podano z argumentom. Če takega izraza ni, potem izpiše "no solution".
    """
    # Seznam vseh možnih operatorjev
    operatorji = ['+', '-', '*', '/']
    # Seznam štirih števil 4
    stevila = [4, 4, 4, 4]

    # Preizkusi vse možne kombinacije operatorjev
    for ope1 in operatorji:
        for ope2 in operatorji:
            for ope3 in operatorji:
                # Tukaj v funkcijo podamo kopijo, saj drugače spremeninjamo seznamu stevila
                rezultat = izracunaj(stevila.copy(), [ope1, ope2, ope3])
                if rezultat == n:
                    return f"4 {ope1} 4 {ope2} 4 {ope3} 4 = {n}"
    
    return "no solution"

# Preberi število testnih primerov
n = int(input())

# Za vsak testni primer najdi rešitev
for i in range(n):
    c = int(input())
    print(resi(c))

