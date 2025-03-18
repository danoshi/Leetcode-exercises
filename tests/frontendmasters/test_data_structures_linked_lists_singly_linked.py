import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.data_structures.linked_lists.singly_linked.solution import LinkedList


class TestSolution(unittest.TestCase):
    def test_linkedlist(self):
        linkedlist = LinkedList()

        linkedlist.push(10)
        linkedlist.push(20)
        linkedlist.push(30)

        self.assertEqual(linkedlist.get(0), 10)
        self.assertEqual(linkedlist.get(1), 20)
        self.assertEqual(linkedlist.get(2), 30)

        self.assertEqual(linkedlist.pop(), 30)
        self.assertEqual(linkedlist.delete(0), 10)
        self.assertEqual(linkedlist.get(0), 20)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
