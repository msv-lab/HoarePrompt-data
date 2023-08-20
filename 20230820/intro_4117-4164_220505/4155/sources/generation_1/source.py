# Read input
N = int(input())
heights = list(map(int, input().split()))

# Initialize the number of watering operations
num_operations = 0

# Iterate through the flowers
for i in range(N-1):
    # Check if the current flower is taller than the next flower
    if heights[i] > heights[i+1]:
        # Calculate the difference in height between the current and next flower
        diff = heights[i] - heights[i+1]
        # Increase the height of the next flower by the difference
        heights[i+1] += diff
        # Increase the number of watering operations
        num_operations += diff

# Print the minimum number of watering operations required
print(num_operations)