# Read input
A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

# Initialize a 3x3 grid to mark the numbers
mark = [[False for _ in range(3)] for _ in range(3)]

# Mark the numbers from the input list on the grid
for b in B:
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                mark[i][j] = True

# Check if there is a bingo
bingo = False

# Check rows
for i in range(3):
    if all(mark[i]):
        bingo = True

# Check columns
for j in range(3):
    if all(mark[i][j] for i in range(3)):
        bingo = True

# Check diagonals
if mark[0][0] and mark[1][1] and mark[2][2]:
    bingo = True
if mark[0][2] and mark[1][1] and mark[2][0]:
    bingo = True

# Print the result
if bingo:
    print("Yes")
else:
    print("No")