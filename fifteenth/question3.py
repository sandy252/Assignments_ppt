from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q1.put(value)

    def pop(self):
        if self.q1.empty():
            return None  # or an appropriate error message

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        top_element = self.q1.get()

        self.q1, self.q2 = self.q2, self.q1  # Swap the queues

        return top_element

    def top(self):
        if self.q1.empty():
            return None  # or an appropriate error message

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        top_element = self.q1.get()
        self.q2.put(top_element)

        self.q1, self.q2 = self.q2, self.q1  # Swap the queues

        return top_element

    def is_empty(self):
        return self.q1.empty() and self.q2.empty()
