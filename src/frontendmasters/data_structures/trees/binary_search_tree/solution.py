from typing import Optional


class Tree:
    def __init__(self):
        """_summary_"""
        self.root: Optional[Node] = None

    def add(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            is_add = True
            while is_add:
                if current.value > value:
                    # go left
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        is_add = False
                else:
                    # go right
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        is_add = False
        return self

    def to_object(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.root:
            return self.root.serialize()
        else:
            return {}


class Node:
    def __init__(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def serialize(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        serialized_node = {"value": self.value}
        if self.left:
            serialized_node["left"] = self.left.serialize()
        else:
            serialized_node["left"] = None  # Represent None explicitly
        if self.right:
            serialized_node["right"] = self.right.serialize()
        else:
            serialized_node["right"] = None  # Represent None explicitly
        return serialized_node
