def count_contiguous_substrings(S):
    return count_substrings(S, 0, len(S) - 1)

def count_substrings(S, start, end):
    # Base cases
    if start > end:
        return 0
    elif start == end:
        return 1

    count = count_substrings(S, start, end - 1)  # Count substrings without considering the last character

    # Check if the last character is the same as the starting character
    if S[start] == S[end]:
        count += 1

    return count

print(count_contiguous_substrings("abc"))