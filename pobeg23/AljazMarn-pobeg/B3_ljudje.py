import os


def najdi_generacije(seznam_ljudi):
    """
    Vrne leto rojstva očeta in matere.
    """
    leta = {}
    # Seštejem koliko ljudi se je rodilo v posameznem letu
    for oseba in seznam_ljudi:
        leto = oseba[1]
        leta[leto] = leta.get(leto, 0) + 1
    # Sortiram po številu ljudi in po letu.
    sorted_leta = sorted(leta.items(), key=lambda x: (-x[1], x[0]))

    leto_oce = sorted_leta[125][0] if len(sorted_leta) > 125 else None

    leta_mati = []
    # Dodam vse leta, kjer ni rojstev v zadnjih dveh letih.
    for leto in sorted(leta.keys()):
        if leto - 2 not in leta:
            leta_mati.append(leto)

    return leto_oce, leta_mati


def najdi_osebo(seznam_ljudi):
    """
    Vrne ime in leto rojstva iskane osebe.
    """
    leto_oce, leta_mati = najdi_generacije(seznam_ljudi)

    mozni_ocetje = set(oseba[0] for oseba in seznam_ljudi if oseba[1] == leto_oce)

    for leto_mati in leta_mati:
        mozne_matere = set(oseba[0] for oseba in seznam_ljudi if oseba[1] == leto_mati)

        for oseba in seznam_ljudi:
            # Preverim, če ima oseba ime in leto rojstva, ki je v možnih očetjih in matere.
            if oseba[2] in mozne_matere and oseba[3] in mozni_ocetje:
                return "".join(c for c in oseba[0] if not c.isdigit()), oseba[1]

    return None, None


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "B3_ljudje.txt")

with open(file_path, "r") as datoteka:
    seznam_ljudi = []
    for vrstica in datoteka:
        podatki = vrstica.strip().split(" ")
        seznam_ljudi.append((podatki[0], int(podatki[1]), podatki[2], podatki[3]))


ime, leto = najdi_osebo(seznam_ljudi)
print(f"Ime: {ime}")
print(f"Leto rojstva: {leto}")
