# Read the input values
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# Calculate the minimal number of steps
steps = max(abs(x2 - x1), abs(y2 - y1))

# Print the result
print(steps)
