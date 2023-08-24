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
    elif i in pile:
        # If the number is in the pile, find its index and remove all cards before it
        index = pile.index(i)
        pile = pile[index+1:]
        # Increment the count variable by the number of cards removed from the pile
        count += index+1

# Print the minimum number of operations
print(count)