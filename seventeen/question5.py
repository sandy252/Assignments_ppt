def find_winner(n, k):
    friends = list(range(1, n + 1))
    current_friend = 0

    while len(friends) > 1:
        current_friend = (current_friend + k - 1) % len(friends)
        friends.pop(current_friend)

    return friends[0]
