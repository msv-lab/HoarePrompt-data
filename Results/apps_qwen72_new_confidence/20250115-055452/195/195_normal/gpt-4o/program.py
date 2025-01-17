# Reading input
n, a, b = map(int, input().split())
groups = list(map(int, input().split()))

# Initialize the number of denied people to 0
denied = 0

# Track the number of single seats occupied in two-seater tables
single_in_two_seater = 0

# Iterate through each group
for group in groups:
    if group == 1:
        if a > 0:
            # Use a one-seater table
            a -= 1
        elif b > 0:
            # Use a two-seater table
            b -= 1
            single_in_two_seater += 1
        elif single_in_two_seater > 0:
            # Use the remaining seat in a two-seater table
            single_in_two_seater -= 1
        else:
            # Deny service
            denied += 1
    elif group == 2:
        if b > 0:
            # Use a two-seater table
            b -= 1
        else:
            # Deny service to the whole group
            denied += 2

# Print the total number of denied people
print(denied)
