#  12. Implement a function to check if a given string is an anagram of another string.

def is_anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
    
print(is_anagram("listen", "fdashg"))