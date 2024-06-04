class Node:
    def __init__(self, string=""):
        self.children = []
        self.terminus = False
        self.value = string[0] if string else ""
        if len(string) > 1:
            self.children.append(Node(string[1:]))
        elif string:
            self.terminus = True

    def add(self, string):
        value = string[0]
        next_string = string[1:]
        for child in self.children:
            if child.value == value:
                if next_string:
                    child.add(next_string)
                else:
                    child.terminus = True
                return
        self.children.append(Node(string))

    def _complete(self, search, built, suggestions):
        if len(suggestions) >= 3 or (search and search[0] != self.value):
            return suggestions

        if self.terminus:
            suggestions.append(built + self.value)

        for child in self.children:
            child._complete(search[1:], built + self.value, suggestions)

        return suggestions

    def complete(self, string):
        completions = []
        for child in self.children:
            completions.extend(child._complete(string, "", []))
        return completions

class Solution:
    def create_trie(self, words):
        root = Node("")
        for word in words:
            root.add(word.lower())
        return root
