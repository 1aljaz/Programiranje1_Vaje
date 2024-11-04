class oklepaji:
    def __init__(self, imeVhod, imeIzhod):
        self.imeVhod = imeVhod
        self.imeIzhod = imeIzhod
        self.arr = []

    def BrezOklepajev(self):
        """
        Predpostavljam, da vhodna in izhodna datoteka obstajata.
        Metoda odstrani vse pravilno postavljene oklepaje in zaklepaje, ter kar je med njima.
        """
        with open(self.imeVhod, "r", encoding="utf8") as f:
            for l in f:
                oklepaj = False
                repl = ""
                for c in l:
                    if c == '(':
                        oklepaj = True
                        repl += c
                    elif c not in "()" and oklepaj:
                        repl += c
                    elif c == ')' and oklepaj:
                        oklepaj = False
                        repl += c
                if oklepaj:
                    self.arr.append("NAPAKA\n")
                else:
                    l = l.replace(repl, '')
                    self.arr.append(l)
        
        with open(self.imeIzhod, "w", encoding="utf-8") as f:
            for l in self.arr:
                f.write(l)

        return self.arr

o = oklepaji("vhod2.txt", "izhod2.txt")

o.BrezOklepajev()