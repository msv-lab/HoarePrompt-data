# Read input
N = int(input())
heights = list(map(int, input().split()))

# Initialize the number of watering operations
num_operations = 0

# Iterate through the flowers
for i in range(N-1):
    # Check if the next flower is shorter than the current flower
    if heights[i+1] < heights[i]:
        # Increase the height of the next flower to match the current flower
        heights[i+1] = heights[i]
        # Increase the number of watering operations
        num_operations += 1

# Print the minimum number of watering operations required
print(num_operations)