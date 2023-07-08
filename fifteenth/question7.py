class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Auxiliary stack to store minimum elements

    def push(self, val):
        self.stack.append(val)

        # Update the minimum stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return None  # or raise an appropriate error

        # Remove the top element from the main stack
        val = self.stack.pop()

        # If the top element is the minimum, remove it from the minimum stack
        if val == self.min_stack[-1]:
            self.min_stack.pop()

        return val

    def top(self):
        if not self.stack:
            return None  # or raise an appropriate error

        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            return None  # or raise an appropriate error

        return self.min_stack[-1]
