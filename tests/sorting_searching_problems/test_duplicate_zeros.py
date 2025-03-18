import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.sorting_searching_problems.duplicate_zeros.solution import Solution

class TestSolution(unittest.TestCase):
    def test_duplicateZeros(self):
        solution = Solution()

        self.assertEqual(solution.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]), None)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
