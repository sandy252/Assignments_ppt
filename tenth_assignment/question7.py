def print_permutations(string, current=""):
    if len(string) == 0:
        print(current)
    else:
        for i in range(len(string)):
            remaining = string[:i] + string[i+1:]
            print_permutations(remaining, current + string[i])

print_permutations("abc")
