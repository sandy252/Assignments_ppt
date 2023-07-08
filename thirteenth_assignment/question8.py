class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def reverse_doubly_linked_list(head):
    # If the list is empty or has only one node, return the head as it is
    if head is None or head.next is None:
        return head
    
    # Initialize variables for traversal and reversal
    current = head
    new_head = None
    
    # Traverse the list and reverse the pointers
    while current is not None:
        next_node = current.next
        current.next = current.prev
        current.prev = next_node
        new_head = current
        current = next_node
    
    return new_head
