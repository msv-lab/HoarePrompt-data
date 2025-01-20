#State of the program right berfore the function call: a_1, b_1, a_2, b_2, a_3, b_3 are integers such that 1 <= a_1, b_1, a_2, b_2, a_3, b_3 <= 1000.
def func():
    a1, b1 = map(int, input().split())

a2, b2 = map(int, input().split())

a3, b3 = map(int, input().split())
    if (max(a1, b1) >= max(a2, b2) and min(a1, b1) >= min(a2, b2)) :
        if (max(a1, b1) >= max(a3, b3) and min(a1, b1) >= min(a3, b3)) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: a1, b1, a2, b2, a3, b3 are integers. If the maximum of a1 and b1 is greater than or equal to the maximum of a3 and b3, and the minimum of a1 and b1 is greater than or equal to the minimum of a3 and b3, no change is made to the variables. Otherwise, 'NO' is printed.
    else :
        if (max(a1, b1) >= max(a3, b3) and min(a1, b1) >= min(a3, b3)) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: `a1`, `b1`, `a2`, `b2`, `a3`, `b3` are integers. Either `max(a1, b1) < max(a2, b2)` or `min(a1, b1) < min(a2, b2)`. If `max(a1, b1) >= max(a3, b3)` and `min(a1, b1) >= min(a3, b3)`, then this condition holds. Otherwise, it is not the case that `max(a1, b1) >= max(a3, b3)` and `min(a1, b1) >= min(a3, b3)`, and still `max(a1, b1) < max(a2, b2)` or `min(a1, b1) < min(a2, b2)` holds.
    #State of the program after the if-else block has been executed: *`a1`, `b1`, `a2`, `b2`, `a3`, `b3` are integers. If the maximum of `a1` and `b1` is greater than or equal to the maximum of `a3` and `b3`, and the minimum of `a1` and `b1` is greater than or equal to the minimum of `a3` and `b3`, then no change is made to the variables. Otherwise, either `max(a1, b1) < max(a2, b2)` or `min(a1, b1) < min(a2, b2)` holds.
#Overall this is what the function does:The function reads three pairs of integers (a1, b1), (a2, b2), and (a3, b3) from the standard input, where each integer is between 1 and 1000. It then checks if the pair (a1, b1) can "dominate" the pair (a3, b3) under certain conditions. Specifically, it checks if both the maximum and minimum values of (a1, b1) are greater than or equal to the corresponding values of (a3, b3). If (a1, b1) cannot dominate (a3, b3), it further checks if (a1, b1) can dominate (a3, b3) by replacing (a3, b3) with (a2, b2). If neither condition holds, it prints 'NO'. If (a1, b1) can dominate (a3, b3) in either scenario, it prints 'YES'. The function does not accept any parameters and has no return value.

