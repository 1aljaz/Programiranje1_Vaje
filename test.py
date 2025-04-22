def neki(k, a=None):
    if a == None:
        a = []
    a.append(k)
    return a

neki(1)
neki(2)
neki(3)
print(neki(4))