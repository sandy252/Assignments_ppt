def count_consonants(string):
    if len(string) == 0:
        return 0
    else:
        first_char = string[0].lower()
        if first_char.isalpha() and first_char not in "aeiou":
            return 1 + count_consonants(string[1:])
        else:
            return count_consonants(string[1:])

print(count_consonants("Hello, World!"))