import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.sorting_searching_problems.check_if_n_and_its_double_exist.solution import Solution


class TestSolution(unittest.TestCase):
    def test_checkIfExist(self):
        solution = Solution()

        self.assertEqual(solution.checkIfExist([-2, 0, 10, -19, 4, 6, -8]), False)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
