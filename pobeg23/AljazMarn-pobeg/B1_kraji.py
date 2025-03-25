import os


def najboljsi_kraj(seznam_krajev: list):
    """
    Vrne kraj, ki ima največje razmerje med samoglasniki in soglasniki.
    """
    samoglasniki = "aeiou"
    soglasniki = "bcdfghjklmnprstvz"

    maks = ["", 0]

    for kraj in seznam_krajev:
        soglasniki_v_imenu = 0
        samoglasniki_v_imenu = 0
        for crka in kraj:
            if crka in soglasniki:
                soglasniki_v_imenu += 1
            elif crka in samoglasniki:
                samoglasniki_v_imenu += 1
        try:
            razmerje = samoglasniki_v_imenu / soglasniki_v_imenu
        except ZeroDivisionError:
            razmerje = 0

        if razmerje > maks[1]:
            maks = [kraj, razmerje]

    return maks[0]


### Tega dela kode ne spreminjaj! ###
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "B1_kraji.txt")


with open(file_path, "r", encoding="utf-8") as datoteka:
    kraji = datoteka.read()
    seznam_krajev = kraji.split(" ")
    print(najboljsi_kraj(seznam_krajev))
