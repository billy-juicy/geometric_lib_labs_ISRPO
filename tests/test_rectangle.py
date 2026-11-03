import unittest
from rectangle import area, perimetr

class RectangleTestCase(unittest.TestCase):
    def test_area_standard(self):
        self.assertEqual(area(3, 4), 12)

    def test_perimetr_standard(self):
        self.assertEqual(perimetr(3, 4), 14)

    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)

    def test_square_as_rectangle(self):
        self.assertEqual(area(5, 5), 25)
        self.assertEqual(perimetr(5, 5), 20)

    def test_correct_spelling(self):
        from rectangle import perimetr
        self.assertEqual(perimetr(3, 4), 14)

if __name__ == "__main__":
    unittest.main()