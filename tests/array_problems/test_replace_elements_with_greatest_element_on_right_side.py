import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.replace_elements_with_greatest_element_on_right_side.solution import Solution


class TestSolution(unittest.TestCase):
    def test_replaceElements(self):
        solution = Solution()

        self.assertEqual(
            solution.replaceElements([17, 18, 5, 4, 6, 1]), [18, 6, 6, 6, 1, -1]
        )
        self.assertEqual(solution.replaceElements([400]), [-1])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
