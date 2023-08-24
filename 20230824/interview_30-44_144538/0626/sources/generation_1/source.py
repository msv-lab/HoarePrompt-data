# Read the input
n = int(input())
a = list(map(int, input().split()))

# Initialize variables
direction_changes = 0
current_computer = 0
information_collected = 0

# Iterate through the computers
while information_collected < n:
    # If the current computer has information, collect it and update the count
    if a[current_computer] > 0:
        information_collected += 1
        a[current_computer] -= 1
    # Move to the next computer in the current direction
    if current_computer == 0 and a[current_computer] > 0:
        direction_changes += 1
    if current_computer == n - 1 and a[current_computer] > 0:
        direction_changes += 1
    if current_computer < n - 1 and a[current_computer] == 0 and a[current_computer + 1] > 0:
        direction_changes += 1
    if current_computer > 0 and a[current_computer] == 0 and a[current_computer - 1] > 0:
        direction_changes += 1
    if current_computer == 0 or a[current_computer - 1] == 0:
        current_computer += 1
    else:
        current_computer -= 1

# Print the result
print(direction_changes)