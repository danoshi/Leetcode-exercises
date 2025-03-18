import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.string_problems.reverse_integer.solution import Solution


class TestSolution(unittest.TestCase):
    def test_reverse(self):
        solution = Solution()

        self.assertEqual(solution.reverse(120), 21)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
