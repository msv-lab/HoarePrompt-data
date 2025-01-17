# Function to calculate the maximum messiness
def max_messiness(n, k):
    # Maximum number of pairs in a fully reversed list
    max_pairs = n * (n - 1) // 2
    
    # If k is large enough to allow full reversal, return max_pairs
    if k >= max_pairs:
        return max_pairs
    
    # Otherwise, the maximum messiness we can achieve with k swaps
    return k

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
k = int(data[1])

# Calculating and printing the result
print(max_messiness(n, k))
