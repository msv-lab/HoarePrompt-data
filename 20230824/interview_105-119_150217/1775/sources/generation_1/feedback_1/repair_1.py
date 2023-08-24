n, m, k = map(int, input().split())

# Initialize a list to store the total number of each detail type in the army
total_details = [0] * m

# Initialize a list to store the number of shots for each detail type
shots = [0] * m

# Read the input droids and update the total_details list
for _ in range(n):
    droid_details = list(map(int, input().split()))
    for i in range(m):
        total_details[i] += droid_details[i]

# Find the maximum number of consecutive droids that can be destroyed
max_destroyed = min(k, n)

# Calculate the maximum number of shots that can be made for each detail type
max_shots = min(k // max_destroyed, min(total_details))

# Distribute the shots among the detail types as evenly as possible
for i in range(m):
    if max_destroyed == 0:
        break
        
    # Calculate the number of shots for each detail type
    shots[i] = min(total_details[i], max_shots)
    max_destroyed -= shots[i]
    total_details[i] -= shots[i]

# Print the number of shots for each detail type
print(*shots)