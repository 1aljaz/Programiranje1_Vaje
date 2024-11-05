import unittest
import sys
import os
from Settings import *

sys.path.append(os.path.abspath(PATH_TO_PROGRAMS))
import MarnAljaz_Enomestna_stevila as ens

class testEnomestna(unittest.TestCase):
    def test_ena(self):
        self.assertEqual(ens.Enomestna_Stevila("9to6"), 2)
        self.assertEqual(ens.Enomestna_Stevila("123h123213jh23kj22k2l1l23l4l5"), 4)
        self.assertEqual(ens.Enomestna_Stevila("2 do treh"), 1)
        self.assertEqual(ens.Enomestna_Stevila("    5       l 5\n245"), 2)


if __name__ == '__main__':
    unittest.main()