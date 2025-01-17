n, m = map(int, input().split())

# Initialize the current number of grains in the barn
current_grains = n

# Initialize the day counter
day = 0

# Loop until the barn becomes empty
while current_grains > 0:
    day += 1
    # Add m grains to the barn
    current_grains = min(n, current_grains + m)
    # Sparrows eat the grains
    current_grains -= day

# Output the day when the barn becomes empty
print(day)
