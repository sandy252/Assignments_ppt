class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_one(head):
    if not head:
        return head
    
    # Reverse the linked list
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    # Add one to the reversed linked list
    carry = 1
    curr = prev
    while curr:
        sum_val = curr.val + carry
        curr.val = sum_val % 10
        carry = sum_val // 10
        curr = curr.next

    # If carry is still 1, add a new node with value 1
    if carry == 1:
        new_node = ListNode(1)
        prev.next = new_node

    # Reverse the linked list again
    new_head = None
    curr = prev
    while curr:
        next_node = curr.next
        curr.next = new_head
        new_head = curr
        curr = next_node
    
    return new_head
