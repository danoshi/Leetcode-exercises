import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.height_checker.solution import Solution

class TestSolution(unittest.TestCase):
    def test_heightChecker(self):
        solution = Solution()

        self.assertEqual(solution.heightChecker([1, 1, 4, 2, 1, 3]), 3)
        self.assertEqual(solution.heightChecker([5, 1, 2, 3, 4]), 5)
        self.assertEqual(solution.heightChecker([1, 2, 3, 4, 5]), 0)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
