def evaluate_postfix(expression):
    stack = []

    # Traverse the expression
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, char)
            stack.append(result)

    return stack.pop()

def perform_operation(operand1, operand2, operator):
    if operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    else:
        raise ValueError('Invalid operator')

