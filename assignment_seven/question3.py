def addStrings(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0:
        digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
        digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
        tempSum = digit1 + digit2 + carry
        carry = tempSum // 10
        result += str(tempSum % 10)
        i -= 1
        j -= 1

    if carry > 0:
        result += str(carry)

    return result[::-1]

print(addStrings("11","123"))