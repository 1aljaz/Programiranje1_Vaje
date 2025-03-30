def podobna(beseda, vse_besede):
    """Vrne prvo tako besedo, ki je najbolj podobna besedi beseda izmed vse_besede"""
    sl = {}
    m2 = set(beseda.lower())
    for bes in vse_besede:
        m1 = set(bes.lower())
        sl[bes] = len(m1 & m2)
    m = max(sl.values())
    return str([bes for bes in sl if sl[bes] == m][0])


        