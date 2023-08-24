# Check the left adjacent tile
if j > 0:
    adjacent_tiles.append(grid[i][j-1])

# Check the top adjacent tile
if i > 0:
    adjacent_tiles.append(grid[i-1][j])

# Check the top left adjacent tile
if i > 0 and j > 0:
    adjacent_tiles.append(grid[i-1][j-1])

# Check the right adjacent tile
if j < 12:
    adjacent_tiles.append(grid[i][j+1])