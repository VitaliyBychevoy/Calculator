import unittest

from geometry import *

class RoundTest(unittest.TestCase):

    def setUp(self) -> None:
        self.r = Round()

    def test_round_positive(self):
        self.assertEqual(self.r.perimeter_round(30), 94.25)



if __name__ == "__main__":
    unittest.main()