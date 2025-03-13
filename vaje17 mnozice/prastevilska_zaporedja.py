def eratostenovo_sito(n:int):
    kandidati = set(range(2, n+1))
    p = 2
    while p < n:
        while not p in kandidati and p <= n:
            p += 1
        veckr = set(range(2*p, n+1, p))
        kandidati = kandidati - veckr
        p += 1
    return kandidati

pra = eratostenovo_sito(1000000)


def najdi1(prastevila:list):
    