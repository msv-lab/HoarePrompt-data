from collections import deque

def solve(s):
    # Check if the string length is not 27, return "Impossible"
    if len(s) != 27:
        return "Impossible"
    
    # Create a grid with empty spaces
    grid = [['' for _ in range(13)] for _ in range(2)]
    
    # Create a queue to store the tiles
    queue = deque(list(s))
    
    # Place the first tile in the top left corner of the grid
    grid[0][0] = queue.popleft()
    
    # Iterate over the grid to fill in the tiles
    for i in range(2):
        for j in range(13):
            # Skip the top left corner tile
            if i == 0 and j == 0:
                continue
            
            # Check if there are tiles in the queue
            if not queue:
                break
            
            # Get the adjacent tiles
            adjacent_tiles = []
            
            # Check the left adjacent tile
            if j > 0:
                adjacent_tiles.append(grid[i][j-1])
            
            # Check the top adjacent tile
            if i > 0:
                adjacent_tiles.append(grid[i-1][j])
            
            # Check the top left adjacent tile
            if i > 0 and j > 0:
                adjacent_tiles.append(grid[i-1][j-1])
            
            # Find a tile in the queue that is adjacent to the current position
            while queue:
                tile = queue.popleft()
                if tile in adjacent_tiles:
                    grid[i][j] = tile
                    break
            
            # If no tile is found, return "Impossible"
            if not grid[i][j]:
                return "Impossible"
    
    # Check if there are tiles remaining in the queue
    if queue:
        return "Impossible"
    
    # Convert the grid to strings
    rows = [''.join(row) for row in grid]
    
    # Return the resulting grid as a string
    return '\n'.join(rows)


s = input()
result = solve(s)
print(result)