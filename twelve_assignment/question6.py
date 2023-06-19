class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def deleteNodes(head, M, N):
    if M == 0:
        return None

    current = head

    while current:
        # Traverse M nodes
        for _ in range(M - 1):
            if current:
                current = current.next
            else:
                break

        # Delete N nodes
        temp = current
        for _ in range(N):
            if temp and temp.next:
                temp = temp.next
            else:
                break
        if temp:
            current.next = temp.next
        else:
            current.next = None

        # Move to the next position
        if current:
            current = current.next

    return head


# Create the linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)
node10 = ListNode(10)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

M = 2
N = 3

updated_head = deleteNodes(head, M, N)

# Print the updated linked list
current = updated_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
