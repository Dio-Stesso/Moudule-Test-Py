import unittest

from quadrilaterals.parallelogram.parallelogram import Parallelogram


class TestParallelogram(unittest.TestCase):

    def setUp(self):
        self.quad1 = Parallelogram([(0, 0), (2, 0), (3, 1), (1, 1)])
        self.quad2 = Parallelogram([(0, 0), (2, 0), (2, 2), (0, 2)])
        self.quad3 = Parallelogram([(5, 5), (7, 5), (8, 6), (6, 6)])  # No intersection with quad1

    def test_intersection_true(self):
        self.assertTrue(self.quad1.check_intersection(self.quad2))

    def test_intersection_false(self):
        self.assertFalse(self.quad1.check_intersection(self.quad3))

    def test_compare_by_perimeter(self):
        self.assertEqual(self.quad1.compare_by_perimeter(self.quad2), 0)

    def test_compare_by_area_and_perimeter(self):
        compare_result = self.quad1.compare_by_area_and_perimeter(self.quad3)
        self.assertTrue(compare_result[0] != 0)
        self.assertTrue(compare_result[1] != 0)

    def test_correct_parallelogram_initialization(self):
        vertices = [(0, 0), (2, 0), (3, 1), (1, 1)]
        parallelogram = Parallelogram(vertices)
        self.assertEqual(parallelogram._sides, [2, 1.414, 2, 1.414])
        self.assertEqual(parallelogram.calculate_area(), 2)

    def test_incorrect_parallelogram_initialization(self):
        vertices = [(0, 0), (2, 0), (2, 2), (0, 1)]
        with self.assertRaises(ValueError):
            Parallelogram(vertices)

    def test_calculate_perimeter(self):
        vertices = [(0, 0), (2, 0), (3, 1), (1, 1)]
        parallelogram = Parallelogram(vertices)
        self.assertEqual(parallelogram.calculate_perimeter(), 7.414)

    def test_calculate_diagonals(self):
        vertices = [(0, 0), (2, 0), (3, 1), (1, 1)]
        parallelogram = Parallelogram(vertices)
        diagonals = parallelogram.calculate_diagonals()
        self.assertAlmostEqual(diagonals[0], 3.162, places=3)
        self.assertAlmostEqual(diagonals[1], 1.414, places=3)

    def test_calculate_angles(self):
        vertices = [(0, 0), (2, 0), (3, 1), (1, 1)]
        parallelogram = Parallelogram(vertices)
        angles = parallelogram.calculate_angles()
        self.assertTrue(all(0 < angle < 180 for angle in angles))

if __name__ == '__main__':
    unittest.main()
