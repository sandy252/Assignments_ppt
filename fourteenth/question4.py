class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
    
    node_map = {}

    # Create a copy of each node
    current = head
    while current:
        copy_node = Node(current.val)
        node_map[current] = copy_node
        current = current.next

    # Set next and random pointers of the copied nodes
    current = head
    while current:
        copy_node = node_map[current]
        copy_node.next = node_map.get(current.next)
        copy_node.random = node_map.get(current.random)
        current = current.next
    
    return node_map[head]
