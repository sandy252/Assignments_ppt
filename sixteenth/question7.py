from stack import Stack

def pairwise_destruction(sequence):
    stack = Stack()

    for word in sequence:
        if not stack.empty() and stack.top() == word:
            stack.pop()
        else:
            stack.push(word)

    return stack.size()
