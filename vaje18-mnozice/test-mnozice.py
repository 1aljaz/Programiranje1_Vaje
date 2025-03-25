import unittest

from mnozicenapol import *
from mnnavecdelov import *

class testMnozice(unittest.TestCase):
    # Test mnozice na pol

    def test_enaa(self): # Testiramo prvo funkcijo
        self.assertEqual(enaa({1, 2, 3, 4, 5, 6}), ({1, 2, 3}, {4, 5, 6}))
        self.assertEqual(enaa({3, 2, 1, 0, -1, 1}), ({0, 1, 2}, {3, -1}))
    def test_dvee(self): # Testiramo drugo funkcijo
        self.assertEqual(dvee({1, 2, 3, 4, 5, 6}), ({1, 2, 3}, {4, 5, 6}))
        self.assertEqual(dvee({3, 2, 1, 0, -1, 1}), ({0, 1, 2}, {3, -1}))
    def test_trii(self): # Testiramo funkcijo funkcijo
        self.assertEqual(trii({1, 2, 3, 4, 5, 6}), ({1, 2, 3}, {4, 5, 6}))
        self.assertEqual(trii({3, 2, 1, 0, -1, 1}), ({0, 1, 2}, {3, -1}))
    
    # Test mnozice na vec delov

    def test_ena(self): # Testiramo prvo funkcijo
        self.assertEqual(pomozna_funkcija_za_testiranje(ena({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 7), 7, 10), True)
        self.assertEqual(pomozna_funkcija_za_testiranje(ena({1, 1, 1, 2, 3, 3, 4, 2, 1, 2, 8}, 3), 3, 5), True)
    def test_dve(self): # Testiramo drugo funkcijo
        self.assertEqual(pomozna_funkcija_za_testiranje(dve({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 7), 7, 10), True)
        self.assertEqual(pomozna_funkcija_za_testiranje(dve({1, 1, 1, 2, 3, 3, 4, 2, 1, 2, 8}, 3), 3, 5), True)
    def test_tri(self): # Testiramo drugo funkcijo
        self.assertEqual(pomozna_funkcija_za_testiranje(tri({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 7), 7, 10), True)
        self.assertEqual(pomozna_funkcija_za_testiranje(tri({1, 1, 1, 2, 3, 3, 4, 2, 1, 2, 8}, 3), 3, 5), True)





if __name__ == '__main__':
    unittest.main()