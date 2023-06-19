class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeAlternate(first_head, second_head):
    if not first_head or not second_head:
        return first_head

    first_current = first_head
    second_current = second_head

    while first_current and second_current:
        first_next = first_current.next
        second_next = second_current.next

        first_current.next = second_current
        second_current.next = first_next

        first_current = first_next
        second_current = second_next

    if second_current:
        first_current.next = second_current

    second_head = None

    return first_head

first_head = ListNode(5)
first_head.next = ListNode(7)
first_head.next.next = ListNode(17)
first_head.next.next.next = ListNode(13)
first_head.next.next.next.next = ListNode(11)

second_head = ListNode(12)
second_head.next = ListNode(10)
second_head.next.next = ListNode(2)
second_head.next.next.next = ListNode(4)
second_head.next.next.next.next = ListNode(6)

first_head = mergeAlternate(first_head, second_head)

current = first_head
while current:
    print(current.val, end=" ")
    current = current.next

current = second_head
while current:
    print(current.val, end=" ")
    current = current.next
