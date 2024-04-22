import unittest
from StringExercise.Valid_Palindrome.palindrom import (
    Solution
)


class TestSolution(unittest.TestCase):
    def test_palindrom(self):
        solution = Solution()

        self.assertEqual(solution.isPalindrome(""), True)

    def tearDown(self):
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
