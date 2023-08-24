# Read the number of lines
n = int(input())

# Read the number of characters in each line
a = list(map(int, input().split()))

# Read the initial and final cursor positions
r1, c1, r2, c2 = map(int, input().split())

# Calculate the minimum number of moves to reach the final position
moves = abs(r1 - r2)

# If the initial and final positions are in different lines, add the number
# of characters in the initial line and the number of characters in the final
# line to the minimum number of moves
if r1 != r2:
    moves += a[r1] + a[r2]

# Add the number of moves required to reach the final column from the initial
# column in the initial line
moves += abs(c1 - c2)

# Print the minimum number of moves
print(moves)