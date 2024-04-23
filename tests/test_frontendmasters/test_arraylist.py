import unittest
from frontendmasters.Complete_Intro_to_Computer_Science.arraylist.arraylist import (
    ArrayList,
)


class TestSolution(unittest.TestCase):
    def test_add(self):
        arraylist = ArrayList(data={}, length=0)
        arraylist.push(10)
        arraylist.push(20)
        arraylist.push(30)

        self.assertEqual(arraylist.get(0), 10)
        self.assertEqual(arraylist.pop(), 30)
        self.assertEqual(arraylist.delete(1), 20)
        self.assertEqual(arraylist.get(0), 10)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
