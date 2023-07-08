def reverse_stack(stack):
    if len(stack) <= 1:
        return stack
    else:
        top = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, top)
    return stack

def insert_at_bottom(stack, element):
    if len(stack) == 0:
        stack.append(element)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, element)
        stack.append(temp)
