import sys
import os
import unittest

sys.path.append(os.path.abspath("C:/Users/azoma/Documents/GitHub/Programiranje1_Vaje/15Nalog/"))

import MarnAljaz_Masa as masa

class masaTest(unittest.TestCase):
    def setUp(self):
        self.m1 = masa.Masa(1, "kg")
        self.m2 = masa.Masa(2, "dag")
    
    def test_InvalidDeclaration(self):
        with self.assertRaises(TypeError):
            masa.Masa(1, "miljon")
        with self.assertRaises(ValueError):
            masa.Masa(-1, "kg")
    
    def test_sestevanje(self):
        prvi = self.m1 + self.m2
        self.assertEqual(prvi.enota, "kg")
        self.assertEqual(prvi.kolicina, 1.02)
    
        drugi = self.m2 + self.m1
        self.assertEqual(drugi.enota, "dag")
        self.assertEqual(drugi.kolicina, 102)

    def test_MultiplyingWithNegNumber(self):
        with self.assertRaises(ValueError):
            self.m1 * -1
        with self.assertRaises(ValueError):
            self.m2 * 0
    
    def test_faktor(self):
        self.assertEqual(self.m1.faktor(), 1000)
        self.assertEqual(self.m2.faktor(), 20)

    def test_najvecjaMasa(self):
        mase1 = [
            masa.Masa(1, "kg"),
            masa.Masa(1000, "g"),
            masa.Masa(10, "dag")
        ] 
        rez1 = masa.Masa.najvecja_masa(mase1)
        self.assertEqual(rez1.enota, "kg")
        self.assertEqual(rez1.kolicina, 1)

        mase2 = [
            masa.Masa(12, "funt"),
            masa.Masa(15, "kg"),
            masa.Masa(15, "g"),
            masa.Masa(1, "kg")
        ]
        
        rez2 = masa.Masa.najvecja_masa(mase2)
        self.assertEqual(rez2.enota, "kg")
        self.assertEqual(rez2.kolicina, 15)

    def test_sestejMase(self):
        mase1 = [
            masa.Masa(1, "kg"),
            masa.Masa(1000, "kg"),
            masa.Masa(10, "dag")
        ]  

        rez1 = masa.Masa.sestej(mase1)
        self.assertEqual(rez1.enota, "kg")
        self.assertEqual(rez1.kolicina, 1001.1)

        mase2 = [
            masa.Masa(12, "funt"),
            masa.Masa(15, "kg"),
            masa.Masa(15, 'g'),
            masa.Masa(1, "kg") 
        ]

        rez2 = masa.Masa.sestej(mase2)
        self.assertEqual(rez2.enota, "kg")
        self.assertEqual(rez2.kolicina, 21.45)


if __name__ == '__main__':
    unittest.main()

    
