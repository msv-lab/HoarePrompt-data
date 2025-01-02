#State of the program right berfore the function call: r and c are integers such that 1 ≤ r, c ≤ 500.
def func():
    r, c = map(int, raw_input().split())
    if (r == 1 and c == 1) :
        print(0)
    else :
        flag = False
        if (c == 1) :
            flag = True
            r, c = c, r
        #State of the program after the if block has been executed: *`r` and `c` are integers such that 1 ≤ r, c ≤ 500, and either `r` is not equal to 1 or `c` is not equal to 1. If `c` == 1, `flag` is `True`. Otherwise, `flag` remains `False`.
        l = [[(1) for _ in range(c)] for _ in range(r)]
        b = [(i + 1) for i in range(r + c)]
        for i in range(r):
            for j in range(c):
                l[i][j] *= b[i] * b[r + j]
            
        #State of the program after the  for loop has been executed: `r` and `c` are integers such that 1 ≤ r, c ≤ 500, and either `r` is not equal to 1 or `c` is not equal to 1. If `c` == 1, `flag` is `True`. Otherwise, `flag` remains `False`. `l` is a 2D list of size `r` x `c` where each element `l[i][j]` is `b[i] * b[r + j]` for all `i` in the range 0 to `r-1` and `j` in the range 0 to `c-1`. `b` is a list of length `r + c` containing elements from 1 to `r + c`.
        if (flag == False) :
            for i in range(r):
                s = ''
                
                for j in range(c):
                    s += str(l[i][j]) + ' '
                
                print(s)
                
            #State of the program after the  for loop has been executed: `r` is an integer such that 1 ≤ r ≤ 500, `c` is an integer such that 1 ≤ c ≤ 500, either `r` is not equal to 1 or `c` is not equal to 1, if `c` == 1 then `flag` is `True` otherwise `flag` is `False`, `l` is a 2D list of size `r` x `c` where each element `l[i][j]` is `b[i] * b[r + j]` for all `i` in the range 0 to `r-1` and `j` in the range 0 to `c-1`, `b` is a list of length `r + c` containing elements from 1 to `r + c`, `i` is `r - 1`, `s` is a string containing the space-separated values of `l[r-1][j]` for `j` in the range 0 to `c-1`, `j` is `c - 1`, and the loop has printed `r` lines, each line containing `c` space-separated values corresponding to the elements of `l[i][j]` for the respective `i` in the range 0 to `r-1`.
        else :
            for j in range(c):
                s = ''
                
                for i in range(r):
                    s += str(l[i][j]) + ' '
                
                print(s)
                
            #State of the program after the  for loop has been executed: `r` is an integer such that 1 ≤ r ≤ 500, `c` is an integer such that 1 ≤ c ≤ 500, either `r` is not equal to 1 or `c` is not equal to 1, `flag` is `True`, `l` is a 2D list of size `r` x `c` where each element `l[i][j]` is `b[i] * b[r + j]`, `b` is a list of length `r + c` containing elements from 1 to `r + c`, and `c` lines have been printed, each containing the concatenated string representations of `l[i][j]` for all `i` from 0 to `r-1`, separated by spaces, for each `j` from 0 to `c-1`.
        #State of the program after the if-else block has been executed: *`r` and `c` are integers such that 1 ≤ r, c ≤ 500, and either `r` is not equal to 1 or `c` is not equal to 1. If `c` == 1, `flag` is `True`; otherwise, `flag` remains `False`. `l` is a 2D list of size `r` x `c` where each element `l[i][j]` is `b[i] * b[r + j]` for all `i` in the range 0 to `r-1` and `j` in the range 0 to `c-1`. `b` is a list of length `r + c` containing elements from 1 to `r + c`. If `flag` is `False`, `i` is `r - 1`, `s` is a string containing the space-separated values of `l[r-1][j]` for `j` in the range 0 to `c-1`, `j` is `c - 1`, and the loop has printed `r` lines, each line containing `c` space-separated values corresponding to the elements of `l[i][j]` for the respective `i` in the range 0 to `r-1`. If `flag` is `True`, `c` lines have been printed, each containing the concatenated string representations of `l[i][j]` for all `i` from 0 to `r-1`, separated by spaces, for each `j` from 0 to `c-1`.
    #State of the program after the if-else block has been executed: *`r` and `c` are integers such that 1 ≤ r, c ≤ 500, updated to the values provided by the user. If `r` == 1 and `c` == 1, the current values of `r` and `c` are both 1. Otherwise, either `r` is not equal to 1 or `c` is not equal to 1. If `c` == 1, `flag` is `True`; otherwise, `flag` remains `False`. A 2D list `l` of size `r` x `c` is created where each element `l[i][j]` is `b[i] * b[r + j]` for all `i` in the range 0 to `r-1` and `j` in the range 0 to `c-1`. `b` is a list of length `r + c` containing elements from 1 to `r + c`. If `flag` is `False`, `i` is `r - 1`, `s` is a string containing the space-separated values of `l[r-1][j]` for `j` in the range 0 to `c-1`, `j` is `c - 1`, and the loop has printed `r` lines, each line containing `c` space-separated values corresponding to the elements of `l[i][j]` for the respective `i` in the range 0 to `r-1`. If `flag` is `True`, `c` lines have been printed, each containing the concatenated string representations of `l[i][j]` for all `i` from 0 to `r-1`, separated by spaces, for each `j` from 0 to `c-1`.
#Overall this is what the function does:The function `func` reads two integers `r` and `c` from the user input, where both `r` and `c` are between 1 and 500 inclusive. If both `r` and `c` are 1, the function prints `0` and exits. Otherwise, it creates a 2D list `l` of size `r` x `c` and a 1D list `b` of length `r + c` containing elements from 1 to `r + c`. Each element `l[i][j]` in the 2D list is set to the product of `b[i]` and `b[r + j]`. If `c` is 1, the function transposes the matrix by swapping `r` and `c` and sets a flag to `True`. Finally, it prints the elements of the 2D list `l` in a specific format: if the flag is `False`, it prints `r` lines, each containing `c` space-separated values; if the flag is `True`, it prints `c` lines, each containing `r` space-separated values. The function does not return any value.

