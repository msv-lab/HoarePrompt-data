n = int(input())

safe_cells = []

# Add the bottom-left cell
safe_cells.append(1)

# Add the bottom row
for i in range(1, n+1):
    safe_cells.append(2*i)

# Add the left column
for i in range(1, n+1):
    safe_cells.append(2*n + 2*i - 1)

# Add the top row
for i in range(1, n+1):
    safe_cells.append(4*n + 2 - 2*i)

# Add the right column
for i in range(1, n+1):
    safe_cells.append(4*n + 4 - 2*i)

# Add the top-right cell
safe_cells.append(4*n + 4)

# Print the number of safe cells
print(len(safe_cells))

# Print the indices of the safe cells
for cell in safe_cells:
    print(cell, end=' ')
