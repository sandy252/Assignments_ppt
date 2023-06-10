def print_all_subsets(s, subset=""):
    count = 0
    if len(s) == 0:
        print(subset)
    else:
        # Include the first character and recursively generate subsets
        print_all_subsets(s[1:], subset + s[0])
        
        # Exclude the first character and recursively generate subsets
        print_all_subsets(s[1:], subset)
    return count

print(print_all_subsets("abc"))