def hasCycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Create the loop

has_cycle = hasCycle(head)
print(has_cycle)
