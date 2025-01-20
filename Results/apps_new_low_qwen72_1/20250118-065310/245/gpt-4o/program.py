# Read the input values
n = int(input())
x = int(input())

# Determine the initial position of the ball
# We need to reverse the sequence of moves

# To keep track of the position of the ball
position = x

# We iterate from n to 1 to reverse the moves
for i in range(n, 0, -1):
    if i % 2 == 1:  # Odd moves: swap left (0) and middle (1)
        if position == 0:
            position = 1
        elif position == 1:
            position = 0
    else:  # Even moves: swap middle (1) and right (2)
        if position == 1:
            position = 2
        elif position == 2:
            position = 1

# Print the initial position of the ball
print(position)
