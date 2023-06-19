class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectAndRemoveLoop(head):
    if not head or not head.next:
        return head

    slow = fast = head
    loop_exists = False

    # Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_exists = True
            break

    # If loop exists, remove it
    if loop_exists:
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None

    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

head.next.next.next.next.next.next = head.next.next

head = detectAndRemoveLoop(head)

current = head
while current:
    print(current.val, end=" ")
    current = current.next
