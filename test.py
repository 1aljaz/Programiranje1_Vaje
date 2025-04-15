def skupna_dolzina(ttn):
    dolzina = []
    if isinstance(ttn, str):
        dolzina.append(len(ttn))
    elif isinstance(ttn, list):
        for s in ttn:
            dolzina.extend(skupna_dolzina(s))
    return sum(dolzina)

print((skupna_dolzina(['sonce', [['dez', 'veter'], 'sneg'], [[[['mavrica']]]]])))