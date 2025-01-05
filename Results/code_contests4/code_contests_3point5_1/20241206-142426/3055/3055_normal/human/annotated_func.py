#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 100. c is an uppercase Latin letter. The office-room description is a matrix of size n x m with each cell containing either an uppercase Latin letter representing a desk colour or a period character '.' representing an empty cell. Each desk colour is unique and represents a continuous subrectangle in the matrix.**
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
        
    #State of the program after the loop has been executed: `n` is a positive integer, `m` is a positive integer greater than 0, `c` is an uppercase Latin letter, `mtrx` is a 2D list with n lists, each containing m elements from user input, `frnds` is an empty set, `k` is equal to `n`, `col` is a string obtained from the user input, `j` is equal to `m`, all elements of `col` have been added to the respective lists in `mtrx`
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
        
    #State of the program after the  for loop has been executed: Output State: `n`, `m`, `c`, `mtrx`, `frnds`, `k`, `col`, `j` are integers. After all iterations of the loop, `frnds` will contain unique elements from the adjacent positions of elements in `mtrx` that are equal to `c` and not equal to '.'. The elements added to `frnds` will be based on the positions of `i` and `j` within the matrix, following the conditions provided in the if statements. If the loop does not execute, `frnds` will remain an empty set.
    if ('.' in frnds) :
        frnds.remove('.')
    #State of the program after the if block has been executed: *`n`, `m`, `c`, `mtrx`, `frnds`, `k`, `col`, `j` are integers. After all iterations of the loop, `frnds` will contain unique elements from the adjacent positions of elements in `mtrx` that are equal to `c` and not equal to '.', based on the positions of `i` and `j` within the matrix. If the loop does not execute, `frnds` will remain an empty set. Additionally, after removing '.', the set `frnds` will not contain '.'.
    print(len(frnds))
#Overall this is what the function does:The function `func` processes an office-room description matrix and identifies unique desk neighbours based on a given desk colour. It accepts no parameters. The matrix consists of uppercase Latin letters representing desk colours or '.' for an empty cell. It iterates over the matrix, identifies adjacent desk colours to the given colour `c`, and stores them in a set `frnds`. The function then removes any '.' from `frnds` and prints the count of unique desk neighbours.

