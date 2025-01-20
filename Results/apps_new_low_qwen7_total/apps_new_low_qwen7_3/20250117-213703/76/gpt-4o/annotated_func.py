#State of the program right berfore the function call: The input consists of two positive integers n and m where 1 ≤ n, m ≤ 1000, representing the dimensions of the depot field. Following these, there are n lines, each containing m symbols "." and "*", representing the cells of the field where "." is an empty cell and "*" is a cell occupied by a wall.
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
        
    #State of the program after the  for loop has been executed: grid is a list of n+index lists, where the first n lists are the original content, and the last index lists are from data, index is n, i is n-1.
    row_walls = [0] * n

col_walls = [0] * m

total_walls = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                row_walls[i] += 1
                col_walls[j] += 1
                total_walls += 1
        
    #State of the program after the  for loop has been executed: Output State: `total` is 0, `grid` is a list of \( n + \text{index} \) lists, `index` is \( n \), `i` is \( n \), `row_walls` is a list of \( n \) integers where each integer represents the count of `'*'` in the corresponding row, `col_walls` is a list of \( m \) integers where each integer represents the count of `'*'` in the corresponding column, `total_walls` is the number of `'*'` in the grid, `j` is \( m - 1 \).
    #
    #Explanation:
    #1. **Analyze the Code and Initial State**:
    #   - The loop iterates over the rows and columns of the grid.
    #   - For each cell `grid[i][j]`, if it contains '*', the corresponding row and column walls are incremented, and the total walls counter is incremented.
    #
    #2. **Track Variable Changes**:
    #   - **Invariant Variables**:
    #     - `index`: This remains constant as \( n \) throughout the loop.
    #     - `i`: This becomes \( n \) after the loop completes.
    #     - `j`: This starts at \( n-1 \) and increments until \( m-1 \). After the loop, `j` will be \( m-1 \).
    #   - **Variables Updated During the Loop**:
    #     - `row_walls`: Each element in this list is incremented based on the number of '*' in the corresponding row.
    #     - `col_walls`: Each element in this list is incremented based on the number of '*' in the corresponding column.
    #     - `total_walls`: This is incremented each time a '*' is found in the grid.
    #
    #3. **Summarize the Loop Behavior**:
    #   - The loop will execute for each '*’ in the grid. Therefore, the number of iterations is equal to the number of '*' in the grid.
    #   - After the loop, `i` will be \( n \) because it is only updated once the inner loop completes.
    #   - `j` will be \( m-1 \) after the inner loop completes.
    #   - `row_walls` and `col_walls` will contain the counts of '*' for each row and column, respectively.
    #   - `total_walls` will hold the total number of '*' in the grid.
    #
    #4. **Verify Relationships**:
    #   - The relationships and invariants identified are consistent with the given output states. The loop correctly increments the wall counts and the total wall count based on the presence of '*'.
    for i in range(n):
        for j in range(m):
            if row_walls[i] + col_walls[j] - (1 if grid[i][j] == '*' else 0
                ) == total_walls:
                print('YES')
                print(i + 1, j + 1)
                return
        
    #State of the program after the  for loop has been executed: `total` is 0, `grid` is a list of \( n + \text{index} \) lists, `index` is \( n \), `i` is \( n \), `row_walls` is a list of \( n \) integers containing the count of `'*'` in each row, `col_walls` is a list of \( m \) integers containing the count of `'*'` in each column, `total_walls` is the total number of `'*'` in the grid, `j` is 0.
    print('NO')
#Overall this is what the function does:The function reads a grid of characters representing a depot field from standard input, where '.' represents an empty cell and '*' represents a cell occupied by a wall. It then calculates the number of walls in each row and column and the total number of walls. The function checks if for each cell in the grid, the sum of the number of walls in its row and column minus one (if the cell itself is a wall) equals the total number of walls. If such a cell is found, the function prints 'YES' followed by the coordinates of the cell (1-indexed) and returns. If no such cell is found, the function prints 'NO' and returns. The function does not accept any parameters and does not return any value.

