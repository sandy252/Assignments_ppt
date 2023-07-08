class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    # Create a dummy node to handle the case where the head needs to be removed
    dummy = ListNode(0)
    dummy.next = head

    # Create a dictionary to store the running sum and its corresponding node
    sum_dict = {}
    prefix_sum = 0
    current = dummy

    # Traverse the list and calculate the running sum
    while current:
        prefix_sum += current.val

        # If the running sum exists in the dictionary, remove the sublist from the previous node to the current node
        if prefix_sum in sum_dict:
            node_to_remove = sum_dict[prefix_sum].next
            running_sum = prefix_sum + node_to_remove.val

            # Remove the sublist from the previous node to the current node
            while running_sum != prefix_sum:
                del sum_dict[running_sum]
                node_to_remove = node_to_remove.next
                running_sum += node_to_remove.val

            # Connect the previous node to the node after the sublist
            sum_dict[prefix_sum].next = node_to_remove.next
        else:
            # Add the running sum and the corresponding node to the dictionary
            sum_dict[prefix_sum] = current

        current = current.next

    return dummy.next
