import unittest
from MathExercise.Find_Numbers_with_Even_Number_of_Digits.FindNumbersWithEvenNumberOfDigits import (
    Solution
)


class TestSolution(unittest.TestCase):
    def test_findNumbers(self):
        solution = Solution()

        self.assertEqual(solution.findNumbers([555, 901, 482, 1771]), 1)
    def tearDown(self):
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
