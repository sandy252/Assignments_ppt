#  22. Implement a function to find the first non-repeating character in a string.

def first_non_repeating(string):
    for i in range(len(string)):
        if string[i] not in string[i+1:]:
            return string[i]
    return 0
        


print(first_non_repeating("saasp"))