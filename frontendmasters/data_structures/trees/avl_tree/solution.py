import json
from typing import Optional


class Node:
    def __init__(self, value=None, left=None, right=None) -> None:
        """_summary_

        Args:
            value (_type_, optional): _description_. Defaults to None.
            left (_type_, optional): _description_. Defaults to None.
            right (_type_, optional): _description_. Defaults to None.
        """
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.height = 1

    def add(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if value < self.value:
            if self.left:
                # recursion
                self.left.add(value)
            else:
                self.left = Node(value)
            if not self.right or self.right.height < self.left.height:
                self.height = self.left.height + 1
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)
            if not self.left or self.right.height > self.left.height:
                self.height = self.right.height + 1

        self.balance()

    def balance(self):
        """_summary_"""
        right_height = self.right.height if self.right else 0
        left_height = self.left.height if self.left else 0

        if left_height > right_height + 1:
            left_right_height = (
                self.left.right.height if self.left and self.left.right else 0
            )
            left_left_height = (
                self.left.left.height if self.left and self.left.left else 0
            )

            if left_right_height > left_left_height:
                if self.left:
                    self.left.rotateRR()
            self.rotateLL()

        elif right_height > left_height + 1:
            right_right_height = (
                self.right.right.height if self.right and self.right.right else 0
            )
            right_left_height = (
                self.right.left.height if self.right and self.right.left else 0
            )

            if right_left_height > right_right_height:
                if self.right:
                    self.right.rotateLL()
            self.rotateRR()

    def rotateRR(self):
        """_summary_"""
        value_before = self.value
        left_before = self.left
        if self.right:
            self.value = self.right.value
            self.left = self.right
            self.right = self.right.right
            self.left.right = self.left.left
            self.left.left = left_before
            self.left.value = value_before
            self.left.update_in_new_location()
            self.update_in_new_location()

    def rotateLL(self):
        """_summary_"""
        value_before = self.value
        right_before = self.right
        if self.left:
            self.value = self.left.value
            self.right = self.left
            self.left = self.left.left
            self.right.left = self.right.right
            self.right.right = right_before
            self.right.value = value_before
            self.right.update_in_new_location()
            self.update_in_new_location()

    def update_in_new_location(self):
        """_summary_"""
        if not self.right and not self.left:
            self.height = 1
        elif not self.right or (self.left and self.right.height < self.left.height):
            if self.left:
                self.height = self.left.height + 1
        else:
            self.height = self.right.height + 1

    def serialize(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        ans = {"value": self.value, "height": self.height}
        ans["left"] = self.left.serialize() if self.left else None
        ans["right"] = self.right.serialize() if self.right else None
        return ans


class Tree:
    def __init__(self) -> None:
        """_summary_"""
        self.root: Optional[Node] = None

    def add(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def to_json(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return (
            json.dumps(self.root.serialize(), indent=4)
            if self.root
            else json.dumps(None, indent=4)
        )

    def to_object(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.root.serialize() if self.root else None


# Example usage
tree = Tree()
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(2)
tree.add(4)
tree.add(6)
tree.add(8)

print(tree.to_json())
print(tree.to_object())
