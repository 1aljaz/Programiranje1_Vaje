def razsiri(podatki, m):
    """
        Program vrne maksimalno obtezeno vsoto seznama, ki vsebuje element m, pri cimer je element m tudi minimum.
    """
    n = len(podatki)
    maksimum = 0
    
    for i in range(n):
        if podatki[i] != m:
            continue

        # Pogledamo vse elemente levo od najdenega indeksa
        levo = i
        while levo > 0 and podatki[levo - 1] > m:
            levo -= 1
        
        # pogledamo vse elemente desno od najdenega indeksa
        desno = i
        while desno < n - 1 and podatki[desno + 1] > m:
            desno += 1
        
        weight = sum(podatki[levo:desno + 1])
        maksimum = max(maksimum, weight)
    
    return maksimum

d = int(input())

for _ in range(d):
    n, m = map(int, input().split())
    podatki = list(map(int, input().split()))
    print(razsiri(podatki, m))