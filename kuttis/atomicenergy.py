# https://open.kattis.com/problems/atomicenergy
a = []
r = {}
n = 0

def energija(k:int):
    """Izracuna, koliko energije dobimo iz atoma."""
    i = j = 0
    try:
        return r[k]
    except:
    
        if k <= n:
            return int(a[k-1])
        else:
            if k % 2 == 0:
                i = j = k//2
                print(f"{i},{j}")
                try:
                    print("r[i]",r[i])
                    return 2*r[i]
                except:
                    return 2 * energija(i)
            else:
                i = k//2
                j = k//2 + 1
                print(f"{i},{j}")
                try:
                    print("r[i] i r[j] j",i, r[i], r[j],j)
                    return r[i] + r[j]
                except:
                    return energija(i) + energija(j)
        
    


n, q = map(int, input().split())
a = input().split()

for i in range(q):
    q1 = int(input())
    if q1 > 3:
        r[q1] = min (energija(q1 - j) + energija(j) for j in range(1, q1//2+1))
        for j in range(1,q1//2):
            print(f"{q1}, {j}, {q1-j}: q-j - {energija(q1-j)} + j - {energija(j)}") 
    else:
        r[q1] = energija(q1)
    print(f"Energija iz {q1} atoma: {r[q1]}")
#    print(r[q1])

print(r)