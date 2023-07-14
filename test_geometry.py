import unittest

from geometry import *

class RoundTest(unittest.TestCase):

    def setUp(self) -> None:
        self.r = Round()

    def test_round_positive(self):
        self.assertEqual(self.r.perimeter_round(30), 94.25)
    
    def test_round_positive_tipe_float(self):
        self.assertEqual(type(self.r.perimeter_round(30)),float)

    def test_round_negative_type_str(self):
        self.assertNotEqual(type(self.r.perimeter_round(30)), str)

    def test_round_negative_type_bool(self):
        self.assertNotEqual(type(self.r.perimeter_round(30)), bool)

    def test_type_input(self):
        self.assertRaises(ValueError, self.r.perimeter_round, "f")

    def tearDown(self) -> None:
        del(self.r)



if __name__ == "__main__":
    unittest.main()