class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_alternate_k(head, k):
    if not head or k <= 1:
        return head
    
    prev = None
    curr = head
    count = 0

    # Reverse k nodes
    while curr and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1
    
    # Link reversed k nodes with the remaining list
    if curr is not None:
        head.next = reverse_alternate_k(curr, k)
    
    return prev
