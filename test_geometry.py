import unittest

from geometry import *

class RoundTest(unittest.TestCase):

    def setUp(self) -> None:
        self.r = Round()

    def test_round_the_smallest_value(self):
        self.assertEqual(self.r.perimeter_round(0.01), 0.03)

    def test_round_positive_float(self):
        self.assertEqual(self.r.perimeter_round(30.0), 94.25)

    def test_round_positive_int(self):
        self.assertEqual(self.r.perimeter_round(30), 94.25)
    
    def test_round_notEqual(self):
        self.assertNotEqual(self.r.perimeter_round(20.8), 3)

    def test_negative_none_value(self):
        self.assertRaises(TypeError, self.r.perimeter_round, None)

    def test_negative_value_negative_number(self):
        self.assertRaises(ValueError, self.r.perimeter_round, -3)

    def test_negative_value(self):
        self.assertRaises(TypeError, self.r.perimeter_round, [2])

    def test_type_input(self):
        self.assertRaises(TypeError, self.r.perimeter_round, "f")

    def tearDown(self) -> None:
        del(self.r)


if __name__ == "__main__":
    unittest.main()