import unittest
from frontendmasters.Complete_Intro_to_Computer_Science.BinarySearchTree.binarySearchTree import (
    Tree, Node
)


class TestTree(unittest.TestCase):
    def test_add(self):
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)

        # Verify tree structure
        self.assertIsNotNone(tree.root)
        assert isinstance(tree.root, Node)
        self.assertEqual(tree.root.value, 5)

        self.assertIsNotNone(tree.root.left)
        assert isinstance(tree.root.left, Node)
        self.assertEqual(tree.root.left.value, 3)

        self.assertIsNotNone(tree.root.right)
        assert isinstance(tree.root.right, Node)
        self.assertEqual(tree.root.right.value, 7)

        self.assertIsNotNone(tree.root.left.left)
        assert isinstance(tree.root.left.left, Node)
        self.assertEqual(tree.root.left.left.value, 2)

        self.assertIsNotNone(tree.root.left.right)
        assert isinstance(tree.root.left.right, Node)
        self.assertEqual(tree.root.left.right.value, 4)

        self.assertIsNotNone(tree.root.right.left)
        assert isinstance(tree.root.right.left, Node)
        self.assertEqual(tree.root.right.left.value, 6)

        self.assertIsNotNone(tree.root.right.right)
        assert isinstance(tree.root.right.right, Node)
        self.assertEqual(tree.root.right.right.value, 8)

    def test_create_correct_tree(self):
        nums = [3, 7, 4, 6, 5, 1, 10, 2, 9, 8]
        tree = Tree()
        for num in nums:
            tree.add(num)

        objs = tree.to_object()

        self.assertEqual(objs["value"], 3)

        self.assertEqual(objs["left"]["value"], 1)
        self.assertIsNone(objs["left"]["left"])

        self.assertEqual(objs["left"]["right"]["value"], 2)
        self.assertIsNone(objs["left"]["right"]["left"])
        self.assertIsNone(objs["left"]["right"]["right"])

        self.assertEqual(objs["right"]["value"], 7)

        self.assertEqual(objs["right"]["left"]["value"], 4)
        self.assertIsNone(objs["right"]["left"]["left"])

        self.assertEqual(objs["right"]["left"]["right"]["value"], 6)
        self.assertEqual(objs["right"]["left"]["right"]["left"]["value"], 5)
        self.assertIsNone(objs["right"]["left"]["right"]["left"]["right"])
        self.assertIsNone(objs["right"]["left"]["right"]["left"]["left"])

        self.assertEqual(objs["right"]["right"]["value"], 10)
        self.assertIsNone(objs["right"]["right"]["right"])

        self.assertEqual(objs["right"]["right"]["left"]["value"], 9)
        self.assertIsNone(objs["right"]["right"]["left"]["right"])

        self.assertEqual(objs["right"]["right"]["left"]["left"]["value"], 8)
        self.assertIsNone(objs["right"]["right"]["left"]["left"]["right"])
        self.assertIsNone(objs["right"]["right"]["left"]["left"]["left"])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
