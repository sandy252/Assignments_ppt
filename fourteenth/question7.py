class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def next_greater_node(head):
    stack = []
    current = head
    result = []

    # Traverse the linked list to find next greater node values
    while current:
        while stack and current.val > result[stack[-1]]:
            result[stack.pop()] = current.val
        stack.append(len(result))
        result.append(current.val)
        current = current.next
    
    # Set remaining elements in the result array as 0
    for index in stack:
        result[index] = 0

    return result
