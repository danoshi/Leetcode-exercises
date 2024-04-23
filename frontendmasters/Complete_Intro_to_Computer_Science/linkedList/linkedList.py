from typing import Optional

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length: int = 0

    def push(self, value):
        node = Node(value)
        if not self.head:  # If the list is empty...
            self.head = node  # ...both head and tail should point to the new node.
            self.tail = node
        else:  # If the list is not empty...
            assert self.tail is not None  # Assure Pyright that self.tail is not None.
            self.tail.next = node  # ...append the new node to the end of the list.
            self.tail = node  # Update the tail to be the new node.
        self.length += 1

    def pop(self):
        if not self.head:
            return None
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev:
            prev.next = None
            self.tail = prev
        else:
            self.head = self.tail = None
        self.length -= 1
        return current.value

    def _find(self, index):
        if index >= self.length:
            return None
        current = self.head
        for i in range(0, index):
            assert current is not None, "current should not be None"
            current = current.next
        return current

    def get(self, index):
        node = self._find(index)
        if not node:
            return None
        return node.value

    def delete(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            head = self.head
            if head:
                self.head = head.next
                if not self.head:
                    self.tail = None
                self.length -= 1
                return head.value
        else:
            prev = self._find(index - 1)
            if not prev or not prev.next:
                return None
            excise = prev.next
            prev.next = excise.next
            if not prev.next:
                self.tail = prev
            self.length -= 1
            return excise.value


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional['Node'] = None  # Note the forward declaration 'Node'
