from drevo import*

def poisci(vmesni,obratni):
    '''poišče vse možne rešitve, če se zadnji v obratnem
       ponovi večkrat. Vedno obstaja vsaj ena rešitev,
       ni pa nuju, da jih je več kot ena'''
    sez = []
    koren = obratni[-1] # poiščemo koren, ki je zadnji v obratnem
    for i,vrednost in enumerate (vmesni):
        if vrednost == koren: # piščemo element v vmesnem, ki je enak korenu
            # razdelimo na levega in desnega
            vmesL = vmesni[:i]
            obratL = obratni[:i]
            
            # drevo bo imelo veljavni vmesni in obratni pregled
            # če bodo vsi elementi iz vmesnega v obratnem
            # in število elementov bo v obeh seznamih enako
            
            if sorted(vmesL) == sorted(obratL):
                # če bo veljavni levi bo tudi desni
                vmesD = vmesni[i+1:] 
                obratD = obratni[i:-1]
                sez += [[vmesL,obratL,vmesD,obratD]]

    return sez

def vmesni_obratni (vmesni, obratni):
    '''iz vmesnega in obraznega pregleda
    sestavi vse možna dvojiška dreva'''

    sez = []
    
    if len(obratni) == 0: # če je seznam prazen vrnemo prazno drevo
        return [Drevo()]
    
    if len(obratni) == 1:
        return [Drevo(obratni[0])]
    
    sez2 = poisci(vmesni,obratni) #dobimo vse trenutne možnosti
    koren = obratni[-1] # koren trenuznega drevesa
    
    for x in sez2:
        vmesL,obratL,vmesD,obratD = x 
        sezL = vmesni_obratni(vmesL,obratL) # rekuzija na levem
        sezD = vmesni_obratni(vmesD,obratD) # rekuzija na desnem

        #sestavljamo drevo
        for levoD in sezL: 
            for desnoD in sezD:
                temp=Drevo(koren,levo=levoD,desno=desnoD) #začasno drevo
                if temp not in sez: # dodamo samo neponavljajoče
                    sez.append(temp)

    return sez


##TESTI

vmesni1 = [3, 2, 2, 4, 1, 2, 3, 3]
obratni1 = [3, 4, 2, 2, 2, 3, 3, 1]

re1 = vmesni_obratni(vmesni1, obratni1) # 2 drevesi!!!

vmesni2 = [8,4,9,5,10,5,1,6,3,7]
obratni2 = [8,9,4,10,5,5,6,7,3,1]

re2 = vmesni_obratni(vmesni2, obratni2) # 2 drevesi!!!

vmesni3 = [8,4,1,2,10,5,1,1,3,7]
obratni3 = [8,1,4,10,5,2,1,7,3,1]

re3 = vmesni_obratni(vmesni3, obratni3) # 2 drevesi!!!

vmesni4 = [1,1,1]
obratni4 = [1,1,1]

re4 = vmesni_obratni(vmesni4, obratni4) # 5 drevesi!!!

vmesni5 = []
obratni5 = []

vmesni6 = [1]
obratni6 = [1]

re6 = vmesni_obratni(vmesni6, obratni6) # 1 drevo

v1 = [8, 2, 6, 4, 6, 1, 3]
o1 = [2, 8, 6, 4, 1, 3, 6]
    
r = vmesni_obratni(v1, o1) # 2 drevesi!!!

v2 = [6, 8, 2, 6, 1, 3, 4]
o2 = [6, 2, 8, 1, 4, 3, 6]

r2 = vmesni_obratni(v2, o2) # 2 drevesi!!!

v3 = [8, 2, 6, 3, 6, 1, 4]
o3 = [8, 2, 3, 4, 1, 6, 6]

r3 = vmesni_obratni(v3, o3) # 1 dreveo!!!
            
v4 = [8, 2, 6, 4, 6, 1, 3, 42, 18, 12, 16, 13, 16, 11, 14]
o4 = [2, 8, 6, 4, 1, 3, 6, 18, 12, 13, 14, 11, 16, 16, 42]

r4 = vmesni_obratni(v4, o4) # 2 drevesi!!!

v5 = [8, 2, 6, 4, 6, 1, 3, 42, 26, 28, 22, 26, 21, 23, 24]
o5 = [2, 8, 6, 4, 1, 3, 6, 26, 22, 28, 21, 24, 23, 26, 42]

r5 = vmesni_obratni(v5, o5) # 4 drevesa!!!


