class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddleNode(head):
    if not head or not head.next:
        return None

    slow = fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    if prev is None:
        head = slow.next
    else:
        prev.next = slow.next

    return head

# Example usage:
# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = deleteMiddleNode(head)

# Print the modified linked list: 1 -> 2 -> 4 -> 5
current = head
while current:
    print(current.val, end=" ")
    current = current.next
