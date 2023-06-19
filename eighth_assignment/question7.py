def decodeString(s):
    stack = []

    for c in s:
        if c.isdigit():
            stack.append(int(c))
        elif c == '[':
            stack.append(c)
        elif c == ']':
            encoded_str = ''
            while stack[-1] != '[':
                encoded_str = stack.pop() + encoded_str

            stack.pop()  # Pop '['

            num = stack.pop()
            decoded_str = encoded_str * num
            stack.append(decoded_str)
        else:
            stack.append(c)

    return ''.join(stack)


print(decodeString("3[a]2[bc]")) 