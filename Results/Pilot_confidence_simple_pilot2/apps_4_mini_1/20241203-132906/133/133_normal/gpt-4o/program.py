# Use Standard Input format

# Read input
n = int(input())
angles = list(map(int, input().split()))

# Calculate the total sum of the angles
total_sum = sum(angles)

# Initialize variables to find the minimum difference
min_diff = float('inf')

# Iterate over all possible starting points for the first sector
for i in range(n):
    current_sum = 0
    for j in range(n):
        current_sum += angles[(i + j) % n]
        # Calculate the difference between the two sectors
        diff = abs(total_sum - 2 * current_sum)
        # Update the minimum difference
        if diff < min_diff:
            min_diff = diff

print(min_diff)
