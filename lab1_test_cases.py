import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(max_list_iter(tlist), 8)
        tlist = [7, 12, 36, 8, 9]
        self.assertEqual(max_list_iter(tlist), 36)
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([6, 4, 3, 1, 7, 9]), [9, 7, 1, 3, 4, 6])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        list_val =[0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        list_val = [0, 3, 6, 9, 12]
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), None)
        list_val = [0, 10, 20]
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), 0)
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(6, 0, len(list_val) - 1, list_val), None)
        list_val = None
        with self.assertRaises(ValueError):
            bin_search(100, 0, 100, list_val)


if __name__ == "__main__":
        unittest.main()
