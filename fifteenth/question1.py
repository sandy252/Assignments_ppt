def nextGreaterElements(arr):
    n = len(arr)
    result = [-1] * n  # Initialize the result list with -1

    stack = []  # Create an empty stack to store the indices

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Pop elements from the stack while they are smaller than the current element
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        # If the stack is not empty, the top element is the next greater element
        if stack:
            result[i] = arr[stack[-1]]

        stack.append(i)  # Push the current index to the stack

    return result
