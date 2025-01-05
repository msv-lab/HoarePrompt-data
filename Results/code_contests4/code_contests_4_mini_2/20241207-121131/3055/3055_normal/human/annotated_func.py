#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 100, c is an uppercase Latin letter representing the President's desk colour, and the office-room is represented as an n x m matrix with uppercase Latin letters and '.' characters.
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
        
    #State of the program after the loop has been executed: `k` is equal to `n`, `j` is equal to `m`, `mtrx` contains `n` lists each extended with elements from `col` up to the index `m-1` if `m` was greater than 0; if `m` was 0, `mtrx` will remain unchanged with all lists empty; `n`, `m`, `c`, `i1`, `ii`, and `iii` remain unchanged at 0, 0, 0, 0, 1, and 2 respectively.
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
        
    #State of the program after the  for loop has been executed: `k` is equal to `n`, `n` is greater than or equal to 0, `m` is greater than or equal to 0, `frnds` contains all unique elements from the neighbors of all `mtrx[i][j]` that equal `c` and are not '.', depending on the conditions met during the loop iterations.
    if ('.' in frnds) :
        frnds.remove('.')
    #State of the program after the if block has been executed: *`k` is equal to `n`, `n` is greater than or equal to 0, `m` is greater than or equal to 0, if `frnds` contains the element '.', it is removed from `frnds`. If `frnds` does not contain '.', its contents remain unchanged.
    print(len(frnds))
#Overall this is what the function does:The function accepts two integers `n` and `m`, and an uppercase Latin letter `c`. It processes an `n x m` matrix filled with uppercase Latin letters and '.' characters, counting unique neighboring elements of all occurrences of `c` in the matrix, excluding the '.' character. The function returns the count of these unique neighboring elements. If there are no occurrences of `c`, it returns 0. Additionally, if `m` is 0, the matrix will be empty, and the function will also return 0.

