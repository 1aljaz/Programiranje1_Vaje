n = 15

stolp = [list(range(n, 0, -1)), [], []]
poteze = []

def hanoi(st, zac, konc, pomozni, poteze, stolp, gl = 0):
    if st == 1:
        disk = stolp[zac][-1]
        poteze.append((disk, zac, konc))
        stolp[konc].append(stolp[zac].pop())
        """   print(poteze)
        print(len(poteze))"""
        return
    
    hanoi(st - 1, zac, pomozni, konc, poteze, stolp, gl + 1)
    disk = stolp[zac][-1]
    poteze.append((disk, zac, konc))
    stolp[konc].append(stolp[zac].pop())

    hanoi(st-1, pomozni, konc, zac, poteze, stolp, gl+1)

hanoi(n, 0, 2, 1, poteze, stolp)
print(len(poteze))

    