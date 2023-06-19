def permute(string, left, right):
    if left == right:
        print(''.join(string))

    for i in range(left, right + 1):
        string[left], string[i] = string[i], string[left]  # Swap
        permute(string, left + 1, right)
        string[left], string[i] = string[i], string[left]  # Backtrack


S = "abc"
permute(list(S), 0, len(S) - 1)
