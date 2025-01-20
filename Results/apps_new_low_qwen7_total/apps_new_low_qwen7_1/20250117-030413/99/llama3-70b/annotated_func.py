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
        #State of the program after the if-else block has been executed: *`a1`, `b1`, `a2`, `b2`, `a3`, `b3` are positive integers. If the maximum of `a1` and `b1` is greater than or equal to the maximum of `a3` and `b3`, and the minimum of `a1` and `b1` is greater than or equal to the minimum of `a3` and `b3`, the condition remains true. Otherwise, the condition becomes false.
    else :
        if (max(a1, b1) >= max(a3, b3) and min(a1, b1) >= min(a3, b3)) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *a1 is a positive integer, b1 is a positive integer, a2 is a positive integer, b2 is a positive integer, a3 is a positive integer, b3 is a positive integer. If max(a1, b1) >= max(a3, b3) and min(a1, b1) >= min(a3, b3), the current values of max(a1, b1) and min(a1, b1) remain unchanged. Otherwise, either max(a1, b1) < max(a3, b3) or min(a1, b1) < min(a3, b3).
    #State of the program after the if-else block has been executed: *`a1`, `b1`, `a2`, `b2`, `a3`, `b3` are positive integers. If the maximum of `a1` and `b1` is greater than or equal to the maximum of `a2` and `b2`, and the minimum of `a1` and `b1` is greater than or equal to the minimum of `a2` and `b2`, the condition remains true and the current values of `max(a1, b1)` and `min(a1, b1)` remain unchanged. Otherwise, either `max(a1, b1) < max(a2, b2)` or `min(a1, b1) < min(a2, b2)`.
#Overall this is what the function does:The function accepts four positive integers `a1`, `b1`, `a2`, and `b2` as input, representing the dimensions of a board and a painting respectively. It also implicitly takes `a3` and `b3` as additional input, which are the dimensions of another painting. The function checks if the first painting can fit within the board dimensions and whether it can fit within the second painting's dimensions based on the given conditions. If the first painting fits within both the board and the second painting, it prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value explicitly; it only prints 'YES' or 'NO' based on the conditions evaluated.

