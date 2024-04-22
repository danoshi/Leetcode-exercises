import unittest
from StringExercise.Valid_Anagram.anagram import Solution


class TestSolution(unittest.TestCase):
    def test_isAnagram(self):
        solution = Solution()

        self.assertEqual(solution.isAnagram("anagram", "nagaram"), True)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
