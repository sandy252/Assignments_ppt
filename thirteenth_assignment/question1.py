class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_new_linked_list(head1, head2):
    # Initialize the head and tail of the new linked list
    new_head = None
    new_tail = None
    
    # Traverse both linked lists simultaneously
    while head1 is not None and head2 is not None:
        # Find the greater node
        if head1.data >= head2.data:
            greater_node = head1
            head1 = head1.next
        else:
            greater_node = head2
            head2 = head2.next
        
        # Create a new node with the greater value
        new_node = Node(greater_node.data)
        
        # If new linked list is empty, set new_head and new_tail to the new node
        if new_head is None:
            new_head = new_node
            new_tail = new_node
        else:
            # Append the new node to the new linked list
            new_tail.next = new_node
            new_tail = new_node
    
    # If any of the linked lists still has remaining nodes, append them to the new linked list
    if head1 is not None:
        if new_tail is None:
            new_head = head1
        else:
            new_tail.next = head1
    elif head2 is not None:
        if new_tail is None:
            new_head = head2
        else:
            new_tail.next = head2
    
    return new_head
