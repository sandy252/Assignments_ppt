class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def remove_loop(head):
    # If the list is empty or has only one node, or there is no loop, return the head as it is
    if head is None or head.next is None:
        return head
    
    # Step 1: Detect the loop in the linked list using Floyd's Cycle-Finding Algorithm
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    # If there is no loop, return the head as it is
    if slow != fast:
        return head
    
    # Step 2: Find the starting point of the loop
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    
    # Step 3: Remove the loop by setting the next pointer of the last node to None
    fast.next = None
    
    return head
