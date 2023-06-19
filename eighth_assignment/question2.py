def checkValidString(s):
    count = 0
    star_count = 0
    for char in s:
        if char == '(' or char == '*':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False

    count = 0
    for i in range(len(s) - 1, -1, -1):
        char = s[i]
        if char == ')' or char == '*':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
    
    return True


print(checkValidString("()"))