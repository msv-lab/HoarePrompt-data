# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
groups = list(map(int, data[2:]))

# Calculate the number of rows and the maximum pairs per row
max_pairs_per_row = 4 * n

# Count the total number of pairs needed
total_pairs_needed = 0
for soldiers in groups:
    total_pairs_needed += (soldiers + 1) // 2

# Check if the total pairs needed can fit into the available pairs
if total_pairs_needed <= max_pairs_per_row:
    print("YES")
else:
    print("NO")
