import math
import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_perimeter_classic(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        self.assertEqual(perimeter(2, 2, 2), 6)

    def test_perimeter_large(self):
        self.assertEqual(perimeter(6, 8, 10), 24)

    def test_area_math_coincidence(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0)

    def test_area_herons_formula(self):
        self.assertAlmostEqual(area(6, 8, 10), 24.0)

if __name__ == "__main__":
    unittest.main()