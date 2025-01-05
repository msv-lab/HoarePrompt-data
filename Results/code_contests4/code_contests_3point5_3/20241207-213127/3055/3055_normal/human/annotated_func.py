#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 100. President's desk colour c is an uppercase Latin letter. The office-room description is a matrix of size n x m where each cell contains either an uppercase Latin letter representing a desk colour or a period character '.' representing an empty cell.**
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
        
    #State of the program after the loop has been executed: Output State: After the loop executes `n` times, `n` and `m` are positive integers such that 1 <= n, m <= 100, President's desk colour `c` is an uppercase Latin letter, `ii` is either `False` or 1, `iii` is False or 2, `k` is equal to `n`, `mtrx` is a 2D list with `n` lists where each list contains all elements of the corresponding input strings, `frnds` is an empty set, `col` is assigned the last input string, `j` is equal to `m` for the last iteration.
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `frnds` will contain all unique elements from the positions surrounding the cells in `mtrx` where the value equals `c` and is not equal to '.'. All other variables (`n`, `m`, `c`, `ii`, `iii`, `k`, `mtrx`, `col`, `j`) will remain unchanged as described.
    if ('.' in frnds) :
        frnds.remove('.')
    #State of the program after the if block has been executed: *After all iterations of the loop, `frnds` will contain all unique elements from the positions surrounding the cells in `mtrx` where the value equals `c` and is not equal to '.', if '.' is in `frnds`, then it indicates that at least one of the surrounding cells in `mtrx` contains a value equal to `c` and not equal to '.'. All other variables (`n`, `m`, `c`, `ii`, `iii`, `k`, `mtrx`, `col`, `j`) will remain unchanged as described.
    print(len(frnds))
#Overall this is what the function does:The function `func` reads input to create an office-room description matrix and President's desk color based on the given constraints. It then analyzes the matrix to find unique desk colors surrounding the President's desk color. The function outputs the count of unique desk colors found. If the matrix contains empty cells represented by '.', it removes them from the analysis.

