import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.data_structures.probabilistic.bloom_filter.solution import Solution


class TestBloomFilter(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_add_and_contains(self):
        test_string = "apple"
        self.assertFalse(self.solution.contains(test_string))
        self.solution.add(test_string)
        self.assertTrue(self.solution.contains(test_string))

    def test_absence(self):
        self.assertFalse(self.solution.contains("banana"))

    def test_false_positive(self):
        self.solution.add("apple")
        self.assertFalse(self.solution.contains("banana"))

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
