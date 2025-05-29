n = 15

stolp = [list(range(n, 0, -1)), [], []]
poteze = []

def hanoi(st, zac, konc, pomozni, poteze, stolp, gl = 0):
    if st == 1:
        disk = stolp[zac][-1]
        poteze.append((disk, zac, konc))
        stolp[konc].append(stolp[zac].pop())
        return
    
    hanoi(st - 1, zac, pomozni, konc, poteze, stolp, gl + 1)
    disk = stolp[zac][-1]
    poteze.append((disk, zac, konc))
    stolp[konc].append(stolp[zac].pop())

    hanoi(st-1, pomozni, konc, zac, poteze, stolp, gl+1)

hanoi(n, 0, 2, 1, poteze, stolp)
print(len(poteze))

"""
Če hočemo prestaviti n diskov iz A na C moramo prestaviti n-1 diskov na B. 
Potem moramo prestaviti n-tega na C in se n-1 diskov prestaviti na C. 
Iz tega sledi rekurzivna formula: H(n)=2*H(n-1)+1. 

H(n)=2*H(n-1)+1=2*(2*H(n-2)+1)+1 =2*(2*(2*H(n-3)+1)+1)+1 = ... = 2^k * T(n-k) + 2^(k-1) + 2^(k-2) + 2^(k-3) + ... + 2 + 1

Enkrat pridemo do k = n - 1, tako da H(n-k) = H(1) = 1
H(n) = 2^(n-1) + 2^(n-2) + 2^(n-3) + 2^(n-4) + ... + 2 + 1

To pa je enako kot geometrična vrsta sum(2^k) ko gre k = 0 pa do k = n-2. Ko to poračunamo pridemo do:
H(n) = 2^n - 1

To lahko tudi dokažemo s pomočjo indukcije.
H(n) = 2^n - 1
> n = 1

H(1) = 2^1 - 1 = 2 - 1 = 1

> n = n + 1
H(n+1) = 2*H(n) - 1 = 2*2^n - 1 = 2^(n+1) - 1
"""

    