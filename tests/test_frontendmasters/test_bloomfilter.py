import unittest
from frontendmasters.Complete_Intro_to_Computer_Science.bloomfilters.bloomfilters import (
    Solution
)


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
