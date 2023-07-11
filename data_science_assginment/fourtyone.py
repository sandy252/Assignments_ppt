def is_palindrom(s):
    rev = s[::-1]
    if rev == s:
        return True
    else:
        return False
    

def longest_palindrome(string):
    m = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            sub = string[i:j]
            if is_palindrom(sub):
                l = len(sub)
                m =  max(l, m)
    return m

print(longest_palindrome("tomorrow"))


