import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.squares_of_a_sorted_array.solution import Solution

class TestSolution(unittest.TestCase):
    def test_sortedSquares(self):
        solution = Solution()

        self.assertEqual(solution.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
