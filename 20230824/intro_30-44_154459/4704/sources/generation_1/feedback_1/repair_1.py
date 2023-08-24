# Read the value of N and the list of cards
N = int(input())
cards = list(map(int, input().split()))

# Check if the number of cards is less than 2
if N < 2:
    print(0)
    exit()

# Check if all the cards have the same value
if len(set(cards)) == 1:
    print(0)
    exit()

# Sort the cards in ascending order
cards.sort()

# Initialize the minimum difference to a large value
min_diff = float('inf')

# Iterate over all possible choices of the number of cards Snuke takes
for i in range(1, N):
    snuke_sum = sum(cards[:i])
    raccoon_sum = sum(cards[i:])
    diff = abs(snuke_sum - raccoon_sum)
    min_diff = min(min_diff, diff)

# Print the minimum possible difference
print(min_diff)