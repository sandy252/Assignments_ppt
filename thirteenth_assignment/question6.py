def delete_last_occurrence(head, key):
    # If the list is empty, return None
    if head is None:
        return None
    
    # Traverse the linked list and keep track of the last occurrence of the key
    last_occurrence = None
    prev = None
    current = head
    while current is not None:
        if current.data == key:
            last_occurrence = prev
        prev = current
        current = current.next
    
    # If the key was not found, return the original head
    if last_occurrence is None:
        return head
    
    # If the last occurrence is the head, update the head to the next node
    if last_occurrence == head:
        head = head.next
    else:
        # Otherwise, skip the last occurrence by updating the previous node's next pointer
        last_occurrence.next = last_occurrence.next.next
    
    return head
