import sys
import os
import unittest

sys.path.append(os.path.abspath("C:/Users/azoma/Documents/GitHub/Programiranje1_Vaje/15Nalog/"))

import MarnAljaz_Ruchtzwertzovo_zaporedje as r

class TestRuchtzwertzSequence(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(r.Ruchtzwertzovo_zaporedje([3, 4, 4, 3, 3, 10, 10, 9, 8], 7))  
        self.assertTrue(r.Ruchtzwertzovo_zaporedje([1, 2, 1, 2, 1], 1))                
        self.assertTrue(r.Ruchtzwertzovo_zaporedje([5, 5, 6, 6, 7], 2))                
        self.assertTrue(r.Ruchtzwertzovo_zaporedje([0, 0, 0, 0], 1))                   
        self.assertTrue(r.Ruchtzwertzovo_zaporedje([2, 3], 1))                         
        self.assertTrue(r.Ruchtzwertzovo_zaporedje([100, 100, 101], 2))                

    def test_invalid(self):
        self.assertFalse(r.Ruchtzwertzovo_zaporedje([1, 3, 5], 4))                     
        self.assertFalse(r.Ruchtzwertzovo_zaporedje([1, 2, 4], 3))                                    
        self.assertFalse(r.Ruchtzwertzovo_zaporedje([3, 5, 7], 24))                     

    def test_edge(self):
        self.assertFalse(r.Ruchtzwertzovo_zaporedje([1.5, 1.4, 1.5], 1))               
        self.assertFalse(r.Ruchtzwertzovo_zaporedje([], 2))                             
        self.assertTrue(r.Ruchtzwertzovo_zaporedje([1], 2))                            

if __name__ == "__main__":
    unittest.main()