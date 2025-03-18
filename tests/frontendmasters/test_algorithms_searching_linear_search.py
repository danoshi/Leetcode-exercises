import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.algorithms.searching.linear_search.solution import Solution


class TestLinearSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        return super().setUp()

    def test_linear_search(self):
        self.assertEqual(self.solution.linear_search(3, [1, 2, 3, 4, 5]), 2)
        self.assertEqual(self.solution.linear_search(-1, [1, 2, 3, 4, 5]), -1)

    def test_linear_search_empty_list(self):
        self.assertEqual(self.solution.linear_search(3, []), -1)

    def test_linear_search_single_element(self):
        self.assertEqual(self.solution.linear_search(1, [1]), 0)
        self.assertEqual(self.solution.linear_search(2, [1]), -1)

    def test_linear_search_multiple_elements(self):
        self.assertEqual(self.solution.linear_search(1, [1, 2, 3, 4, 5]), 0)
        self.assertEqual(self.solution.linear_search(5, [1, 2, 3, 4, 5]), 4)
        self.assertEqual(self.solution.linear_search(2, [1, 2, 3, 4, 5]), 1)
        self.assertEqual(self.solution.linear_search(4, [1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.solution.linear_search(3, [1, 2, 3, 4, 5]), 2)
        self.assertEqual(self.solution.linear_search(6, [1, 2, 3, 4, 5]), -1)

    def tearDown(self) -> None:
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
