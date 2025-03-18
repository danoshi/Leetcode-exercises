import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.math_problems.find_numbers_with_even_number_of_digits.solution import Solution


class TestSolution(unittest.TestCase):
    def test_findNumbers(self):
        solution = Solution()

        self.assertEqual(solution.findNumbers([555, 901, 482, 1771]), 1)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
