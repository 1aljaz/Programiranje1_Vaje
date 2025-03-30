def hitro_sestavljanje(skatla, model):
    skupaj_skatla = {tip : sum(barve.values()) for tip, barve in skatla.items()}
    skupaj_model = {tip : sum(barve.values()) for tip, barve in model.items()}
    print(skupaj_skatla, skupaj_skatla, sep='\n')
    for tip, koliko in skupaj_model.items():
        if tip not in skupaj_skatla:
            return False
        if skupaj_skatla[tip] < koliko:
            return False
    return False

hitro_sestavljanje({'4x1': {'rdeča': 3}, '2x2': {'rdeča': 1, 'rumena': 5}}, {'4x1': {'modra': 2}, '2x2': {'rdeča': 2, 'modra': 1}})