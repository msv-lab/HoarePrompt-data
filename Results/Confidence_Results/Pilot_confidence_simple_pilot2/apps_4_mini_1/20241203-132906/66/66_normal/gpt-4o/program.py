# Use Standard Input format

n = int(input())
arr = list(map(int, input().split()))

# Find the minimum value in the array
min_value = min(arr)

# List to store indices of the minimum value
min_indices = [i for i, x in enumerate(arr) if x == min_value]

# Calculate the minimum distance between consecutive minimum value indices
min_distance = min(min_indices[i+1] - min_indices[i] for i in range(len(min_indices) - 1))

print(min_distance)
