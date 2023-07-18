import unittest

from geometry import *

class RoundTest(unittest.TestCase):

    def setUp(self) -> None:
        self.r = Round()

    #test primeter
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

    def test_round_miss_argumetn(self):
        self.assertRaises(TypeError, self.r.perimeter_round)

    #test shape group 
    def test_group_shape(self):
        self.assertEqual(self.r.get_class_shape(), "Стандартна форма")

    def tearDown(self) -> None:
        del(self.r)


class Incomplete_circle_test(unittest.TestCase):
    
    def setUp(self) -> None:
        self.inc_cir = Incomplete_circle()

    def test_incomplete_circle_positive(self):
        self.assertEqual(self.inc_cir.perim_in_circle(60, 45), 177.62)

    def test_incomplete_circle_negative_miss_argument(self):
        self.assertRaises(TypeError, self.inc_cir.perim_in_circle, 3)

    def test_incomplete_circle_negative_miss_argument_height(self):
        self.assertRaises(TypeError, self.inc_cir.perim_in_circle, diameter=34)

    def test_incomplete_circle_negative_miss_argument_diameter(self):
        self.assertRaises(TypeError, self.inc_cir.perim_in_circle, height=5)

    def test_incomplete_circle_negative_miss_arguments(self):
        self.assertRaises(TypeError, self.inc_cir.perim_in_circle)

    def tearDown(self) -> None:
        del(self.inc_cir)

if __name__ == "__main__":
    unittest.main()