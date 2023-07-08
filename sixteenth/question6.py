class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None  # or raise an appropriate error

    def size(self):
        return len(self.queue)

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None  # or raise an appropriate error

    def is_empty(self):
        return len(self.queue) == 0


def reverseKElements(queue, k):
    if queue.size() < k:
        return  # Handle the case when k is greater than the queue size

    stack = []
    for _ in range(k):
        stack.append(queue.dequeue())

    while stack:
        queue.enqueue(stack.pop())

    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())
