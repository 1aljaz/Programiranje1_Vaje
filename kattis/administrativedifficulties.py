# https://open.kattis.com/problems/administrativeproblems

from math import ceil

cases = int(input())
for c in range(cases):
    n, m = map(int, input().split())

    avti = {} #{avto: [p, q, k]}
    pickup = {} #{agent:avto}
    agenti = {} #{avto:cena/inconsistent}

    for i in range(n):
        N, price, pickup_cost, kilometer = input().split()
        price = int(price)
        pickup_cost = int(pickup_cost)
        kilometer = int(kilometer)
        avti[N] = [price, pickup_cost, kilometer]

    for i in range(m):
        t, S, e, w = input().split()
        if S not in agenti:
            agenti[S] = 0
        t = int(t)

        if agenti[S] == "INCONSISTENT":
            continue
        
        if e == 'p': # Pickup
            if S in pickup.values:
                agenti[S] = "INCONSISTENT"
            if w not in pickup.values():
                pickup[S] = w
                agenti[S] += avti[pickup[S]][1]
            else:
                agenti[S] = "INCONSISTENT"
        elif e == 'r': # Return
            if S not in pickup:
                agenti[S] = "INCONSISTENT"
            else:
                agenti[S] += int(w) * avti[pickup[S]][2]
                del pickup[S]
        elif e == 'a': # Accident
            if S not in pickup:
                agenti[S] = "INCONSISTENT"
            else:
                agenti[S] += ceil(avti[pickup[S]][0] * int(w)/100)
    
    for S, a in pickup.items():
        agenti[S] = "INCONSISTENT"
    agenti = dict(sorted(agenti.items()))
    for S, p in agenti.items():
        print(S, p)


    

