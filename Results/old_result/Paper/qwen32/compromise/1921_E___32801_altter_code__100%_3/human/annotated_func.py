#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. Each of the following t lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9. It is guaranteed that x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6.
def func_1():
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing.
    #State: `t` is a positive integer such that 1 <= t <= 10^4; `r` is a list of integers; `n` is `r[0]`; `m` is `r[1]`; `x1` is `r[2]`; `y1` is `r[3]`; `x2` is `r[4]`; `y2` is `r[5]`; `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state; `x2` is greater than `x1`.
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing.
        #State: `t` is a positive integer such that 1 <= t <= 10^4; `r` is a list of integers; `n` is `r[0]`; `m` is `r[1]`; `x1` is `r[2]`; `y1` is `r[3]`; `x2` is `r[4]`; `y2` is `r[5]`; `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state; `x2` is greater than `x1`; the difference between `x2` and `x1` is odd; `y1` is not equal to `y2`
        if (y2 > y1) :
            y1 += 1
            x1 += 1
        else :
            y1 -= 1
            x1 += 1
        #State: `t` is a positive integer such that 1 <= t <= 10^4; `r` is a list of integers; `n` is `r[0]`; `m` is `r[1]`; `x1` is `r[2] + 1`; `y1` is `r[3] + 1` if `y2` is greater than `y1`, otherwise `y1` is `r[3] - 1`; `x2` is `r[4]`; `y2` is `r[5]`; `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state; `x2` is greater than `x1`; the difference between `x2` and `x1` is even; `y1` is not equal to `y2`.
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing.
        #State: `t` is a positive integer such that 1 <= t <= 10^4; `r` is a list of integers; `n` is `r[0]`; `m` is `r[1]`; `x1` is `r[2] + 1`; `y1` is `r[3] + 1` if `y2` is greater than `r[3] + 1`, otherwise `y1` is `r[3] - 1`; `x2` is `r[4]`; `y2` is `r[5]`; `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state; `x2` is greater than `x1`; the difference between `x2` and `x1` is even; `y1` is not equal to `y2`.
        if (y1 >= y2) :
            a = y2 - 1
        else :
            a = m - y2
        #State: `t` is a positive integer such that 1 <= t <= 10^4; `r` is a list of integers; `n` is `r[0]`; `m` is `r[1]`; `x1` is `r[2] + 1`; `y1` is `r[3] + 1` if `y2` is greater than `r[3] + 1`, otherwise `y1` is `r[3] - 1`; `x2` is `r[4]`; `y2` is `r[5]`; `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state; `x2` is greater than `x1`; the difference between `x2` and `x1` is even; `y1` is not equal to `y2`. If `y1` is greater than or equal to `y2`, `a` is `y2 - 1`. If `y1` is less than `y2`, `a` is `m - y2`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program returns nothing (None)
        #State: `t` is `abs(y2 - y1)`, `r` is a list of integers; `n` is `r[0]`; `m` is `r[1]`; `x1` is `r[2] + y2` if `y1` is greater than `y2`, otherwise `x1` is `r[2] + 1 + m - y2`; `y1` is `r[3] + 1` if `y2` is greater than `r[3] + 1`, otherwise `y1` is `r[3] - 1`; `x2` is `x2 - a`; `y2` is `r[5]`; `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state; `x2` is greater than `x1`; the difference between `x2` and `x1` is even; `y1` is not equal to `y2`. If `y1` is greater than or equal to `y2`, `a` is `y2 - 1`. If `y1` is less than `y2`, `a` is `m - y2`. `b` is `x2 - x1`, which is an even positive integer. Additionally, `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`.
        if (y2 <= y1) :
            y2 = 1
            y1 -= a
            c = y1 - 1
        else :
            y2 = m
            y1 += a
            c = m - y1
        #State: `t` is `abs(y2 - y1)`, `r` is a list of integers; `n` is `r[0]`; `m` is `r[1]`; `x1` is `r[2] + y2` if `y1` is greater than `y2`, otherwise `x1` is `r[2] + 1 + m - y2`; `y1` is `r[3] + 1` if `y2` is greater than `r[3] + 1`, otherwise `y1` is `r[3] - 1`; `x2` is `x2 - a`; `y2` is `1` if `y2 <= y1`, otherwise `y2` is `m`; `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state; `x2` is greater than `x1`; the difference between `x2` and `x1` is even; `y1` is not equal to `y2`; `a` is `0` if `y2 <= y1`, otherwise `a` is `m - y2`; `b` is `x2 - x1`, which is an even positive integer; `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`; `c` is `y1 - 1` if `y2 <= y1`, otherwise `c` is `r[1] - (r[3] - 1)`
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns None
        else :
            print('draw')
            #This is printed: draw
            return
            #The program returns nothing (None)
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing (None)
        #State: `t` is a positive integer such that 1 <= t <= 10^4; `r` is a list of integers; `n` is `r[0]`; `m` is `r[1]`; `x1` is `r[2]`; `y1` is `r[3]`; `x2` is `r[4]`; `y2` is `r[5]`; `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state; `x2` is greater than `x1`; `(x2 - x1)` is an even number; `y1` is not equal to `y2`
        if (y2 >= y1) :
            a = y1 - 1
        else :
            a = m - y1
        #State: `t` is a positive integer such that 1 <= t <= 10^4; `r` is a list of integers; `n` is `r[0]`; `m` is `r[1]`; `x1` is `r[2]`; `y1` is `r[3]`; `x2` is `r[4]`; `y2` is `r[5]`; `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state; `x2` is greater than `x1`; `(x2 - x1)` is an even number; `y1` is not equal to `y2`; if `y2` is greater than or equal to `y1`, `a` is `y1 - 1`; otherwise, `a` is `m - y1`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program returns nothing.
        #State: `t` is `abs(y2 - y1)`, `r` is a list of integers, `n` is `r[0]`, `m` is `r[1]`, `x1` is `r[2] + a`, `y1` is `r[3]`, `x2` is `r[4] - a`, `y2` is `r[5]`, `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state, `x2` is greater than `x1`, `(x2 - x1)` is an even number, `y1` is not equal to `y2`, if `y2` is greater than or equal to `y1`, `a` is `y1 - 1`; otherwise, `a` is `m - y1`, `b` is `x2 - x1`, `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`
        if (y1 <= y2) :
            y1 = 1
            y2 -= a
            c = y2 - 1
        else :
            y1 = m
            y2 += a
            c = m - y2
        #State: `t` is `abs(y2 - 1)` if `y1 <= y2`, otherwise `t` is `abs(y2 - y1)`. `r` is a list of integers, `n` is `r[0]`, `m` is `r[1]`, `x1` is `r[2] + a`, `x2` is `r[4] - a`, `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as described in the initial state, `x2` is greater than `x1`, `(x2 - x1)` is an even number, `y2` is greater than or equal to `1` if `y1 <= y2`, otherwise `y1` is greater than `y2`, `a` is `1 - 1` if `y1 <= y2`, otherwise `m - y1`, `b` is `x2 - x1`, `x1` is greater than or equal to `1`, `x2` is less than or equal to `n`, `y1` is `1` if `y1 <= y2`, otherwise `y1` is `m`, `y2` is `r[5]` if `y1 <= y2`, otherwise `y2` is `y2 + (m - y1)`, `c` is `t`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing (None)
        else :
            print('draw')
            #This is printed: draw
            return
            #The program returns nothing.
#Overall this is what the function does:The function reads input values representing dimensions and coordinates, then determines and prints the result of a game based on the given conditions. The function does not return any value.

