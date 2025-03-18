import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.string_problems.first_unique_character_in_a_string.solution import Solution

class TestSolution(unittest.TestCase):
    def test_firstUniqChar(self):
        solution = Solution()

        self.assertEqual(solution.firstUniqChar("leetcode"), 0)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
