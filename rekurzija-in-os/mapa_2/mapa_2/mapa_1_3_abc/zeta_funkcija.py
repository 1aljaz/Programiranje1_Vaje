def zeta(s,n):
    vsota = 0
    for i in range(1, n+1):
        vsota += i ** (-s)
    return vsota
