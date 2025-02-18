import unittest

def vsota_stevk(n):
   """
      vrne vsoto števk naravnega števila n
   """
   vsota = 0
   while n > 0:
       vsota += n % 10
       n //= 10
   return vsota

def vsota_crk(niz:str):
    """
    Vrne vsoto crk besede niz.
    """
    sum = 0
    for crka in niz:
        sum += ord(crka)
    return sum

def lazji(x, y):
    """
       Vrne True, če je vsota števk x manjša
       ali enaka vsoti števk y
       Tako x kot y sta naravni števili 
    """
    return  vsota_stevk(x) <= vsota_stevk(y)

def lazji_stabilno(x, y):
    """
    Stabilna verzija funkcija lazji.
    Vrne True, ce je vsota stevk x manjsa kot vsota stevk y.
    """

    return vsota_stevk(x) < vsota_stevk(y)

def lazji_besede(x, y):
    """
    Verzija funkcije lazji, ki namesto stevil sortira besede.
    Vrne True, ce je vsota crk x manjsa kot vsota crk y.
    """

    return vsota_crk(x) <= vsota_crk(y)


def quicksort_narascajoce(tab:list):
    """
    Vrne soritran seznam stevil, z uporabo funkcije lazji.
    """
    tab = tab[:]
    rez = []
    while len(tab) > 0:
        lazja = 9999
        indeks = 0
        for i in range(0, len(tab)):
            if lazji(tab[i], lazja):
                lazja = tab[i]
                indeks = i
        rez.append(tab[indeks])
        tab.pop(indeks)
    return rez

def quicksort_padajoce(tab:list):
    """
    Vrne soritran seznam stevil, z uporabo negirane funkcije lazji.
    """
    tab = tab[:]
    rez = []
    while len(tab) > 0:
        tezja = 0
        indeks = 0
        for i in range(0, len(tab)):
            if not lazji(tab[i], tezja):
                tezja = tab[i]
                indeks = i
        rez.append(tab[indeks])
        tab.pop(indeks)
    return rez

def quicksort_stabilno(tab:list):
    """
    Vrne soritran seznam stevil, z uporabo funkcije lazji_stabilno.
    """
    tab = tab[:]
    rez = []
    while len(tab) > 0:
        lazja = 9999
        indeks = 0
        for i in range(0, len(tab)):
            if lazji_stabilno(tab[i], lazja):
                lazja = tab[i]
                indeks = i
        rez.append(tab[indeks])
        tab.pop(indeks)
    return rez

def quicksort_besed_v1(tab:list):
    """
    Vrne soritran seznam besed, z uporabo funkcije lazji_besede.
    """
    tab = tab[:]
    rez = []

    while len(tab) > 0:
        manjsa = "ZZZZZZZZZZZZ"
        indeks = 0
        for i in range(0, len(tab)):
            if lazji_besede(tab[i], manjsa):
                manjsa = tab[i]
                indeks = i
        rez.append(tab[indeks])
        tab.pop(indeks)
    
    return rez

def quicksort_besed_v2(tab:list):
    """
    Vrne leksikografsko soritran seznam besed.
    """
    tab = tab[:]
    rez = []

    while len(tab) > 0:
        manjsa = "ZZZZZZZZZZZZ"
        indeks = 0
        for i in range(0, len(tab)):
            if tab[i] < manjsa:
                manjsa = tab[i]
                indeks = i
        rez.append(tab[indeks])
        tab.pop(indeks)
    
    return rez


class Test(unittest.TestCase):
    # Nepadajoca
    def test_navaden_seznam_narascajoce(self): 
        self.assertEqual(quicksort_narascajoce([1, 4, 2, 3, 5, 9, 8, 7, 6]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(quicksort_narascajoce([10, 11, 12, 13, 19, 20]), [10, 20, 11, 12, 13, 19])
    
    def test_cuden_seznam_narascajoce(self):
        self.assertEqual(quicksort_narascajoce([]), []) # Prazen
        self.assertEqual(quicksort_narascajoce([1]), [1]) # En element
        self.assertEqual(quicksort_narascajoce([1, 2, 3, 4, 5, 6, 9, 99, 999]), [1, 2, 3, 4, 5, 6, 9, 99, 999]) # Ze urejen
    
    def test_negativna_stevila_narascajoce(self):
        self.assertEqual(quicksort_narascajoce([-1, -2, -3, -4, -10, -15]), [-15, -10, -4, -3, -2, -1])
    
    def test_robni_primeri_narascajoce(self):
        self.assertEqual(quicksort_narascajoce([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 100, 10000, 100000000, 10000000000000]), [10000000000000, 100000000, 10000, 100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(quicksort_narascajoce([-9725, -9083, -5861, -4191, 4672, 704, 2463, -1027, -454, -9771, 7954, 6860, -1362, -6380, 1449, 1862, -3067, -6554, 5472, -7157, -5758, 1949, -5215, 4708, -5188, -6131, -3951, 6832, -5182, -1133, 3746, -781, -8746, 9290, -7850, 4945, -5139, 1577, -7659, 7911, -7620, 8530, -5460, -1736, -9352, 8444, -6489, -7161, 5112, 9203, 8250, 8436, 7207, -2894, 1309, 805, -3410, -7053, 6184, 7954, -7788, 2295, -7601, 5171, 4388, -3525, -6832, 8556, 7964, -6004, 2161, 6752, 7019, -8567, 208, 3364, 2836, 8236, 663, 2028, -6746, -231, 9284, -383, 8663, -6892, -1574, -7055, -2255, -8755, -7861, 3832, 7033, 6911, 1359, 7066, -5034, 2227, -2309, 1207]), [-2309, -5034, -7861, -8755, -2255, -7055, -1574, -6892, -383, -231, -6746, -8567, -6004, -6832, -3525, -7601, -7788, -7053, -3410, -2894, -7161, -6489, -9352, -1736, -5460, -7620, -7659, -5139, -7850, -8746, -781, -1133, -5182, -3951, -6131, -5188, -5215, -5758, -7157, -6554, -3067, -6380, -1362, -9771, -454, -1027, -4191, -5861, -9083, -9725, 5112, 1207, 208, 2161, 704, 2028, 2227, 7033, 805, 1309, 5171, 9203, 663, 8250, 2463, 3832, 3364, 7207, 8530, 6911, 7019, 1862, 1359, 2295, 7911, 5472, 1449, 7066, 8236, 2836, 6184, 6832, 4708, 4672, 6752, 8444, 1577, 9290, 3746, 6860, 8436, 4945, 8663, 9284, 4388, 1949, 8556, 7954, 7954, 7964])
    
    # Nenarascajoca  
    def test_navaden_seznam_nenarascajoca(self): 
        self.assertEqual(quicksort_padajoce([1, 4, 2, 3, 5, 9, 8, 7, 6]), [9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(quicksort_padajoce([10, 11, 12, 13, 19, 20]), list(reversed([10, 20, 11, 12, 13, 19])))
    
    def test_cuden_seznam_nenarascajoca(self):
        self.assertEqual(quicksort_padajoce([]), []) # Prazen
        self.assertEqual(quicksort_padajoce([1]), [1]) # En element
        self.assertEqual(quicksort_padajoce([1, 2, 3, 4, 5, 6, 9, 99, 999]), list(reversed([1, 2, 3, 4, 5, 6, 9, 99, 999]))) # Ze urejen
    
    def test_negativna_stevila_nenarascajocae(self):
        self.assertEqual(quicksort_padajoce([-1, -2, -3, -4, -10, -15]), list(reversed([-15, -10, -4, -3, -2, -1])))
    
    def test_robni_primeri_nenarascajoca(self):
        self.assertEqual(quicksort_padajoce([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 100, 10000, 100000000, 10000000000000]), list(reversed([10000000000000, 100000000, 10000, 100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])))
        self.assertEqual(quicksort_padajoce([-9725, -9083, -5861, -4191, 4672, 704, 2463, -1027, -454, -9771, 7954, 6860, -1362, -6380, 1449, 1862, -3067, -6554, 5472, -7157, -5758, 1949, -5215, 4708, -5188, -6131, -3951, 6832, -5182, -1133, 3746, -781, -8746, 9290, -7850, 4945, -5139, 1577, -7659, 7911, -7620, 8530, -5460, -1736, -9352, 8444, -6489, -7161, 5112, 9203, 8250, 8436, 7207, -2894, 1309, 805, -3410, -7053, 6184, 7954, -7788, 2295, -7601, 5171, 4388, -3525, -6832, 8556, 7964, -6004, 2161, 6752, 7019, -8567, 208, 3364, 2836, 8236, 663, 2028, -6746, -231, 9284, -383, 8663, -6892, -1574, -7055, -2255, -8755, -7861, 3832, 7033, 6911, 1359, 7066, -5034, 2227, -2309, 1207]), list(reversed([-2309, -5034, -7861, -8755, -2255, -7055, -1574, -6892, -383, -231, -6746, -8567, -6004, -6832, -3525, -7601, -7788, -7053, -3410, -2894, -7161, -6489, -9352, -1736, -5460, -7620, -7659, -5139, -7850, -8746, -781, -1133, -5182, -3951, -6131, -5188, -5215, -5758, -7157, -6554, -3067, -6380, -1362, -9771, -454, -1027, -4191, -5861, -9083, -9725, 5112, 1207, 208, 2161, 704, 2028, 2227, 7033, 805, 1309, 5171, 9203, 663, 8250, 2463, 3832, 3364, 7207, 8530, 6911, 7019, 1862, 1359, 2295, 7911, 5472, 1449, 7066, 8236, 2836, 6184, 6832, 4708, 4672, 6752, 8444, 1577, 9290, 3746, 6860, 8436, 4945, 8663, 9284, 4388, 1949, 8556, 7954, 7954, 7964])))
    
    # Stabilno
    def test_stabilno(self):
        self.assertEqual(quicksort_stabilno([1, 10, 100, 2, 11, 110, 103, 301, 31]), [1, 10, 100, 2, 11, 110, 103, 301, 31]) 
        self.assertEqual(quicksort_stabilno([1, 9090, 99, 23, 11, 32]), [1, 11, 23, 32, 9090, 99])

    # Besede func. v1   
    def test_besede_func_v1(self):
        self.assertEqual(quicksort_besed_v1(['a', 'b', 'c', 'd', 'aa', 'bb', 'z']), ['a', 'b', 'c', 'd', 'aa', 'bb', 'z'])     
        self.assert
        
if __name__ == "__main__":
    unittest.main()
