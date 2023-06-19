def findDuplicate(nums):
    slow = fast = nums[0]

    # Detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Find the meeting point
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1, 3, 4, 2, 2]
repeated_number = findDuplicate(nums)
print(repeated_number)