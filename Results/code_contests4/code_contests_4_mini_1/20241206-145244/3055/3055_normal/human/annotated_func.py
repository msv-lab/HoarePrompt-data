#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 100, c is an uppercase Latin letter representing the President's desk colour, and the following n lines contain m characters each, where each character is either an uppercase Latin letter representing a desk colour or a period ('.') representing an empty cell.
def func():
    i1 = False or 0
    ii = False or 1
    iii = False or 2
    k = raw_input().split(' ')
    n, m, c = int(k[i1]), int(k[ii]), k[iii]
    mtrx = [[] for _ in range(n)]
    frnds = set([])
    k = int(False)
    while k < n:
        col = raw_input()
        
        j = 0
        
        while j < m:
            mtrx[k].extend(col[j])
            j = j + 1
        
        k = k + 1
        
    #State of the program after the loop has been executed: `k` is equal to `n`, `j` is equal to `m`, `m` is greater than or equal to 0, `mtrx` contains `n` lists, each extended with the corresponding input strings from `raw_input()` for the first `m` characters.
    for i in range(n):
        for j in range(m):
            if mtrx[i][j] == c and mtrx[i][j] != '.':
                if i - 1 > 0:
                    frnds.add(mtrx[i - 1][j])
                if j - 1 > 0:
                    frnds.add(mtrx[i][j - 1])
                if j + 1 < m:
                    frnds.add(mtrx[i][j + 1])
                if i + 1 < n:
                    frnds.add(mtrx[i + 1][j])
        
    #State of the program after the  for loop has been executed: `k` is equal to `n`, `j` is equal to `m`, `m` is greater than or equal to 0, `frnds` contains all unique elements from `mtrx` that are adjacent to positions where `mtrx[i][j]` is equal to `c` and not equal to '.', for all valid indices in the matrix.
    if ('.' in frnds) :
        frnds.remove('.')
    #State of the program after the if block has been executed: *`k` is equal to `n`, `j` is equal to `m`, `m` is greater than or equal to 0, `frnds` contains all unique elements from `mtrx` that are adjacent to positions where `mtrx[i][j]` is equal to `c` and not equal to '.'; if '.' is present in `frnds`, it is removed from `frnds`.
    print(len(frnds))
#Overall this is what the function does:The function accepts two integers `n` and `m`, and a character `c`, representing the dimensions of a grid and a desk color respectively. It processes the grid to find all unique desk colors adjacent to the cells containing `c`, excluding empty cells represented by '.'. The function then prints the count of these unique colors. However, it does not return any value, only prints the result.

