from stack import Stack

def max_absolute_difference(arr):
    n = len(arr)
    stack = Stack()
    left_smaller = [0] * n
    right_smaller = [0] * n

    # Find nearest left smaller elements
    for i in range(n):
        while not stack.empty() and arr[stack.top()] >= arr[i]:
            stack.pop()
        
        if stack.empty():
            left_smaller[i] = 0
        else:
            left_smaller[i] = arr[stack.top()]
        
        stack.push(i)

    stack.clear()

    # Find nearest right smaller elements
    for i in range(n-1, -1, -1):
        while not stack.empty() and arr[stack.top()] >= arr[i]:
            stack.pop()
        
        if stack.empty():
            right_smaller[i] = 0
        else:
            right_smaller[i] = arr[stack.top()]
        
        stack.push(i)

    max_diff = 0

    # Calculate maximum absolute difference
    for i in range(n):
        diff = abs(left_smaller[i] - right_smaller[i])
        max_diff = max(max_diff, diff)

    return max_diff
