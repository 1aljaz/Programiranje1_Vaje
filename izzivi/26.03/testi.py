import unittest

from podobna import *
from pokaziCrke import *
from samo_enkrat import *
from slovar_izrazov4 import *

class Test(unittest.TestCase):
    def setUp(self): 
        self.rezultat = slovar_izrazov4() 
        
    def test_pokaziCrke(self):
        self.assertEqual(pokaziCrke("Maska", {'m', 's', 'k' 'a'}), ".aska") # Velike crke
        self.assertEqual(pokaziCrke("Otorinolaringolog", {'O', 'o', 'l', 'r'}), "O.or..ol.r...olo.")
        self.assertEqual(pokaziCrke("aaannnsssjjjlkkkaaa", {'A', 'N', 'J', 'S', 'K'}), "...................") # Nobena ni v mnozici

    def test_podobna(self):
        self.assertEqual(podobna("mačka", ["maska", "hiša", "pes"]), "maska")
        self.assertEqual(podobna("programiranje", ["program", "algoritmi", "koda", "python"]), "program")
        self.assertEqual(podobna("Python", ["PYTHON", "java", "ruby"]), "PYTHON") # Testiranje velikih crk
        self.assertEqual(podobna("hello!", ["hello?", "bye!", "hi?"]), "hello?") # Posebni znaki

    def test_samo_enkrat(self):
        self.assertTrue(samo_enkrat("")) # Prazen
        self.assertTrue(samo_enkrat("abcdef")) # Vsi uniqe
        self.assertFalse(samo_enkrat("abcda")) # a se ponovi
        self.assertFalse(samo_enkrat("a!@#$%!")) # Posebni znaki
        self.assertFalse(samo_enkrat("a1b2c31")) # Stevilke

    def test_slovar_izrazov4(self):
        self.assertIsInstance(self.rezultat, dict) # Preveri ali je tisto kar vrne funkcije slovar

        vsi = sum(len(izrazi) for izrazi in self.rezultat.values())
        self.assertEqual(vsi, 64) # Preveri koliko je vseh vnosov v slovarju

        self.assertIn("4*4*4*4", self.rezultat[256]) # Preverimo ce sta dva specifina v slovarju
        self.assertIn("4+4+4+4", self.rezultat[16])


if __name__ == '__main__':
    unittest.main()