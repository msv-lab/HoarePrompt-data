# Read input values
v1, v2 = map(int, input().split())
t, d = map(int, input().split())

# Initialize the list to store the speeds at each second
speeds = [0] * t

# Set the speed at the first second
speeds[0] = v1

# Set the speed at the last second
speeds[-1] = v2

# Calculate maximum possible speeds in between
for i in range(1, t):
    speeds[i] = min(speeds[i-1] + d, v2 + (t - i - 1) * d)

# Calculate total distance traveled
total_distance = sum(speeds)

# Print the result
print(total_distance)
