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


def reverse_number(number):
    stack = Stack()
    number_str = str(number)
    reversed_str = ""

    # Push each digit onto the stack
    for digit in number_str:
        stack.push(digit)

    # Pop each digit from the stack and append it to the reversed string
    while not stack.is_empty():
        reversed_str += stack.pop()

    # Convert the reversed string back to an integer
    reversed_number = int(reversed_str)

    return reversed_number
