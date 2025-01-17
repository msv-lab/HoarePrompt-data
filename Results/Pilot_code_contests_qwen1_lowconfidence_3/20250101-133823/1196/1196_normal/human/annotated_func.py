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
        #State of the program after the if block has been executed: *`r` is an integer between 1 and 500 (inclusive), `c` is an integer between 1 and 500 (inclusive); if `c` equals 1, then `flag` is True and `c` is now the previous value of `r`. Otherwise, the values of `r`, `c`, and `flag` remain unchanged.
        l = [[(1) for _ in range(c)] for _ in range(r)]
        b = [(i + 1) for i in range(r + c)]
        for i in range(r):
            for j in range(c):
                l[i][j] *= b[i] * b[r + j]
            
        #State of the program after the  for loop has been executed: `r` is a positive integer, `c` is a positive integer, `flag` is either `True` or `False` based on the initial value of `c`, `l` is a 2D list of dimensions `r x c` where each element `l[i][j]` is \((b[i] \times b[r + j])^{rc}\), `b` is a list containing integers from 1 to `r + c`.
        if (flag == False) :
            for i in range(r):
                s = ''
                
                for j in range(c):
                    s += str(l[i][j]) + ' '
                
                print(s)
                
            #State of the program after the  for loop has been executed: 
        else :
            for j in range(c):
                s = ''
                
                for i in range(r):
                    s += str(l[i][j]) + ' '
                
                print(s)
                
            #State of the program after the  for loop has been executed: `s` is the concatenation of the string representations of all elements `l[i][j]` for `i` in the range `0` to `r-1` and `j` in the range `0` to `c-1`, separated by spaces, `r` is a positive integer, `c` is a positive integer, `i` is `r - 1`, `j` is `c - 1`, and the loop prints `s` for each column.
        #State of the program after the if-else block has been executed: *`s` is the concatenation of the string representations of all elements `l[i][j]` for `i` in the range `0` to `r-1` and `j` in the range `0` to `c-1`, separated by spaces. If `flag` is `False`, then `s` is printed for each column. If `flag` is `True`, no specific action is taken for `s`.
    #State of the program after the if-else block has been executed: *`r` is an integer between 1 and 500 (inclusive), `c` is an integer between 1 and 500 (inclusive). If `r == 1` and `c == 1`, the printed value is 0. Otherwise, `s` is the concatenation of the string representations of all elements `l[i][j]` for `i` in the range `0` to `r-1` and `j` in the range `0` to `c-1`, separated by spaces. If `flag` is `False`, then `s` is printed for each column. If `flag` is `True`, no specific action is taken for `s`.
#Overall this is what the function does:The function reads two integers \( r \) and \( c \) from standard input, representing the number of rows and columns respectively. It then creates a 2D list \( l \) of size \( r \times c \) filled with ones. A list \( b \) is also created containing integers from 1 to \( r + c \). Based on whether \( c \) is 1, it either keeps the original dimensions and prints the matrix column-wise, or swaps \( r \) and \( c \) and prints the matrix row-wise. If \( r = 1 \) and \( c = 1 \), it prints 0. After these operations, the function prints the matrix in the specified format and exits.

