def dobi_resitev(ugib, t):
    resitev = ['-'] * 5
    uporabljene = [False] * 5 
    # Zelene
    for i in range(5):
        if ugib[i] == t[i]:
            resitev[i] = 'G'
            uporabljene[i] = True

    # Rumene
    for i in range(5):
        if resitev[i] == 'G':
            continue
        for j in range(5):
            if not uporabljene[j] and ugib[i] == t[j] and ugib[j] != t[j]:
                resitev[i] = 'Y'
                uporabljene[j] = True
                break

    return ''.join(resitev)


n, m = map(int, input().split())
ugibi = [tuple(input().split()) for _ in range(n)]
besede = [input().strip() for _ in range(m)]

veljavne = []
for beseda in besede:
    veljavna = True
    for ugib, resitev in ugibi:
        if dobi_resitev(ugib, beseda) != resitev:
            veljavna = False
            break
    if veljavna:
        veljavne.append(beseda)


print('\n'.join(veljavne))
