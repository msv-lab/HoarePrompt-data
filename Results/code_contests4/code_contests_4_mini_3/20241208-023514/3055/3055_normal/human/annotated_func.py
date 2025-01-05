#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 100, c is an uppercase Latin letter representing the President's desk colour, and the following n lines each contain m characters consisting of uppercase Latin letters or the period character ('.') indicating the office-room layout.
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
        
    #State of the program after the loop has been executed: `k` is equal to `n`, `j` is equal to `m`, `mtrx` remains a list containing 0 empty lists if `n` was 0, or has been extended by elements from `col` if `n` was greater than 0. `col` is the last input string received, `n` is 0, and `frnds` remains an empty set.
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
        
    #State of the program after the  for loop has been executed: `k` is equal to `n`, `j` is equal to `m`, `m` is greater than or equal to 0, `mtrx` remains a list containing 0 empty lists if `n` was 0, or has been extended by elements from `col` if `n` was greater than 0, and `frnds` remains an empty set.
    if ('.' in frnds) :
        frnds.remove('.')
    #State of the program after the if block has been executed: *`k` is equal to `n`, `j` is equal to `m`, and `m` is greater than or equal to 0. If '.' is present in `frnds`, then '.' is removed from `frnds`, while `mtrx` remains a list containing 0 empty lists if `n` was 0 or has been extended by elements from `col` if `n` was greater than 0. If '.' is not in `frnds`, then `frnds` remains an empty set.
    print(len(frnds))
#Overall this is what the function does:The function processes an office-room layout defined by dimensions `n` and `m`, and a specified color `c`. It collects unique characters adjacent to occurrences of `c` in the layout, excluding the period character ('.'). Finally, it prints the count of these unique characters. The function does not take parameters directly; instead, it relies on user input for its operation. If the layout is empty or if no valid adjacent characters are found, it will return 0. Additionally, it does not handle cases where `n` or `m` are 0 effectively, as the logic assumes positive values for both.

