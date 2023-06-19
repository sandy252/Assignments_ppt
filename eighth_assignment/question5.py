def compress(chars):
    write = 0
    count = 1

    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            count += 1
        else:
            chars[write] = chars[i-1]
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            count = 1

    chars[write] = chars[-1]
    write += 1
    if count > 1:
        for digit in str(count):
            chars[write] = digit
            write += 1

    return write


chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
print(compress(chars))