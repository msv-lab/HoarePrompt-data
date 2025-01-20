def find_bomb_placement():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    grid = []
    index = 2
    for i in range(n):
        grid.append(data[index])
        index += 1

    # Count the number of walls in each row and each column
    row_walls = [0] * n
    col_walls = [0] * m
    
    total_walls = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                row_walls[i] += 1
                col_walls[j] += 1
                total_walls += 1

    # Check every cell to see if placing a bomb there will destroy all walls
    for i in range(n):
        for j in range(m):
            if row_walls[i] + col_walls[j] - (1 if grid[i][j] == '*' else 0) == total_walls:
                print("YES")
                print(i + 1, j + 1)
                return

    print("NO")

# Call the function to execute the solution
find_bomb_placement()
