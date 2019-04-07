import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("Paris", 48.9, 2.4)
        loc2 = Location('Home', 90, 0)

        self.assertEqual(str(loc), "Location('SLO', 35.3, -120.7)")
        self.assertEqual(str(loc1), "Location('Paris', 48.9, 2.4)")
        self.assertEqual(str(loc2), "Location('Home', 90, 0)")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("Paris", 48.9, 2.4)
        loc2 = Location('Home', 90, 0)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = loc

        self.assertEqual(loc, loc3)
        self.assertEqual(loc3, loc4)
        self.assertNotEqual(loc, loc1)
        self.assertNotEqual(loc2, loc3)


if __name__ == "__main__":
        unittest.main()
