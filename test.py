def koliko_napacnih(sscs, t=0):
    if not isinstance(sscs, list) and t == 0:
        return None

    skupaj_napacni = 0

    for s in sscs:
        if isinstance(s, list):
            skupaj_napacni += koliko_napacnih(s, 1)
        elif not isinstance(s, int):
            skupaj_napacni += 1

    return skupaj_napacni



print(koliko_napacnih([1, [2.0], 3, [2, 3, 4]]))