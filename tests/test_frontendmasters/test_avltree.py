import unittest
import json
from frontendmasters.Complete_Intro_to_Computer_Science.AVLTree.avltree import (
    Tree,
    Node,
)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()

    def test_add(self):
        self.tree.add(5)
        assert isinstance(self.tree.root, Node)
        self.assertEqual(self.tree.root.value, 5)

        self.tree.add(3)
        assert isinstance(self.tree.root.left, Node)
        self.assertIsNotNone(self.tree.root.left)
        self.assertEqual(self.tree.root.left.value, 3)

        self.tree.add(7)
        assert isinstance(self.tree.root.right, Node)
        self.assertEqual(self.tree.root.right.value, 7)

        self.tree.add(2)
        self.tree.add(4)
        self.tree.add(6)
        self.tree.add(8)

        self.assertIsNotNone(self.tree.root.left.left)
        assert isinstance(self.tree.root.left.left, Node)
        self.assertEqual(self.tree.root.left.left.value, 2)

        self.assertIsNotNone(self.tree.root.left.right)
        assert isinstance(self.tree.root.left.right, Node)
        self.assertEqual(self.tree.root.left.right.value, 4)

        self.assertIsNotNone(self.tree.root.right.left)
        assert isinstance(self.tree.root.right.left, Node)
        self.assertEqual(self.tree.root.right.left.value, 6)

        self.assertIsNotNone(self.tree.root.right.right)
        assert isinstance(self.tree.root.right.right, Node)
        self.assertEqual(self.tree.root.right.right.value, 8)

    def test_balance(self):
        values = [10, 20, 30, 40, 50, 25]
        for v in values:
            self.tree.add(v)

        self.assertIsNotNone(self.tree.root)
        assert isinstance(self.tree.root, Node)
        self.assertEqual(self.tree.root.value, 30)

        self.assertIsNotNone(self.tree.root.left)
        assert isinstance(self.tree.root.left, Node)
        self.assertEqual(self.tree.root.left.value, 20)

        self.assertIsNotNone(self.tree.root.right)
        assert isinstance(self.tree.root.right, Node)
        self.assertEqual(self.tree.root.right.value, 40)

        self.assertIsNotNone(self.tree.root.left.left)
        assert isinstance(self.tree.root.left.left, Node)
        self.assertEqual(self.tree.root.left.left.value, 10)

        self.assertIsNotNone(self.tree.root.left.right)
        assert isinstance(self.tree.root.left.right, Node)
        self.assertEqual(self.tree.root.left.right.value, 25)

        self.assertIsNotNone(self.tree.root.right.right)
        assert isinstance(self.tree.root.right.right, Node)
        self.assertEqual(self.tree.root.right.right.value, 50)

    def test_serialize(self):
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(2)
        self.tree.add(4)
        self.tree.add(6)
        self.tree.add(8)

        expected_dict = {
            "value": 5,
            "height": 3,
            "left": {
                "value": 3,
                "height": 2,
                "left": {"value": 2, "height": 1, "left": None, "right": None},
                "right": {"value": 4, "height": 1, "left": None, "right": None},
            },
            "right": {
                "value": 7,
                "height": 2,
                "left": {"value": 6, "height": 1, "left": None, "right": None},
                "right": {"value": 8, "height": 1, "left": None, "right": None},
            },
        }

        self.assertEqual(self.tree.to_object(), expected_dict)

    def test_to_json(self):
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(2)
        self.tree.add(4)
        self.tree.add(6)
        self.tree.add(8)

        expected_json = json.dumps(
            {
                "value": 5,
                "height": 3,
                "left": {
                    "value": 3,
                    "height": 2,
                    "left": {"value": 2, "height": 1, "left": None, "right": None},
                    "right": {"value": 4, "height": 1, "left": None, "right": None},
                },
                "right": {
                    "value": 7,
                    "height": 2,
                    "left": {"value": 6, "height": 1, "left": None, "right": None},
                    "right": {"value": 8, "height": 1, "left": None, "right": None},
                },
            },
            indent=4,
        )

        self.assertEqual(self.tree.to_json(), expected_json)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
