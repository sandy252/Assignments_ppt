def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []

    count = {}
    for num in changed:
        count[num] = count.get(num, 0) + 1

    original = []
    sorted_changed = sorted(changed)

    for num in sorted_changed:
        if count.get(num, 0) > 0 and count.get(num * 2, 0) > 0:
            original.append(num)
            count[num] -= 1
            count[num * 2] -= 1
        elif count.get(num, 0) < 0:
            return []

    return original



print(findOriginalArray([1,3,4,2,6,8]))