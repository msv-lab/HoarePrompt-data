#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that x_a ≠ x_b or y_a ≠ y_b, and the sum of h over all test cases does not exceed 10^6.
def func_1():
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program does not return anything as there is no expression or variable specified in the return statement.
    #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4; `r` is a list containing six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9; `n` is equal to `r[0]`; `m` is equal to `r[1]`; `x1` is equal to `r[2]`; `y1` is equal to `r[3]`; `x2` is equal to `r[4]`; `y2` is equal to `r[5]`. Additionally, `x2` is greater than `x1`.
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing.
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4; `r` is a list containing six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9; `n` is equal to `r[0]`; `m` is equal to `r[1]`; `x1` is equal to `r[2]`; `y1` is equal to `r[3]`; `x2` is equal to `r[4]`; `y2` is equal to `r[5]`. Additionally, `x2` is greater than `x1` and `(x2 - x1)` is odd. `y1` is not equal to `y2`.
        if (y2 > y1) :
            y1 += 1
            x1 += 1
        else :
            y1 -= 1
            x1 += 1
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4; `r` is a list containing six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9; `n` is equal to `r[0]`; `m` is equal to `r[1]`; `x1` is equal to `r[2] + 1`; `x2` is equal to `r[4]`; `(x2 - x1)` is odd and `x2` is greater than `x1`; `y1` is not equal to `y2`. If `y2` is greater than `y1`, then `y1` is incremented by 1. Otherwise, `y1` is decremented by 1.
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program does not return any value.
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4; `r` is a list containing six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9; `n` is equal to `r[0]`; `m` is equal to `r[1]`; `x1` is equal to `r[2] + 1`; `x2` is equal to `r[4]`; `(x2 - x1)` is odd and `x2` is greater than `x1`; `y1` is not equal to `y2`. If `y2` is greater than `y1`, then `y1` is incremented by 1. Otherwise, `y1` is decremented by 1; `y1` is not equal to `y2`
        if (y1 >= y2) :
            a = y2 - 1
        else :
            a = m - y2
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4; `r` is a list containing six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9; `n` is equal to `r[0]`; `m` is equal to `r[1]`; `x1` is equal to `r[2] + 1`; `x2` is equal to `r[4]`; `(x2 - x1)` is odd and `x2` is greater than `x1`; `y1` is not equal to `y2`. If `y2` is greater than `y1`, then `y1` is incremented by 1. Otherwise, `y1` is decremented by 1; `y1` is compared to `y2`. If `y1` is greater than or equal to `y2`, `a` is equal to `y2 - 1`. Otherwise, `a` is equal to `m - y2`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program returns nothing (None)
        #State: `t` is `abs(y2 - y1)`, `r` is a list containing six integers `[h, w, x_a, y_a, x_b, y_b]`, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is `(x_a + 1) + a`, `x2` is `r[4] - a`, `y1` is incremented or decremented based on the comparison with `y2`, `a` is `y2 - 1` if `y1 >= y2` else `m - y2`, `b` is `x2 - x1`. Additionally, `x2` is greater than `x1`, `x1` is at least 1, and `x2` is less than or equal to `n`.
        if (y2 <= y1) :
            y2 = 1
            y1 -= a
            c = y1 - 1
        else :
            y2 = m
            y1 += a
            c = m - y1
        #State: `t` is either `abs(y2 - y1)` or `abs(m - y1)`, `r` is a list containing six integers `[h, w, x_a, y_a, x_b, y_b]`, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is `(x_a + 1) + a`, `x2` is `r[4] - a`, `y1` remains unchanged, `a` is `0`, `b` is `x2 - x1`, `x2` is greater than `x1`, `x1` is at least 1, `x2` is less than or equal to `n`, `y2` is either `1` or `m`, and `c` is either `y1 - 1` or `1` or `-1` depending on the condition `y2 <= y1`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('Alice')
            #This is printed: Alice
            return
            #The program does not return any value.
        else :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value.
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing (None)
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4; `r` is a list containing six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9; `n` is equal to `r[0]`; `m` is equal to `r[1]`; `x1` is equal to `r[2]`; `y1` is equal to `r[3]`; `x2` is equal to `r[4]`; `y2` is equal to `r[5]`. Additionally, `x2` is greater than `x1` and `(x2 - x1)` is even. `y1` is not equal to `y2`.
        if (y2 >= y1) :
            a = y1 - 1
        else :
            a = m - y1
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4; `r` is a list containing six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9; `n` is equal to `r[0]`; `m` is equal to `r[1]`; `x1` is equal to `r[2]`; `y1` is equal to `r[3]`; `x2` is equal to `r[4]`; `y2` is equal to `r[5]`. Additionally, `x2` is greater than `x1` and `(x2 - x1)` is even. `y1` is not equal to `y2`. If `y2` is greater than or equal to `y1`, `a` is equal to `y1 - 1`. Otherwise, `a` is equal to `m - y1`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program returns None
        #State: `t` is `abs(y2 - y1)`, `r` is a list containing six integers `[h, w, x_a, y_a, x_b, y_b]`, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + a`, `y1` is equal to `r[3]`, `x2` is equal to `r[4] - a`, `y2` is equal to `r[5]`, `a` is equal to `y1 - 1` if `y2` is greater than or equal to `y1`, otherwise `a` is equal to `m - y1`, `b` is equal to `x2 - x1`. Additionally, `x2` is greater than `x1`, `x1` is at least 1, and `x2` is less than or equal to `n`.
        if (y1 <= y2) :
            y1 = 1
            y2 -= a
            c = y2 - 1
        else :
            y1 = m
            y2 += a
            c = m - y2
        #State: `t` is `abs(y2 - 1)` if `y1 <= y2`, otherwise `t` is `abs(m - y2)`. `r` is a list containing six integers `[h, w, x_a, y_a, x_b, y_b]`, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + a`, `x2` is equal to `r[4] - a`, `a` is equal to `y1 - 1` if `y1 <= y2`, otherwise `a` is equal to `m - y1`, `b` is equal to `x2 - x1`, `c` is equal to `r[5] - 1` if `y1 <= y2`, otherwise `c` is equal to `r[3] - r[5]`. Additionally, `x2` is greater than `x1`, `x1` is at least 1, `x2` is less than or equal to `n`, `y1` is equal to `1` if `y1 <= y2`, otherwise `y1` is equal to `m`, and `y2` is equal to `r[5]` if `y1 <= y2`, otherwise `y2` is equal to `r[5] + (m - r[3])`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing.
        else :
            print('draw')
            #This is printed: draw
            return
            #The program returns None
#Overall this is what the function does:The function reads input values representing dimensions and coordinates of two points on a grid, then determines and prints the winner ('Alice' or 'Bob') based on specific movement rules, or prints 'draw' if neither can win. The function does not return any value.

