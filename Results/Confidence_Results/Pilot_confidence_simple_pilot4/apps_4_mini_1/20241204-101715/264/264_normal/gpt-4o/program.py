# Reading inputs
n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]

# Calculate the initial maximum and total people sitting on benches
initial_max = max(a)
total_people = sum(a)

# Calculate maximum possible k
max_k = initial_max + m

# Calculate minimum possible k
# Distribute m people evenly to make the smallest possible increase in the maximum
min_k = (total_people + m + n - 1) // n  # This is the ceiling of (total_people + m) / n

# Output the results
print(min_k, max_k)
