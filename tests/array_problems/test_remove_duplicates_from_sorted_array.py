import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.remove_duplicates_from_sorted_array.solution import Solution


class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        solution = Solution()

        self.assertEqual(solution.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(solution.removeDuplicates([1, 1, 2]), 2)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
