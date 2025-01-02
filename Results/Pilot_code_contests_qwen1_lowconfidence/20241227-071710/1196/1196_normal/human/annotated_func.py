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
        #State of the program after the if block has been executed: *`r` is an integer within the range 1 to 500, `c` is an integer within the range 1 to 500, and the condition (r != 1 and c != 1) remains true. If `c` equals 1 and `r` is 1, then `flag` is True. Otherwise, `flag` remains False.
        l = [[(1) for _ in range(c)] for _ in range(r)]
        b = [(i + 1) for i in range(r + c)]
        for i in range(r):
            for j in range(c):
                l[i][j] *= b[i] * b[r + j]
            
        #State of the program after the  for loop has been executed: `r` is an integer within the range 1 to 500, `c` is an integer within the range 1 to 500, the condition `(r != 1 and c != 1)` remains true, `flag` is False, `l` is a list of lists where each `l[i][j]` is the product of the initial value of `b[i]` and `b[r + j]` raised to the power of `j`, `b` is a list of length `r + c` containing elements from 1 to `r + c`.
        if (flag == False) :
            for i in range(r):
                s = ''
                
                for j in range(c):
                    s += str(l[i][j]) + ' '
                
                print(s)
                
            #State of the program after the  for loop has been executed: `s` is the concatenation of the string representations of all elements in the sublist `l[r-1]`, separated by spaces, `c` is the length of the sublist `l[r-1]`, and `j` is `c - 1`. The loop prints `s` for each row `i` from `0` to `r-1`.
        else :
            for j in range(c):
                s = ''
                
                for i in range(r):
                    s += str(l[i][j]) + ' '
                
                print(s)
                
            #State of the program after the  for loop has been executed: `i` is `r`, `s` is a string containing the concatenation of the string representations of `l[i][j]` for all `j` from `0` to `c-1`, `j` is `c`, `c` must be greater than 0, `r` is an integer within the range 1 to 500, `flag` is `True`, `l` is a list of lists where each `l[i][j]` is the product of the initial value of `b[i]` and `b[r + j]` raised to the power of `j`, `b` is a list of length `r + c` containing elements from 1 to `r + c`.
        #State of the program after the if-else block has been executed: *`r` is an integer within the range 1 to 500, `c` is an integer within the range 1 to 500, `flag` is `True`, `l` is a list of lists where each `l[i][j]` is the product of the initial value of `b[i]` and `b[r + j]` raised to the power of `j`, `b` is a list of length `r + c` containing elements from 1 to `r + c`. If `flag` is `False`, then `s` is the concatenation of the string representations of all elements in the sublist `l[r-1]`, separated by spaces, `c` is the length of the sublist `l[r-1]`, and `j` is `c - 1`. The loop prints `s` for each row `i` from `0` to `r-1`. If `flag` is `True`, then `i` is `r`, `s` is a string containing the concatenation of the string representations of `l[i][j]` for all `j` from `0` to `c-1`, `j` is `c`, and `c` must be greater than 0.
    #State of the program after the if-else block has been executed: `r` is an integer within the range 1 to 500, `c` is an integer within the range 1 to 500. If `r == 1` and `c == 1`, then `flag` is `True`, `l` is a list of lists where each `l[i][j]` is the product of the initial value of `b[i]` and `b[r + j]` raised to the power of `j`, `b` is a list of length `r + c` containing elements from 1 to `r + c`. If `r != 1` or `c != 1`, then `flag` is `True`, `s` is the concatenation of the string representations of all elements in the sublist `l[r-1]`, separated by spaces, `c` is the length of the sublist `l[r-1]`, and `j` is `c - 1`. The loop prints `s` for each row `i` from `0` to `r-1`. If `flag` is `False`, then `i` is `r`, `s` is a string containing the concatenation of the string representations of `l[i][j]` for all `j` from `0` to `c-1`, `j` is `c`, and `c` must be greater than 0.
#Overall this is what the function does:The function reads two integers \( r \) and \( c \) from the standard input, where both \( r \) and \( c \) are within the range 1 to 500. It then constructs a matrix \( l \) of size \( r \times c \) where each element \( l[i][j] \) is calculated as the product of the initial value of \( b[i] \) and \( b[r + j] \) raised to the power of \( j \). Here, \( b \) is a list containing the first \( r + c \) natural numbers. Based on the values of \( r \) and \( c \), the function determines whether to transpose the matrix \( l \) before printing its contents. Specifically, if \( r \neq 1 \) and \( c \neq 1 \), the function prints the matrix \( l \) as is. If \( c = 1 \) and \( r \neq 1 \), the function transposes the matrix and prints it. If \( r = 1 \) and \( c = 1 \), the function prints 0 directly without constructing the matrix.

