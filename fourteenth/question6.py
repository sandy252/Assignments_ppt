class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def left_shift_linked_list(head, k):
    if not head or k == 0:
        return head
    
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    k %= length
    if k == 0:
        return head
    
    current = head
    for _ in range(k):
        current = current.next
    
    new_head = current
    while current.next:
        current = current.next
    
    current.next = head
    new_end = current
    new_end.next = None
    
    return new_head
