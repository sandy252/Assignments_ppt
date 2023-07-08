class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def delete_node_at_position(head, position):
    if not head:
        return head
    
    if position == 0:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head
    
    current = head
    count = 0

    while current and count < position:
        current = current.next
        count += 1
    
    if not current:
        return head
    
    current.prev.next = current.next
    if current.next:
        current.next.prev = current.prev
    
    return head
