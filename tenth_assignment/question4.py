def calculate_length(s):
    if s == "":
        return 0
    else:
        return 1 + calculate_length(s[1:])

print(calculate_length("Hello, world!"))