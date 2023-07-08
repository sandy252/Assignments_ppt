class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None  # or raise an appropriate error

    def is_empty(self):
        return len(self.stack) == 0


def reverse_string(s):
    stack = Stack()
    reversed_string = ""

    # Push each character onto the stack
    for char in s:
        stack.push(char)

    # Pop each character from the stack and append it to the reversed string
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string
