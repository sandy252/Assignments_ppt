def reverseStr(s, k):
    chars = list(s)
    n = len(chars)
    start = 0

    while start < n:
        end = min(start + k, n)  # Calculate the end index for reversing
        chars[start:end] = reversed(chars[start:end])  # Reverse the portion

        start += 2 * k

    return ''.join(chars)

s = "abcdefg"
k = 2
print(reverseStr(s, k))
