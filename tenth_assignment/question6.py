def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return 1
    else:
        moves = 0
        moves += tower_of_hanoi(n - 1, source, destination, auxiliary)
        print("Move disk", n, "from rod", source, "to rod", destination)
        moves += 1
        moves += tower_of_hanoi(n - 1, auxiliary, source, destination)
        return moves


n = 3  
source = 1
auxiliary = 2  
destination = 3  

total_moves = tower_of_hanoi(n, source, auxiliary, destination)
print("Total moves:", total_moves)