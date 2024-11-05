import unittest
import sys
import os
from Settings import *

sys.path.append(os.path.abspath(PATH_TO_PROGRAMS))

import MarnAljaz_Na_datoteko_brez_oklepajev as m

class Testoklepaji(unittest.TestCase):
    def setUp(self):
        self.o1 = m.oklepaji("../brez_oklepajev/in/vhod1.txt", "../brez_oklepajev/out/izhod1.txt")
        self.o2 = m.oklepaji("../brez_oklepajev/in/vhod2.txt", "../brez_oklepajev/out/izhod2.txt")
    def tearDown(self):
        print("Teardown")
    def test_brez_oklepajev(self):
        self.assertEqual(self.o1.BrezOklepajev(), ["Peter  zamuja.\n", "NAPAKA\n", "To ni racun.\n", "2*2+=8\n", "NAPAKA\n", "[]\n", "Konec.\n"])
        self.assertEqual(self.o2.BrezOklepajev(), ["Vcerajsni  je bil zelo dober.\n"," res \n","Pa to  more biti res\n", "....\n", "[[[[[[[[[[[[[[[[[[]"])


if __name__ =='__main__':
    unittest.main()
    