# 19. Write a program to remove all vowels from a given string.
def rem_vowels(string):
    vowels = ['a','e','i','o','u']
    string = string.lower()
    new = ""
    for s in string:
        if s not in vowels:
            new += s
    return new

print(rem_vowels('sand2646EEep'))