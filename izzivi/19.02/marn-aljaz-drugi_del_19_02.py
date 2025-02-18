import random
import unittest

def album(koliko_je_slicic): 
    """
    Vrne, koliko nakupov moramo izvesti, da bomo dobili 
    vse slicice od 1 do koliko_je_slicic
    """
    album = [0 for _ in range(koliko_je_slicic)]
    st_nakupov = 0
    mnozica = set()
    while not len(mnozica) == koliko_je_slicic:
        st_nakupov += 1
        nakup = random.randint(1, koliko_je_slicic)
        mnozica.add(nakup)
        album[nakup - 1] += 1
    return st_nakupov

def povprecno_v_1000_simulacijah(vel_albuma, rezultati=None):
    '''
    Simulira 1000 polnjenj albuma dane velikosti.

    Vrne povprečno število nakupov, da dobimo
    vse slicice od 1 do velAlbuma.

    Vse rezultate shranimo v seznam rezultati, ki je
    neobvezna spremenljivka. Če ni podana, se ustvari novi seznam,
    sicer pa se rezultati doda v obstoječi seznam.
    '''
    if rezultati is None:
        rezultati = []

    vsota = 0
    for _ in range(1000):
        potrebne_slicice = album(vel_albuma)
        vsota += potrebne_slicice
        rezultati.append(potrebne_slicice)
    return round(vsota / 1000, 2)

class TestAlbumFunctions(unittest.TestCase):

    def test_album(self):
        rezultat = album(5)
        self.assertIsInstance(rezultat, int)
        self.assertGreater(rezultat, 0)
        
        rezultat_velik = album(10)
        self.assertIsInstance(rezultat_velik, int)
        self.assertGreater(rezultat_velik, 0)

    def test_povprecno_v_1000_simulacijah(self):
        seznam_rezultatov = []
        povprecje = povprecno_v_1000_simulacijah(5, seznam_rezultatov)
        self.assertIsInstance(povprecje, float)
        self.assertGreater(povprecje, 0)
        self.assertEqual(str(povprecje).split('.')[-1], str(round(povprecje, 2)).split('.')[-1])
        self.assertEqual(len(seznam_rezultatov), 1000)

if __name__ == '__main__':
    unittest.main()




