import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.contains_duplicate.solution import Solution


class TestSolution(unittest.TestCase):
    def test_containsDuplicate(self):
        solution = Solution()

        self.assertEqual(solution.containsDuplicate2([0, 4, 5, 0, 3, 6]), True)
        self.assertEqual(solution.containsDuplicate([0, 4, 5, 0, 3, 6]), True)
        self.assertEqual(solution.containsDuplicate2([1, 2, 3, 4, 5]), False)
        self.assertEqual(solution.containsDuplicate([1, 2, 3, 4, 5]), False)

        self.assertEqual(solution.containsDuplicate2([3, 3]), True)
        self.assertEqual(solution.containsDuplicate([3, 3]), True)

        self.assertEqual(solution.containsDuplicate2([2, 2]), True)
        self.assertEqual(solution.containsDuplicate([2, 2]), True)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
