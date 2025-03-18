#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and (x_a, y_a) ≠ (x_b, y_b). Additionally, the sum of h over all test cases does not exceed 10^6.
def func_1():
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns None
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4, r is a list containing six integers obtained from splitting the input string using space as delimiter, n is the first element of r, m is the second element of r, x1 is the third element of r, y1 is the fourth element of r, x2 is the fifth element of r, y2 is the sixth element of r, and x2 is greater than x1
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns None
        #State: t is a positive integer such that 1 ≤ t ≤ 10^4, r is a list containing six integers obtained from splitting the input string using space as delimiter, n is the first element of r, m is the second element of r, x1 is the third element of r, y1 is the fourth element of r, x2 is the fifth element of r, y2 is the sixth element of r, x2 is greater than x1, and y1 is not equal to y2
        if (y2 > y1) :
            y1 += 1
            x1 += 1
        else :
            y1 -= 1
            x1 += 1
        #State: t is a positive integer such that 1 ≤ t ≤ 10^4, r is a list containing six integers obtained from splitting the input string using space as delimiter, n is the first element of r, m is the second element of r, x1 is incremented by 1, and y1 is adjusted based on the relationship with y2 (if y2 > y1, y1 becomes one more than the original value; otherwise, y1 becomes one less than the original value). x2 is the fifth element of r, and y2 is the sixth element of r, with x2 being greater than x1.
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns None
        #State: t is a positive integer such that 1 ≤ t ≤ 10^4, r is a list containing six integers obtained from splitting the input string using space as delimiter, n is the first element of r, m is the second element of r, x1 is incremented by 1, and y1 is adjusted based on the relationship with y2 (if y2 > y1, y1 becomes one more than the original value; otherwise, y1 becomes one less than the original value). x2 is the fifth element of r, and y2 is the sixth element of r, with x2 being greater than x1, and y1 is not equal to y2
        if (y1 >= y2) :
            a = y2 - 1
        else :
            a = m - y2
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `r` is a list containing six integers obtained from splitting the input string using space as delimiter, `n` is the first element of `r`, `m` is the second element of `r`, `x1` is incremented by 1, `y1` is adjusted based on the relationship with `y2` (if `y2` > `y1`, `y1` becomes one more than the original value; otherwise, `y1` becomes one less than the original value), `x2` is the fifth element of `r`, `y2` is the sixth element of `r`, `x2` is greater than `x1`, `y1` is not equal to `y2`, and `a` is either `y2 - 1` if `y1` ≥ `y2` or `m - y2` if `y1` < `y2`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value since there is no return statement provided in the given code snippet.
        #State: `t` is the absolute difference between `y2` and `y1`, `r` is a list containing six integers obtained from splitting the input string using space as delimiter, `n` is the first element of `r`, `m` is the second element of `r`, `x1` is incremented by `a`, `y1` is adjusted based on the relationship with `y2`, `x2` is the fifth element of `r` reduced by `a`, `y2` is the sixth element of `r`, `x1` is less than or equal to `x2`, `y1` is not equal to `y2`, and `a` is either `y2 - 1` if `y1` ≥ `y2` or `m - y2` if `y1` < `y2`, `b` is the difference between `x2` and `x1`.
        if (y2 <= y1) :
            y2 = 1
            y1 -= a
            c = y1 - 1
        else :
            y2 = m
            y1 += a
            c = m - y1
        #State: `t` is the absolute difference between `y2` and `y1`, `r` is a list containing six integers obtained from splitting the input string using space as delimiter, `n` is the first element of `r`, `m` is the second element of `r`, `x1` is incremented by `a`, `y1` is adjusted based on the condition (if `y2 <= y1`, then `y1` is set to `0`; otherwise, `y1` is adjusted by adding `a` to its previous value), `x2` is the fifth element of `r` reduced by `a`, `y2` is the sixth element of `r`, `x1` is less than or equal to `x2`, `y1` is not equal to `y2`, `c` is `-1` if `y2 <= y1` and `m - y1` otherwise, `b` is the difference between `x2` and `x1`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns None
        else :
            print('draw')
            #This is printed: draw
            return
            #The program returns None
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns None
        #State: t is a positive integer such that 1 ≤ t ≤ 10^4, r is a list containing six integers obtained from splitting the input string using space as delimiter, n is the first element of r, m is the second element of r, x1 is the third element of r, y1 is the fourth element of r, x2 is the fifth element of r, y2 is the sixth element of r, and y1 is not equal to y2
        if (y2 >= y1) :
            a = y1 - 1
        else :
            a = m - y1
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `r` is a list containing six integers obtained from splitting the input string using space as delimiter, `n` is the first element of `r`, `m` is the second element of `r`, `x1` is the third element of `r`, `y1` is the fourth element of `r`, `x2` is the fifth element of `r`, `y2` is the sixth element of `r`, and `y1` is not equal to `y2`. If `y2` is greater than or equal to `y1`, then `a` is `y1 - 1`. Otherwise, `a` is `m - y1`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program returns None
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `r` is a list containing six integers obtained from splitting the input string using space as delimiter, `n` is the first element of `r`, `m` is the second element of `r`, `x1` is the third element of `r` increased by `a`, `y1` is the fourth element of `r`, `x2` is the fifth element of `r` decreased by `a`, `y2` is the sixth element of `r`, and `y1` is not equal to `y2`; `b` is `x2 - x1`, `t` is `abs(y2 - y1)`, `x2 > x1`, `x1 ≥ 1`, and `x2 ≤ n`
        if (y1 <= y2) :
            y1 = 1
            y2 -= a
            c = y2 - 1
        else :
            y1 = m
            y2 += a
            c = m - y2
        #State: Postcondition: `t` is the absolute difference between `y2` and `y1`, `r` is a list containing six integers obtained from splitting the input string using space as delimiter, `n` is the first element of `r`, `m` is the second element of `r`, `x1` is the third element of `r` increased by `a`, `y1` is either 1 or the second element of `r`, `x2` is the fifth element of `r` decreased by `a`, `y2` is the sixth element of `r` decreased by `a` or the sixth element of `r` plus `a`, `b` is `x2 - x1`, `x2 > x1`, `x1 ≥ 1`, `x2 ≤ n`, and `y1` is less than or equal to `y2`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('bob')
            #This is printed: bob
            return
            #The program returns None
        else :
            print('draw')
            #This is printed: draw
            return
            #The program returns None
#Overall this is what the function does:The function reads six integers from the standard input, representing the dimensions of a grid and two coordinates. It then determines which player, Alice or Bob, wins based on the relative positions of the coordinates and prints the result. If the initial conditions do not lead to a clear winner, it prints 'draw'. The function does not return any value.

