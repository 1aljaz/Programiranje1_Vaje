import sys
import os
import unittest

sys.path.append(os.path.abspath("C:/Users/azoma/Documents/GitHub/Programiranje1_Vaje/15Nalog/"))

import MarnAljaz_Kvadratna_enacba as kvEnacba

class KvTest(unittest.TestCase):
    def test_positive_D(self):
        self.assertEqual(kvEnacba.nicleKvEnacbe(1, -3, 2), [2.0, 1.0])

    def test_zero_D(self):
        self.assertEqual(kvEnacba.nicleKvEnacbe(1, 2, 1), [-1.0, -1.0])

    def test_negative_D(self):
        with self.assertRaises(ValueError):
            kvEnacba.nicleKvEnacbe(1, 4, 5)


if __name__ == '__main__':
    unittest.main()