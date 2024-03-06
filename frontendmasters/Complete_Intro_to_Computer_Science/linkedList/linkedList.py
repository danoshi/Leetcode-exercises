class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    def push(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
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
        for i in range(1, index):
            current = current.next
        return current

    def get(self, index):
        node = self._find(index)
        if not node:
            return None
        return node.value

    def delete(self, index):
        if index == 0:
            head = self.head
            if head:
                self.head = head.next
                if not self.head:
                    self.tail = None
            self.length -= 1
            return head.value
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
        self.next = None


# Create an instance of the LinkedList class
linked_list = LinkedList()

# Test the push method
linked_list.push(10)
linked_list.push(20)
linked_list.push(30)

# Test the get method
print(linked_list.get(0))  # Output: 10
print(linked_list.get(1))  # Output: 20
print(linked_list.get(2))  # Output: 30

# Test the pop method
print(linked_list.pop())  # Output: 30

# Test the delete method
print(linked_list.delete(0))  # Output: 10

# Test the remaining elements
print(linked_list.get(0))  # Output: 20
