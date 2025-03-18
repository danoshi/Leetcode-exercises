import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.algorithms.sorting.radix_sort.solution import Solution

class TestSolution(unittest.TestCase):
    def test_radixSort(self):
        solution = Solution()

        self.assertEqual(solution.getLongestNumber([1, 10, 100, 1000]), 4)
        self.assertEqual(
            solution.radixSort([2, 20324, 2323, 3, 434, 23, 1]),
            [1, 2, 3, 23, 434, 2323, 20324],
        )

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
