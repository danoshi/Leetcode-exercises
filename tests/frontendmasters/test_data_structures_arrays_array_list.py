import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.data_structures.arrays.array_list.solution import ArrayList

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
