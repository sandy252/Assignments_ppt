# 29. Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.
def is_palidrome(string):
    rev = string[::-1]
    # r = ""
    # for e in string:
    #     r = e + r
    # print(r)

    if rev == string:
        return True
    else:
        return False
    
print(is_palidrome("manam"))