import unittest
from ArrayExercise.Squares_of_a_Sorted_Array.SquaresOfASortedArray import (
    Solution
)

class TestSolution(unittest.TestCase):
    def test_sortedSquares(self):
        solution = Solution()

        self.assertEqual(solution.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    def tearDown(self):
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
