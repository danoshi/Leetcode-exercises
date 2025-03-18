import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.plus_one.solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_plusOne_single_digit_no_carry(self):
        # Test adding one to a single-digit number without carrying over
        self.assertEqual(self.solution.plusOne([0]), [1])
        self.assertEqual(self.solution.plusOne([4]), [5])
        self.assertEqual(self.solution.plusOne([8]), [9])

    def test_plusOne_single_digit_with_carry(self):
        # Test adding one to a single-digit number with carrying over
        self.assertEqual(self.solution.plusOne([9]), [1, 0])

    def test_plusOne_multiple_digits_no_carry(self):
        # Test adding one to a multiple-digit number without carrying over
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(self.solution.plusOne([4, 5, 6]), [4, 5, 7])
        self.assertEqual(self.solution.plusOne([7, 8, 9]), [7, 9, 0])

    def test_plusOne_multiple_digits_with_carry(self):
        # Test adding one to a multiple-digit number with carrying over
        self.assertEqual(self.solution.plusOne([1, 9]), [2, 0])
        self.assertEqual(self.solution.plusOne([1, 9, 9]), [2, 0, 0])
        self.assertEqual(self.solution.plusOne([9, 9, 9]), [1, 0, 0, 0])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
