import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_standard(self):
        self.assertEqual(area(4), 16)

    def test_perimeter_standard(self):
        self.assertEqual(perimeter(4), 16)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_float_side(self):
        self.assertAlmostEqual(area(2.5), 6.25)
        self.assertAlmostEqual(perimeter(2.5), 10.0)

    def test_negative_side_raises_error(self):
        with self.assertRaises(ValueError):
            area(-4)

if __name__ == "__main__":
    unittest.main()