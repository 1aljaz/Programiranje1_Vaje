import unittest
import sys
import os
from Settings import *

sys.path.append(os.path.abspath(PATH_TO_PROGRAMS))
import MarnAljaz_DruzabneStevke as dru

class testEnomestna(unittest.TestCase):
    def test_ena(self):
        self.assertEqual(dru.druzabneStevke("bal123i4e7e12bed42"), 7)
        self.assertEqual(dru.druzabneStevke("12k34k1k 2 2k 3 2k123"), 7)
        self.assertEqual(dru.druzabneStevke("1234567890"), 10)


if __name__ == '__main__':
    unittest.main()