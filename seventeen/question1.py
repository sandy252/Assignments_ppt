def firstUniqChar(s):
    char_count = {}  # Dictionary to store character count

    # Count the occurrences of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the index of the first non-repeating character
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i

    return -1  # If there are no non-repeating characters

# Example usage
input_string = "leetcode"
print(firstUniqChar(input_string))  # Output: 0
