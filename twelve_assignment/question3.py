class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findNthFromEnd(head, N):
    fast = slow = head

    # Move fast pointer N nodes ahead
    for _ in range(N):
        if fast is None:
            return None  # Linked list does not have N nodes
        fast = fast.next

    # Move both pointers simultaneously
    while fast:
        fast = fast.next
        slow = slow.next

    return slow