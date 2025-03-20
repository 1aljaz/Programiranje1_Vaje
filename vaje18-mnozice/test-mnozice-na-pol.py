import unittest
import sys

from mnozicenapol import *

class testMnoziceNaPol(unittest.TestCase):
    def test_ena(self): # Testiramo prvo funkcijo
        self.assertEqual(ena({1, 2, 3, 4, 5, 6}), ({1, 2, 3}, {4, 5, 6}))
        self.assertEqual(ena({3, 2, 1, 0, -1, 1}), ({0, 1, 2}, {3, -1}))
    def test_dve(self): # Testiramo drugo funkcijo
        self.assertEqual(dve({1, 2, 3, 4, 5, 6}), ({1, 2, 3}, {4, 5, 6}))
        self.assertEqual(dve({3, 2, 1, 0, -1, 1}), ({0, 1, 2}, {3, -1}))
    def test_tri(self): # Testiramo funkcijo funkcijo
        self.assertEqual(tri({1, 2, 3, 4, 5, 6}), ({1, 2, 3}, {4, 5, 6}))
        self.assertEqual(tri({3, 2, 1, 0, -1, 1}), ({0, 1, 2}, {3, -1}))



if __name__ == '__main__':
    unittest.main()