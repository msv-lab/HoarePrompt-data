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
        #State of the program after the if block has been executed: *`r` and `c` are integers within the range 1 to 500, and `r` is not equal to 1 or `c` is not equal to 1. If `c` equals 1, then `r` becomes the original value of `c`, `c` becomes the original value of `r`, and `flag` is True. Otherwise, the values of `r`, `c`, and `flag` remain unchanged.
        l = [[(1) for _ in range(c)] for _ in range(r)]
        b = [(i + 1) for i in range(r + c)]
        for i in range(r):
            for j in range(c):
                l[i][j] *= b[i] * b[r + j]
            
        #State of the program after the  for loop has been executed: `r` is the original value of `c`, `c` is the original value of `r`, `flag` is still `True`, `l` is a 2D list with `r` rows and `c` columns where each element is the product of `b[i] * b[r + j]` for all `0 <= j < c` and `0 <= i < r`, `b` is a list containing integers from 1 to `r + c`.
        if (flag == False) :
            for i in range(r):
                s = ''
                
                for j in range(c):
                    s += str(l[i][j]) + ' '
                
                print(s)
                
            #State of the program after the  for loop has been executed: `r` is the original value of `c`, `c` is the original value of `r`, `l` is the 2D list with `r` rows and `c` columns where each element is the product of `b[i] * b[r + j]` for all `0 <= j < c` and `0 <= i < r`, `b` is the list containing integers from 1 to `r + c`, `flag` is still `False`. The output is the formatted printing of all elements in `l` row by row.
        else :
            for j in range(c):
                s = ''
                
                for i in range(r):
                    s += str(l[i][j]) + ' '
                
                print(s)
                
            #State of the program after the  for loop has been executed: `r` is the original value and must be greater than 0, `c` is the original value and must be greater than 0, `flag` is still `True`, `l` is a 2D list with `r` rows and `c` columns, `b` is a list containing integers from 1 to `r + c`, `j` is `c-1`, `s` is the concatenation of all elements in the 2D list `l` across all columns, separated by spaces.
        #State of the program after the if-else block has been executed: `r` is the original value of `c`, `c` is the original value of `r`, and `flag` is still `False`. If `flag` is `False`, the output is the formatted printing of all elements in `l` row by row. Otherwise, `l` is a 2D list with `r` rows and `c` columns where each element is the product of `b[i] * b[r + j]` for all `0 <= j < c` and `0 <= i < r`, `b` is a list containing integers from 1 to `r + c`, `j` is `c-1`, and `s` is the concatenation of all elements in the 2D list `l` across all columns, separated by spaces.
    #State of the program after the if-else block has been executed: *`r` and `c` are integers within the range 1 to 500. If `r` is 1 and `c` is 1, then `r` remains 1 and `c` remains 1. Otherwise, `r` is the original value of `c`, `c` is the original value of `r`, and `flag` is still `False`. If `flag` is `False`, the output is the formatted printing of all elements in `l` row by row. If `flag` is `True`, `l` is a 2D list with `r` rows and `c` columns where each element is the product of `b[i] * b[r + j]` for all `0 <= j < c` and `0 <= i < r`, `b` is a list containing integers from 1 to `r + c`, `j` is `c-1`, and `s` is the concatenation of all elements in the 2D list `l` across all columns, separated by spaces.
#Overall this is what the function does:The function takes two integers `r` and `c` as input, representing the dimensions of a 2D array. It first checks if both `r` and `c` are 1. If so, it prints `0` and ends. Otherwise, it swaps `r` and `c` if `c` is 1. Then, it creates a 2D list `l` with `r` rows and `c` columns, where each element is the product of corresponding elements from two lists: `b` (containing integers from 1 to `r + c`), and `b` shifted by `r`. Finally, it prints the 2D list either row-wise or column-wise depending on the initial value of `c` (whether it was swapped). If `c` was not swapped, it prints the list row-wise; otherwise, it prints the list column-wise. The function does not return anything.

