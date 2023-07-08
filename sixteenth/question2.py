def sortStack(stack):
    tempStack = []

    while stack:
        temp = stack.pop()

        while tempStack and tempStack[-1] > temp:
            stack.append(tempStack.pop())

        tempStack.append(temp)

    return tempStack
