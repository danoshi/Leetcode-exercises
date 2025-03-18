import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.max_consecutive_ones.solution import Solution

class TestSolution(unittest.TestCase):
    def test_findMaxConsecutiveOnes(self):
        solution = Solution()

        self.assertEqual(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)
        self.assertEqual(solution.findMaxConsecutiveOnes([1, 1, 1, 1, 0]), 4)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
