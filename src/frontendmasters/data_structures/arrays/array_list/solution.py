class ArrayList:
    def __init__(self, data, length):
        """_summary_

        Args:
            data (_type_): _description_
            length (_type_): _description_
        """
        self.data = {}
        self.length = 0

    def push(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.data[self.length] = value
        self.length += 1

    def pop(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        response = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return response

    def get(self, index):
        """_summary_

        Args:
            index (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.data[index]

    def delete(self, index):
        """_summary_

        Args:
            index (_type_): _description_

        Returns:
            _type_: _description_
        """
        response = self.data[index]
        self._collapseTo(index)
        return response

    def _collapseTo(self, index):
        """_summary_

        Args:
            index (_type_): _description_
        """
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
