class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_k_nodes(head, k):
    # If the list is empty or k is 1, no need to reverse, return the head as it is
    if head is None or k == 1:
        return head
    
    # Create dummy nodes for easy reversal of groups
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    
    # Initialize variables for reversing groups
    count = 0
    curr = head
    next_node = None
    
    # Calculate the length of the linked list
    length = 0
    temp = head
    while temp:
        temp = temp.next
        length += 1
    
    # Reverse k nodes at a time
    while curr:
        count += 1
        next_node = curr.next
        
        # Reverse the group of k nodes
        if count == k or (count < k and count == length):
            prev = reverse_group(prev, curr.next)
            count = 0
        
        curr = next_node
    
    return dummy.next

# Function to reverse a group of nodes
def reverse_group(prev, next_node):
    last_node = prev.next
    curr = prev.next.next
    while curr != next_node:
        next_temp = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = next_temp
    
    last_node.next = next_node
    return last_node
