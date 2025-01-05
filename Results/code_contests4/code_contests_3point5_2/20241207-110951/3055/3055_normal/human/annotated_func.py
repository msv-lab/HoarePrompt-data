#State of the program right berfore the function call: n and m are positive integers representing the dimensions of the office-room matrix, c is a single uppercase Latin letter representing the President's desk colour. The office-room description is a matrix of n rows and m columns with unique uppercase Latin letters representing desk colours and periods representing empty cells.**
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
        
    #State of the program after the loop has been executed: `n` and `m` are positive integers representing the dimensions of the office-room matrix, `c` is a single uppercase Latin letter representing the President's desk colour, `mtrx` is a matrix with `n` rows each extended by the raw input value, `frnds` is an empty set, `m` is greater than 0, `col` is assigned the raw input value, `j` is equal to the final value of `m`, `k` is equal to the final value of `n` where `k` is incremented by 1
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
        
    #State of the program after the  for loop has been executed: `n`, `m`, `c`, `mtrx`, `frnds`, `i`, `j`, `k` are integers with updated values based on the conditions met in the loop. The set `frnds` contains all the elements in `mtrx` that are adjacent to an element equal to `c` and not equal to '.'. `j` is equal to `m` and `k` is equal to `n+1`
    if ('.' in frnds) :
        frnds.remove('.')
    #State of the program after the if block has been executed: *`n`, `m`, `c`, `mtrx`, `frnds`, `i`, `j`, `k` are integers with updated values based on the conditions met in the loop. The set `frnds` contains all the elements in `mtrx` that are adjacent to an element equal to `c` and not equal to '.'. `j` is equal to `m` and `k` is equal to `n+1`. There is at least one element '.' in the set `frnds` except for '.' that has been removed.
    print(len(frnds))
#Overall this is what the function does:The function func reads input to describe an office-room matrix, identifies adjacent elements to the President's desk color, and prints the count of those adjacent elements. If a '.' is found in the adjacent elements, it is removed before counting. The function does not accept any parameters and provides information about the office-room matrix based on the constraints provided.

