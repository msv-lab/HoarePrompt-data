# Read input values
n, k = map(int, input().split())
heights = list(map(int, input().split()))

actions = []  # List to store the actions

# Iterate from the second tree to the last tree
for i in range(1, n):
    diff = heights[i] - heights[i-1] - k  # Calculate the difference
    if diff < 0:
        actions.append(f"- {i+1} {abs(diff)}")  # Decrease the height
        heights[i] -= abs(diff)
    elif diff > 0:
        actions.append(f"+ {i+1} {diff}")  # Increase the height
        heights[i] += diff

# Print the number of actions required
print(len(actions))
# Print the actions in reverse order
for action in reversed(actions):
    print(action)