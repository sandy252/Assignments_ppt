class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    # If the list is empty or has only one node, return the head as it is
    if not head or not head.next:
        return head

    # Create two pointers for odd and even groups
    odd = head
    even = head.next
    even_head = even

    # Traverse the list and group the nodes based on odd and even indices
    while even and even.next:
        # Connect odd nodes
        odd.next = even.next
        odd = odd.next

        # Connect even nodes
        even.next = odd.next
        even = even.next

    # Connect the end of the odd group to the start of the even group
    odd.next = even_head

    return head
