n, m = map(int, input().split())
je_koncna = [True for i in range(n+1)]
dol_poglavij = list(map(int, input().split()))
poglavja = [i for i in range(n+1)]


for i in range(m):
    a, b = map(int, input().split())
    je_koncna[a] = False
    poglavja[b] = a

koncna = [i for i in range(n+1) if je_koncna[i]]

min_skupaj = float('inf')

for a in range(1, len(koncna)):
    for b in range(a+1, len(koncna)):
        if a != b:
            potrebne = {koncna[a], koncna[b]}
            trenutna = koncna[a]
            while poglavja[trenutna] != trenutna:
                potrebne.add(poglavja[trenutna])
                trenutna = poglavja[trenutna]
            trenutna = koncna[b]
            while poglavja[trenutna] != trenutna:
                potrebne.add(poglavja[trenutna])
                trenutna = poglavja[trenutna]
            
            skupaj = 0

            for p in potrebne:
               skupaj += dol_poglavij[p-1]
            
            min_skupaj = min(min_skupaj, skupaj)
            
print(min_skupaj)