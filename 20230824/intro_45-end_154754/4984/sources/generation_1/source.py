def exploreIsland(grid, i, j, visited):
    # Mark current cell as visited
    visited[i][j] = True

    # If the current cell is not land, return
    if grid[i][j] != 'L':
        return

    # Check the adjacent cells
    # Up
    if i > 0 and not visited[i - 1][j]:
        exploreIsland(grid, i - 1, j, visited)
    # Down
    if i < len(grid) - 1 and not visited[i + 1][j]:
        exploreIsland(grid, i + 1, j, visited)
    # Left
    if j > 0 and not visited[i][j - 1]:
        exploreIsland(grid, i, j - 1, visited)
    # Right
    if j < len(grid[0]) - 1 and not visited[i][j + 1]:
        exploreIsland(grid, i, j + 1, visited)

def countIslands(grid):
    # Initialize visited matrix
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize count of islands
    count = 0

    # Traverse the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If a land cell is found that has not been visited, it is a new island
            if grid[i][j] == 'L' and not visited[i][j]:
                exploreIsland(grid, i, j, visited)
                count += 1

    return count

# Read the number of rows and columns
r, c = map(int, input().split())

# Read the image/grid
grid = [list(input()) for _ in range(r)]

# Count the minimum number of islands
min_islands = countIslands(grid)

# Print the result
print(min_islands)