import sys
import os
import unittest

sys.path.append(os.path.abspath("C:/Users/azoma/Documents/GitHub/Programiranje1_Vaje/15Nalog/"))

import MarnAljaz_Dolzina as dolzina

class dolzinaTest(unittest.TestCase):
    def setUp(self):
        self.dol = dolzina.Dolzina (2, 'mm')
    def test_invalidDelcaration(self):
        with self.assertRaises(ValueError):
            dolzina.Dolzina(-1, "cm")
        with self.assertRaises(TypeError):
            dolzina.Dolzina(1, "km")
    
    def test_multiplyingWithNeg(self):
        with self.assertRaises(ValueError):
            self.dol * -1
    
    def test_najkrajsaTest(self):
        dolzine1 = [
            dolzina.Dolzina(100, "cm"),
            dolzina.Dolzina(10, "dm"),
            dolzina.Dolzina(1, "m")
        ]

        rez1 = dolzina.Dolzina.najkrajsa_razdalija(dolzine1)
        self.assertEqual(rez1.koliko, 1)
        self.assertEqual(rez1.enota, "m")
        
        dolzine2 = [
            dolzina.Dolzina(5, "m"),
            dolzina.Dolzina(10, "cm"),
            dolzina.Dolzina(10, "dm")
        ]

        rez2 = dolzina.Dolzina.najkrajsa_razdalija(dolzine2)
        self.assertEqual(rez2.koliko, 10)
        self.assertEqual(rez2.enota, "cm")

        dolzine3 = [
            dolzina.Dolzina(100, "cm"),
            dolzina.Dolzina(50, "cm"),
            dolzina.Dolzina(75, "cm")
        ]
        rez3 = dolzina.Dolzina.najkrajsa_razdalija(dolzine3)
        self.assertEqual(rez3.koliko, 50)
        self.assertEqual(rez3.enota, "cm")
        

if __name__ == '__main__':
    unittest.main()
