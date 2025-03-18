import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.remove_element.solution import Solution

class TestSolution(unittest.TestCase):
    def test_removeElement(self):
        solution = Solution()

        self.assertEqual(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)
        self.assertEqual(solution.removeElement2([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
