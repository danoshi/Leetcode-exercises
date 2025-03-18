import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.data_structures.graphs.solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_most_common_title(self):
        my_id = 10
        degrees_of_separation = 2
        expected_title = "Chief Technology Officer"
        most_common_title = self.solution.findMostCommonTitle(
            my_id, degrees_of_separation
        )
        self.assertEqual(most_common_title, expected_title)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
