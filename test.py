def pogostost_crk(besedilo):
    sl = {}
    for c in besedilo:
        sl[c] = sl.get(c, 0) + 1
    return sl

def najpogostejsa(sl):
    M = max(sl.values())
    for c, n in sl.items():
        if n == M:
            return c
        
def razbij(beseda):
    abeceda = "abcčdefghijklmnoprsštuvzž"
    naj_crka = najpogostejsa(pogostost_crk(beseda))
    zamik = abeceda.index(naj_crka) - abeceda.index('e')
    return "".join(abeceda[(abeceda.index(c) - zamik) % len(abeceda)] for c in beseda)

print(razbij("ajzaštfjzjinrt"))
print(len("od obstojeÄih presledkov. Tako nastale nadaljevalne vrstice se zato vedno zaÄnejo s presledkom; tiste nastale vrstice, ki nimajo ..."))