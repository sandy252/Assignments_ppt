from queue import Queue
from stack import Stack

def check_queue_order(queue):
    stack = Stack()
    new_queue = Queue()
    expected = 1

    while not queue.empty():
        if queue.queue[0] == expected:
            new_queue.put(queue.get())
            expected += 1
        elif not stack.empty() and stack.top() == expected:
            new_queue.put(stack.pop())
            expected += 1
        else:
            stack.push(queue.get())

    while not stack.empty():
        if stack.top() == expected:
            new_queue.put(stack.pop())
            expected += 1
        else:
            return False

    return True
