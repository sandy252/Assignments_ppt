def reconstruct_permutation(s):
    n = len(s)
    perm = []
    low, high = 0, n

    for c in s:
        if c == 'I':
            perm.append(low)
            low += 1
        elif c == 'D':
            perm.append(high)
            high -= 1

    perm.append(low)  
    return perm

print(reconstruct_permutation("IDID"))