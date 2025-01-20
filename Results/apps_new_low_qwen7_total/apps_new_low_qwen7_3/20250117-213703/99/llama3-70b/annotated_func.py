#State of the program right berfore the function call: a_1 and b_1 are positive integers representing the dimensions of the board, and a_2, b_2, a_3, b_3 are positive integers representing the dimensions of the two paintings, all fitting into the range from 1 to 1000.
def func():
    a1, b1 = map(int, input().split())

a2, b2 = map(int, input().split())

a3, b3 = map(int, input().split())
    if (max(a1, b1) >= max(a2, b2) and min(a1, b1) >= min(a2, b2)) :
        if (max(a1, b1) >= max(a3, b3) and min(a1, b1) >= min(a3, b3)) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a1` is a positive integer, `b1` is a positive integer, `a2` is a positive integer, `b2` is a positive integer, `a3` is a positive integer, `b3` is a positive integer. If the maximum of `a1` and `b1` is greater than or equal to the maximum of `a3` and `b3`, and the minimum of `a1` and `b1` is greater than or equal to the minimum of `a3` and `b3`, then the output is `YES`. Otherwise, the program does not perform any specific action, but maintains the initial conditions of the variables.
    else :
        if (max(a1, b1) >= max(a3, b3) and min(a1, b1) >= min(a3, b3)) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: `a1`, `b1`, `a2`, `b2`, `a3`, `b3` are positive integers. If the maximum of `a1` and `b1` is greater than or equal to the maximum of `a3` and `b3`, and the minimum of `a1` and `b1` is greater than or equal to the minimum of `a3` and `b3`, then no specific changes are made. Otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`a1`, `b1`, `a2`, `b2`, `a3`, `b3` are positive integers. If the maximum of `a1` and `b1` is greater than or equal to the maximum of `a3` and `b3`, and the minimum of `a1` and `b1` is greater than or equal to the minimum of `a3` and `b3`, then the output is `YES`. Otherwise, the output is `NO`.
#Overall this is what the function does:The function accepts four parameters \(a_1\), \(b_1\), \(a_2\), and \(b_2\) which represent the dimensions of a board and two paintings, respectively. It checks if the board can accommodate both paintings based on their dimensions. Specifically, the function determines if the board's dimensions can satisfy the dimensions of either of the two paintings. If the board can fit both paintings according to the specified conditions, the function prints 'YES'; otherwise, it prints 'NO'. The function does not modify the input variables and only outputs a string based on the comparison results. The function handles the following edge cases:
1. If the dimensions of the board and paintings are within the range of 1 to 1000.
2. If the board dimensions are larger than or equal to the maximum and minimum dimensions of both paintings.
If neither condition is met, the function prints 'NO'.

