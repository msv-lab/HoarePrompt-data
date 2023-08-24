def count_gold(map):
    max_gold = [0]  # Use a list to store the maximum gold
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Define directions inside the dfs function
    visited = set()
    
    # Helper function to check if a cell is valid
    def is_valid(x, y):
        return 0 <= x < len(map) and 0 <= y < len(map[0]) and map[x][y] != "#" and (x, y) not in visited
    
    # DFS function
    def dfs(x, y):
        visited.add((x, y))
        if map[x][y] == "G":
            max_gold[0] += 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                dfs(nx, ny)
        
        visited.remove((x, y))  # Remove the cell from visited when backtracking
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "P":
                dfs(i, j)
    
    return max_gold[0]


# Read the input
w, h = map(int, input().split())
map = [list(input()) for _ in range(h)]

# Calculate and print the maximum gold
print(count_gold(map))