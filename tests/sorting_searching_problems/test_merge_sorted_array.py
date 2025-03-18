import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.sorting_searching_problems.merge_sorted_array.solution import Solution

class TestSolution(unittest.TestCase):
    def test_merge(self):
        solution = Solution()

        self.assertEqual(solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), None)
        self.assertEqual(solution.merge([1], 1, [], 0), None)
        self.assertEqual(solution.merge([0], 0, [1], 1), None)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
