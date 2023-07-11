def palindrome(string):
    rev = string[::-1]
    if rev == string:
        return "palindrome"
    else:
        return "not palindrome"
    

print(palindrome("sandeep"))
print(palindrome("naman"))