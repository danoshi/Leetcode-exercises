import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.data_structures.trees.trie.solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_create_trie(self):
        city_names = [
            "New York",
            "Los Angeles",
            "Chicago",
            "Houston",
            "Philadelphia",
            "Phoenix",
            "San Antonio",
            "San Diego",
            "Dallas",
            "San Jose",
            "Austin",
            "Indianapolis",
            "Jacksonville",
            "San Francisco",
        ]
        trie = self.solution.create_trie(city_names)
        completions = trie.complete("san")
        expected = ["san antonio", "san diego", "san jose"]
        self.assertEqual(completions, expected)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
