import unittest
from ArrayExercise.Intersection_of_Two_Arrays_II.intersectionOfTwoArrays import Solution


class TestSolution(unittest.TestCase):
    def test_intersect(self):
        solution = Solution()

        self.assertEqual(solution.intersect([1, 2, 2, 1], [2, 2]), [2, 2])
        self.assertEqual(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
