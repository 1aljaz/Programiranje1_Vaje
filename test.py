def je_sifra(sifra):
    sl = []
    r = []
    for crka, slika in sifra.items():
        for c, s in sl:
            if crka == s:
                s = crka
                continue
        sl.append((crka, slika))
    print(sl)
    for i in range(len(sl)):
        if sl[i][0] != sl[i][1]:
            r.append(sl[i])
    return len(r) == 0


je_sifra({"A":"B", "B":"C", "C": "D"})
