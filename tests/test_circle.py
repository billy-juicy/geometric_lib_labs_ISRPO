import math
import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_standard(self):
        self.assertAlmostEqual(area(5), 78.53981633974483)

    def test_perimeter_standard(self):
        self.assertAlmostEqual(perimeter(5), 31.41592653589793)

    def test_area_one(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_zero_radius(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_negative_radius_raises_error(self):
        with self.assertRaises(ValueError):
            area(-5)

if __name__ == "__main__":
    unittest.main()