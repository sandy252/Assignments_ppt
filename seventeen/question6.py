import collections

def deckRevealedIncreasing(deck):
    deck.sort()  # Sort the deck in ascending order
    result = collections.deque()  # Result list to store the ordering of revealed cards

    # Start the simulation
    for card in reversed(deck):
        if result:  # If there are already revealed cards
            result.appendleft(result.pop())  # Move the top card to the bottom

        result.appendleft(card)  # Add the current card to the top of the deck

    return list(result)
