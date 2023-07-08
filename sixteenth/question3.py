def deleteMiddle(stack):
    middleIndex = len(stack) // 2
    deleteMiddleRecursive(stack, middleIndex, 0)

def deleteMiddleRecursive(stack, middleIndex, currentIndex):
    if currentIndex == middleIndex:
        stack.pop()
        return

    temp = stack.pop()
    deleteMiddleRecursive(stack, middleIndex, currentIndex + 1)
    stack.append(temp)
