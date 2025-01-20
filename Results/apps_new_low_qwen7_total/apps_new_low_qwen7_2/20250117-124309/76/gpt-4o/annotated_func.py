#State of the program right berfore the function call: The input consists of two positive integers n and m (1 ≤ n, m ≤ 1000) representing the number of rows and columns in the depot field. The following n lines contain m symbols "." and "*" each, representing the cells in the field. Each symbol "." indicates an empty cell, and each symbol "*" indicates a cell occupied by a wall.
def func_1():
    input = sys.stdin.read

data = input().split()

n = int(data[0])

m = int(data[1])

grid = []

index = 2
    for i in range(n):
        grid.append(data[index])
        
        index += 1
        
    #State of the program after the  for loop has been executed: i is n-1, grid contains [data[2], data[3], ..., data[n+1]], index is 2 + n.
    row_walls = [0] * n

col_walls = [0] * m

total_walls = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                row_walls[i] += 1
                col_walls[j] += 1
                total_walls += 1
        
    #State of the program after the  for loop has been executed: Output State: `i` is `n-1`, `m` is greater than 0, `row_walls[i]` is equal to the number of columns `j` where `grid[i][j]` is '*', `col_walls[j]` is equal to the number of rows `i` where `grid[i][j]` is '*', and `total_walls` is the sum of all `row_walls[i]` values (or equivalently, the sum of all `col_walls[j]` values).
    #
    #Explanation:
    #- The loop iterates over every element in the grid. The variable `i` starts at `n-1` and decreases until it reaches 0. The inner loop iterates over each column `j`.
    #- If `grid[i][j]` is '*', then `row_walls[i]` and `col_walls[j]` are incremented, and `total_walls` is also incremented.
    #- The loop continues to execute as long as there are elements in the grid that are '*'. Once all elements in the grid are checked, the loop stops.
    #
    #By the time the loop completes, `i` will be 0 because the loop decrements `i` from `n-1` to 0. The value of `m` remains unchanged since it is an invariant throughout the loop. The `row_walls` and `col_walls` arrays are updated based on the occurrences of '*' in the grid, and `total_walls` reflects the total count of '*' in the grid.
    #
    #Thus, the final state of the program after the loop has executed is as described above.
    for i in range(n):
        for j in range(m):
            if row_walls[i] + col_walls[j] - (1 if grid[i][j] == '*' else 0
                ) == total_walls:
                print('YES')
                print(i + 1, j + 1)
                return
        
    #State of the program after the  for loop has been executed: `i` is `0`, `m` is greater than 0, `row_walls[i]` is the total count of '*' in the last row `n-1`, `col_walls[j]` is the total count of '*' in columns `j` where `0 <= j < m`, and `total_walls` is the sum of all `row_walls[i]` values (or equivalently, the sum of all `col_walls[j]` values).
    print('NO')
#Overall this is what the function does:The function `func_1` processes a depot field grid consisting of `n` rows and `m` columns. Each cell in the grid is either an empty cell (`"."`) or a cell occupied by a wall (`"*"`). The function calculates the number of walls in each row and column and then checks if there is a cell `(i, j)` such that the sum of the walls in row `i` and column `j` minus one (if the cell itself is a wall) equals the total number of walls in the grid. If such a cell is found, the function prints 'YES' followed by the coordinates of the cell `(i+1, j+1)` and returns `None`. If no such cell is found, the function prints 'NO' and returns `None`.

The function accepts no parameters directly but relies on input read from standard input. It reads the dimensions of the grid (`n` and `m`), followed by the grid itself, and processes the grid according to the specified conditions. If the grid is such that the sum of walls in any row and column (considering the cell itself if it is a wall) matches the total number of walls, the function indicates this by printing 'YES' and the coordinates. Otherwise, it prints 'NO'.

Potential edge cases include:
- If the grid is empty (`n = 0` or `m = 0`), the function still processes the grid and prints 'NO'.
- If all cells are empty (`"."`), the function prints 'NO'.
- If the grid has no walls (`"*"`), the function also prints 'NO'.
- The function handles the case where the sum condition is met exactly, indicating the presence of a valid cell.

