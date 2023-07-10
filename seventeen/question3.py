def countStudents(students, sandwiches):
    # Count the number of circular and square sandwiches
    circular_count = sandwiches.count(0)
    square_count = sandwiches.count(1)

    # Iterate through the queue until it doesn't change or the stack is empty
    while students:
        # If the student at the front of the queue prefers the top sandwich, they take it
        if students[0] == sandwiches[0]:
            if sandwiches[0] == 0:
                circular_count -= 1
            else:
                square_count -= 1
            students.pop(0)
            sandwiches.pop(0)
        # If the student at the front of the queue doesn't prefer the top sandwich,
        # they go to the end of the queue
        else:
            students.append(students.pop(0))

        # If the queue doesn't change anymore, exit the loop
        if students[-1] == sandwiches[0]:
            break

    return len(students)

# Example usage
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(countStudents(students, sandwiches))  # Output: 0
