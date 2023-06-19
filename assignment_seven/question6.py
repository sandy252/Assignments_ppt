def canConvertString(s, goal):
    if len(s) != len(goal):
        return False

    concat = s + s
    return goal in concat

print(canConvertString("abcde", "bcdea"))