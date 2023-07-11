def valid_palidrome(string):
    rev= string[::-1]
    if string == rev:
        return True
    else:
        return False
    
print(valid_palidrome('manAm'))