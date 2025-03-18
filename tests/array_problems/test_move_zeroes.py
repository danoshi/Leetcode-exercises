import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.move_zeroes.solution import Solution

class TestSolution(unittest.TestCase):
    def test_moveZeroes(self):
        solution = Solution()

        self.assertEqual(solution.moveZeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]), None)
        self.assertEqual(solution.moveZeroes2([0, 0, 1]), None)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
