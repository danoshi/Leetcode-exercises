import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.algorithms.recursion.solution import Solution

class TestSolution(unittest.TestCase):
    def test_recursion(self):
        solution = Solution()

        self.assertEqual(solution.recursion_factorial(5), 120)
        self.assertEqual(
            solution.recursion_nested_array([10, 5, 3, 8, 2, 6, 4, 7, 9, 1]),
            55,
        )
        self.assertEqual(solution.recursion_nested_array([1, [2], 3]), 6)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
