import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.single_number.solution import Solution

class TestSolution(unittest.TestCase):
    def test_singleNumber(self):
        solution = Solution()

        self.assertEqual(solution.singleNumber([2, 2, 1]), 1)
        self.assertEqual(solution.singleNumber([4, 1, 2, 1, 2]), 4)
        self.assertEqual(solution.singleNumber([1]), 1)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
