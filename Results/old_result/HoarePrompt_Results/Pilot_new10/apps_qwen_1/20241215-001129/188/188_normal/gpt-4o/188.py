n = int(input())
cards = [int(input()) for _ in range(n)]

from collections import Counter

# Count the frequency of each number on the cards
count = Counter(cards)

# Find all unique numbers and sort them by their frequency
unique_numbers = sorted(count.keys(), key=lambda x: count[x])

# Check if we can find two distinct numbers such that each appears n/2 times
if len(unique_numbers) < 2:
    print("NO")
else:
    # Check if the two most frequent numbers each appear exactly n/2 times
    if count[unique_numbers[-1]] == n // 2 and count[unique_numbers[-2]] == n // 2:
        print("YES")
        print(unique_numbers[-1], unique_numbers[-2])
    else:
        print("NO")
