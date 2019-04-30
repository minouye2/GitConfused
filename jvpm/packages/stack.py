"""Module that creates a stack along with methods to access the Stack"""
class Stack:
    """Class that creates a Stack, with methods to interact with the Stack"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """test if Stack is empty"""
        return self.items == []

    def push(self, item):
        """Put item on the stack"""
        self.items.append(item)

    def pop(self):
        """Take item off stack"""
        return self.items.pop()

    def peek(self):
        """Look at item on top of stack"""
        return self.items[len(self.items)-1]

    def size(self):
        """Tells how many items are on the stack"""
        return len(self.items)