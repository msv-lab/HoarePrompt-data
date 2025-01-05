#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 1000, and grid is a list of strings where each string has a length of m consisting of characters '#' and '.' representing black and white cells respectively.
def func_1(n, m, grid):
    components, visited = 0, [([False] * m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == '#':
                components += dfs(i, j)
        
    #State of the program after the  for loop has been executed: `components` is the total number of connected components in the grid, `visited` reflects the explored positions in the grid, `grid` is an n by m grid containing '#' and other characters.
    return components
    #The program returns the total number of connected components in the grid
#Overall this is what the function does:The function accepts two integers `n` and `m`, and a list of strings `grid`, where each string represents a row of cells with '#' for black cells and '.' for white cells. It returns the total number of connected components of '#' cells in the grid. If there are no '#' cells, it will return 0, indicating no components are found.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 1000, and the grid is represented as a list of n strings, each of length m, consisting of characters '#' (black) and '.' (white).
def get_adj(i, j):
    adj = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
    res = []
    for (ai, aj) in adj:
        if 0 <= ai < n and 0 <= aj < m and grid[ai][aj] == '#':
            res.append((ai, aj))
        
    #State of the program after the  for loop has been executed: `res` is a list containing all tuples `(ai, aj)` from `adj` where `0 <= ai < n`, `0 <= aj < m`, and `grid[ai][aj] == '#'`; `adj` is a list of tuples representing the coordinates of adjacent cells in a grid.
    return res
    #The program returns the list of tuples `res` containing all coordinates `(ai, aj)` from `adj` where `0 <= ai < n`, `0 <= aj < m`, and `grid[ai][aj] == '#'`.
#Overall this is what the function does:The function accepts two integer parameters `i` and `j`, representing the coordinates of a cell in a grid. It returns a list of tuples containing the coordinates of all adjacent cells (up, down, left, and right) that are within the grid boundaries and contain a black cell ('#'). If none of the adjacent cells are black or if the coordinates are at the edges of the grid, the function will return an empty list.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 1000, and the grid is represented as a list of n strings, each of length m, consisting of characters '#' (black) and '.' (white).
def dfs(i, j):
    component, stack = 1, [(i, j)]
    while stack:
        si, sj = stack[-1]
        
        if visited[si][sj]:
            stack.pop()
            continue
        else:
            visited[si][sj] = True
            component = 1
            for ai, aj in get_adj(si, sj):
                if not visited[ai][aj]:
                    stack.append((ai, aj))
        
    #State of the program after the loop has been executed: `stack` is empty, `component` is 1, all positions in `visited` that were reachable from the initial position have been marked as True.
    return component
    #The program returns the value of component which is 1
#Overall this is what the function does:The function `dfs` accepts two integer parameters `i` and `j`, representing coordinates in a grid of characters ('#' for black and '.' for white). It performs a depth-first search to explore connected components from the starting position `(i, j)`. However, instead of returning the size of the connected component as might be expected, it always returns the value 1, indicating that at least one cell (the starting position) was visited, regardless of the actual size of the component. This implies that the function does not accurately reflect the number of cells connected to the starting cell.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 1000, and the grid is represented by a list of n strings, each of length m, containing only characters '#' (black) and '.' (white).
def func_2():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    if (grid == [('.' * m) for _ in range(n)]) :
        func_3(0)
        return
        #The program returns None, as there is no value specified in the return statement.
    #State of the program after the if block has been executed: *`n` and `m` are positive integers such that 1 ≤ `n`, `m` ≤ 1000; `grid` is a list of `n` strings from input. The `grid` is not equal to a list of `n` strings where each string consists of `m` dots ('.').
    for row in grid:
        start, stop = row.find('#'), row.rfind('#')
        
        if start == -1 or '.' in row[start:stop + 1]:
            func_3(-1)
            return
        
    #State of the program after the  for loop has been executed: `n` and `m` are positive integers such that 1 ≤ `n`, `m` ≤ 1000; `grid` is a list of `n` strings; for each `row`, `start` is the index of the first occurrence of '#', `stop` is the index of the last occurrence of '#' in `row`, and there are no '.' characters in the substring of `row` from index `start` to index `stop` for any row.
    grit = transpose(grid)
    for row in grit:
        start, stop = row.find('#'), row.rfind('#')
        
        if start == -1 or '.' in row[start:stop + 1]:
            func_3(-1)
            return
        
    #State of the program after the  for loop has been executed: `n` and `m` are positive integers such that 1 ≤ `n`, `m` ≤ 1000; `grit` is a list of strings that have been transposed from `grid`; for every `row` in `grit`, if `row` contains at least one occurrence of '#' and there are no '.' characters between the first and last occurrence of '#', the loop completes without returning. If any `row` does not meet these conditions, the function returns None immediately.
    func_3(func_1(n, m, grid))
#Overall this is what the function does:The function accepts no parameters and verifies the structure of a grid represented by a list of strings. It checks if the grid consists entirely of '.' characters, and if so, it calls `func_3(0)` and returns None. It then ensures that each row contains '#' characters without any '.' between the first and last occurrence of '#'. If any row fails this check, it calls `func_3(-1)` and returns None. After validating rows, it transposes the grid and performs the same checks on the transposed version. Finally, it calls `func_3` with the result of `func_1(n, m, grid)`. The function returns None in all cases, as there are no return values specified in the code.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 1000; the next n lines contain strings of length m, where each string consists of characters '#' (representing black cells) and '.' (representing white cells).
def func_3():
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 1000, `m` is an integer such that 1 ≤ `m` ≤ 1000, `sep` is ' ', `file` is `sys.stdout`, `at_start` is False, and all elements from `args` have been written to `file`, separated by `sep`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 1000, `m` is an integer such that 1 ≤ `m` ≤ 1000, `sep` is ' ', `file` is `sys.stdout`, `at_start` is False, and the end value from kwargs has been written to file, defaulting to '\n' if not provided. If `kwargs.pop('flush', False)` evaluates to True, then `file` has been flushed.
#Overall this is what the function does:The function accepts a variable number of arguments and keyword arguments. It writes these arguments to a specified output file, separated by a defined separator. If no separator is provided, it defaults to a space. After writing all the arguments, it adds an optional end character (defaulting to a newline) and can flush the output file if specified. The function does not process or validate the input strings, nor does it handle edge cases such as invalid types or empty input.

