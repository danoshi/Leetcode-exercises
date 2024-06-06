import unittest
from frontendmasters.Complete_Intro_to_Computer_Science.Graphs.graphs import Solution


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
