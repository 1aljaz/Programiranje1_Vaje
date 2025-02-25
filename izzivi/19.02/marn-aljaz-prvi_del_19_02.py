import unittest

def zamenjaj_min_max(tab):
    """
    Vrne seznam s tem da zamenja prvo pojavitev najmanjšega elementa z zadnjo pojavitvijo največjega elementa.
    """
    min_index = tab.index(min(tab)) 
    max_index = len(tab) - 1 - tab[::-1].index(max(tab))
    
    tab[min_index], tab[max_index] = tab[max_index], tab[min_index]
    return tab


def vrni_ind_min_max(tab):
    """
    Vrne indeks najmanjšega in največjega elementa v seznamu.
    """
    return tab.index(min(tab)), len(tab) - 1 - tab[::-1].index(max(tab))


class TestSeznamFunctions(unittest.TestCase):
    def test_zamenjaj_min_max(self):
        self.assertEqual(zamenjaj_min_max([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])
        self.assertEqual(zamenjaj_min_max([1, 2, 3, 3, 2, 1]), [3, 2, 3, 1, 2, 1])
        self.assertEqual(zamenjaj_min_max([-5, 0, 5, -5, 10, 10]), [10, 0, 5, -5, 10, -5])
        self.assertEqual(zamenjaj_min_max([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(zamenjaj_min_max([1, 2]), [2, 1])

    def test_vrni_ind_min_max(self):
        self.assertEqual(vrni_ind_min_max([1, 2, 3, 4, 5]), (0, 4))
        self.assertEqual(vrni_ind_min_max([1, 2, 3, 3, 2, 1]), (0, 3))
        self.assertEqual(vrni_ind_min_max([-5, 0, 5, -5, 10, 10]), (0, 5))
        self.assertEqual(vrni_ind_min_max([1, 1, 1, 1]), (0, 3))
        self.assertEqual(vrni_ind_min_max([1, 2]), (0, 1))

    def test_edge_cases(self):
        self.assertEqual(zamenjaj_min_max([1]), [1])
        self.assertEqual(vrni_ind_min_max([1]), (0, 0))
        with self.assertRaises(ValueError):
            zamenjaj_min_max([])
        with self.assertRaises(ValueError):
            vrni_ind_min_max([])

if __name__ == '__main__':
    unittest.main()


