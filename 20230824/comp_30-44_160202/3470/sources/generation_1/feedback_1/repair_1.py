n = int(input())

safe_cells = set()

# Calculate the indices of safe cells in the bottom row
for i in range(n+1):
    safe_cells.add(i)

# Calculate the indices of safe cells in the left column
for i in range(n+1, 2*n+1):
    safe_cells.add(2*n + i)

# Calculate the indices of safe cells in the top row
for i in range(2*n+1, 3*n+1):
    safe_cells.add(4*n + 3 - i)

# Calculate the indices of safe cells in the right column
for i in range(3*n+1, 4*n+1):
    safe_cells.add(4*n + 4*n + 4 - i)

# Sort the indices in increasing order
safe_cells = sorted(safe_cells)

# Print the number of safe cells
print(len(safe_cells))

# Print the indices of the safe cells
for cell in safe_cells:
    print(cell, end=' ')