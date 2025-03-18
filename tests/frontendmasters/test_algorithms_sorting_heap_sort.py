import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.algorithms.sorting.heap_sort.solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        self.assertEqual(self.solution.heapSort([]), [])

    def test_single_element_array(self):
        self.assertEqual(self.solution.heapSort([1]), [1])

    def test_sorted_array(self):
        self.assertEqual(self.solution.heapSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(self.solution.heapSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(self.solution.heapSort([4, 10, 3, 5, 1]), [1, 3, 4, 5, 10])

    def test_duplicates_array(self):
        self.assertEqual(self.solution.heapSort([4, 10, 4, 5, 1]), [1, 4, 4, 5, 10])

    def test_large_numbers(self):
        self.assertEqual(
            self.solution.heapSort([1000, 2000, 500, 10000]), [500, 1000, 2000, 10000]
        )

    def test_negative_numbers(self):
        self.assertEqual(
            self.solution.heapSort([-1, -3, -2, -5, -4]), [-5, -4, -3, -2, -1]
        )

    def test_mixed_numbers(self):
        self.assertEqual(self.solution.heapSort([-1, 0, 1, -2, 2]), [-2, -1, 0, 1, 2])


if __name__ == "__main__":
    unittest.main()
