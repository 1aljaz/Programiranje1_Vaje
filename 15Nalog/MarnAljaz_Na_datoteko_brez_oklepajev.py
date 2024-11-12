def BrezOklepajev(imeVhod, imeIzhod):
    arr = []
    """
    Predpostavljam, da vhodna in izhodna datoteka obstajata.
    Metoda odstrani vse pravilno postavljene oklepaje in zaklepaje, ter kar je med njima.
    """
    with open(imeVhod, "r", encoding="utf8") as f:
        for l in f:
            oklepaj = False
            repl = ""
            for c in l:
                if c == '(': # Ko najdem oklepaj zacnem use med tem oklepajem in koncem dajat v poseben niz
                    oklepaj = True
                    repl += c
                elif c not in "()" and oklepaj: # Ce znak ni () in sm v nacinu oklepajev, ga pripopam nizu
                    repl += c
                elif c == ')' and oklepaj: # Ce je znak ( potem neham iz nacinom za oklepaje in pripopam se zadnji znak, ki mi je ostal
                    oklepaj = False
                    repl += c
            if oklepaj: # Če smo končali brez končnega zaklepaja potem javim napako
                arr.append("NAPAKA\n")
            else: # Drugače vse kar je v oklepaju + () zbrisem iz stringa in ga dam v array
                l = l.replace(repl, '')
                arr.append(l)
    # Prepišem vse iz arraya v izhodno datoteko
    with open(imeIzhod, "w", encoding="utf-8") as f:
        for l in arr:
            f.write(l)
    return arr

BrezOklepajev("vhod2.txt", "izhod2.txt")

