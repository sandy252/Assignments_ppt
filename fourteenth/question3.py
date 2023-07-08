class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None


def flatten_linked_list(head):
    # If the list is empty or has only one node, return the head as it is
    if head is None or head.next is None:
        return head
    
    # Merge two sorted linked lists
    def merge_lists(list1, list2):
        # If one of the lists is empty, return the other list
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        # Choose the smaller node as the head of the merged list
        if list1.data <= list2.data:
            result = list1
            result.bottom = merge_lists(list1.bottom, list2)
        else:
            result = list2
            result.bottom = merge_lists(list1, list2.bottom)
        
        return result
    
    # Merge bottom sub-linked lists recursively
    def merge_bottom(head1, head2):
        # If one of the lists is empty, return the other list
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        
        # Merge the bottom sub-linked lists and return the head
        if head1.data <= head2.data:
            head1.bottom = merge_bottom(head1.bottom, head2)
            return head1
        else:
            head2.bottom = merge_bottom(head1, head2.bottom)
            return head2
    
    # Step 1: Merge the sub-linked lists one by one from left to right
    current = head
    while current.next is not None:
        head1 = current
        head2 = current.next
        
        # Merge the current and next sub-linked lists
        merged_head = merge_bottom(head1, head2)
        
        # Update the next pointer to the merged list
        current.next = merged_head
        
        # Move to the next pair of sub-linked lists
        current = current.next
    
    # Step 2: Return the head of the flattened linked list
    return head
