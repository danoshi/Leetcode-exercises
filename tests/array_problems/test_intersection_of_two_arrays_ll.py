import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.intersection_of_two_arrays_ll.solution import Solution

class TestSolution(unittest.TestCase):
    def test_intersect(self):
        solution = Solution()

        self.assertEqual(solution.intersect([1, 2, 2, 1], [2, 2]), [2, 2])
        self.assertEqual(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
