# https://open.kattis.com/problems/addingwords

from sys import stdin

# Slovar za shranjevanje definicij spremenljivk
spremenljivke = {}
# Beri vrstice do konca datoteke
for line in stdin:
    # Če je ukaz 'def', dodaj novo spremenljivko
    if line[0] == 'd':
        _, spr, num = line.strip().split()
        spremenljivke[spr] = int(num)

    # Če je ukaz 'calc', izračunaj izraz
    if line[0] == 'c' and line[1] == 'a':
        operacije = list(line.strip().split())
        line = line[5:]  # Odstrani 'calc ' iz začetka
        sestevek = []
        j=0
        unknown = False
        # Pretvori besede v številke in upoštevaj operatorje
        for i in range(1, len(operacije)):
            if operacije[i] != '-' and operacije[i] != '+' and operacije[i] != '=':
                # Preveri, če je spremenljivka definirana
                if operacije[i] in spremenljivke:
                    if operacije[i-1] == '-':
                        sestevek.append(spremenljivke[operacije[i]] * -1)
                    else:
                        sestevek.append(spremenljivke[operacije[i]])
                else:
                    unknown = True
                    break
        
        if unknown:
            print(line.strip(), "unknown")
        else:
            # Poišči spremenljivko z ustrezno vrednostjo
            sprem = [s for s, num in spremenljivke.items() if num == sum(sestevek)]
            if sprem == []:
                print(line.strip(), "unknown")
            else:
                print(line.strip(), sprem[0])
    
    # Če je ukaz 'clear', izbriši vse definicije
    if line[0] == 'c' and line[1] == 'l':
        spremenljivke.clear()
