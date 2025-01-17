# Read input values
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Initialize variables to track the bounding box of the black cells ('B')
top, bottom, left, right = n, -1, m, -1

# Find the bounding box of the black cells
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'B':
            top = min(top, i)
            bottom = max(bottom, i)
            left = min(left, j)
            right = max(right, j)

# If no black cells were found, paint one cell black
if top > bottom or left > right:
    print(1)
else:
    # Calculate the size of the bounding box
    height = bottom - top + 1
    width = right - left + 1
    
    # The side length of the square should be the maximum of height and width
    side_length = max(height, width)
    
    # Check if the square can fit within the grid
    if side_length > n or side_length > m:
        print(-1)
    else:
        # Calculate the number of white cells that need to be painted black
        total_cells = side_length * side_length
        existing_black_cells = 0
        
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                if grid[i][j] == 'B':
                    existing_black_cells += 1
                    
        print(total_cells - existing_black_cells)
