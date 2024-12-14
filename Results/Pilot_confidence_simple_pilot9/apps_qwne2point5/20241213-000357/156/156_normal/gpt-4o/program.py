def find_lara_position(n, m, k):
    if k < n - 1:
        # Still in the initial descent down the first column
        print(k + 1, 1)
    else:
        # Adjust k by removing the initial descent
        k -= (n - 1)
        # Determine which full zigzag row Lara is in
        full_rows = k // (m - 1)
        # Determine the remaining steps after full zigzag rows
        remaining_steps = k % (m - 1)
        
        if full_rows % 2 == 0:
            # If on an even full row, moving rightward
            row = n - full_rows
            col = 2 + remaining_steps
        else:
            # If on an odd full row, moving leftward
            row = n - full_rows
            col = m - remaining_steps
        
        print(row, col)

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
n, m, k = int(data[0]), int(data[1]), int(data[2])

# Find Lara's position
find_lara_position(n, m, k)
