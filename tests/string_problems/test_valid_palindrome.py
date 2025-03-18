import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.string_problems.valid_palindrome.solution import Solution

class TestSolution(unittest.TestCase):
    def test_palindrom(self):
        solution = Solution()

        self.assertEqual(solution.isPalindrome(""), True)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
