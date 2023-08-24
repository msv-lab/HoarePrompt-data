# Read the value of N and the list of cards
N = int(input())
cards = list(map(int, input().split()))

# Sort the cards in ascending order
cards.sort()

# Calculate the sum of the first N-1 cards
snuke_sum = sum(cards[:-1])

# Calculate the sum of the last card
raccoon_sum = cards[-1]

# Calculate the difference between the sums
diff = abs(snuke_sum - raccoon_sum)

# Print the minimum possible difference
print(diff)