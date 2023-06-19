class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def isPalindrome(head):
    if not head or not head.next:
        return True

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    second_half = prev
    first_half = head

    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True
