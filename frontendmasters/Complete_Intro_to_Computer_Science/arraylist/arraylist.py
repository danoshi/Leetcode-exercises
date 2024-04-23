class ArrayList:
    def __init__(self, data, length):
        self.data = {}
        self.length = 0

    def push(self, value):
        self.data[self.length] = value
        self.length += 1

    def pop(self):
        response = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return response

    def get(self, index):
        return self.data[index]

    def delete(self, index):
        response = self.data[index]
        self._collapseTo(index)
        return response

    def _collapseTo(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
