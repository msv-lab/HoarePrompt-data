n = int(input())
hand = list(map(int, input().split()))
pile = list(map(int, input().split()))

# Initialize the count variable to keep track of the minimum number of operations
count = 0

# Iterate from 1 to n and check if the current number is in the hand or pile
for i in range(1, n+1):
    if i in hand:
        # If the number is in the hand, remove it from the hand
        hand.remove(i)
    elif pile and i in pile:
        # If the number is in the pile and the current pile on the top is not empty
        # Find the index of the number in the remaining pile, remove all cards before it, and update the pile
        index = pile[pile.index(i)+1:]
        pile = pile[index:]
        # Increment the count variable by the number of cards removed from the pile
        count += len(index)

# Print the minimum number of operations
print(count)