def koliko(niz):
    sl = {}
    arr = niz.split(',')
    for s in arr:
        if s in sl:
            sl[s] += 1
        else:
            sl[s] = 1
        print(f"{s} {sl[s]}\n")

koliko('Janez,Maja,Zan,Janez,Maja,Zan')