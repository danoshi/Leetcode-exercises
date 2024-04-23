import unittest
from frontendmasters.Complete_Intro_to_Computer_Science.binarySearch.binarySearch import (
    Solution,
)


class TestSolution(unittest.TestCase):
    def test_binarysearch(self):
        solution = Solution()
        binarysearch = [
            {"id": 1, "name": "Sam"},
            {"id": 10, "name": "Sarah"},
            {"id": 11, "name": "John"},
            {"id": 21, "name": "Burke"},
            {"id": 22, "name": "Ben"},
        ]
        linearsearch = [
            {"id": 1, "name": "Sam"},
            {"id": 11, "name": "Sarah"},
            {"id": 21, "name": "John"},
            {"id": 10, "name": "Burke"},
            {"id": 14, "name": "Ben"},
        ]

        self.assertEqual(
            solution.binarySearch(10, binarysearch), {"id": 10, "name": "Sarah"}
        )
        self.assertEqual(
            solution.linearSearch(10, linearsearch), {"id": 10, "name": "Burke"}
        )

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
