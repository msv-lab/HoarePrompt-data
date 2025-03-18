#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the following t lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6.
def func_1():
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns None
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list containing the single integer `t`; `n`, `m`, `x1`, `y1`, `x2`, and `y2` are not assigned values; `x2` is greater than `x1`.
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns None
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list containing the single integer `t`; `n`, `m`, `x1`, `y1`, `x2`, and `y2` are not assigned values; `x2` is greater than `x1`; the difference between `x2` and `x1` is odd; `y1` is not equal to `y2`.
        if (y2 > y1) :
            y1 += 1
            x1 += 1
        else :
            y1 -= 1
            x1 += 1
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list containing the single integer `t`; `n` and `m` are not assigned values; if `y2` > `y1`, then `y1` is incremented by 1 and `x2` is greater than `x1 + 1` with the difference between `x2` and `x1 + 1` being even; otherwise, `y1` is decremented by 1, `x1` is incremented by 1, and `x2` is greater than `x1` with the difference between `x2` and `x1` being odd; `y1` is not equal to `y2`.
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program does not return any value.
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list containing the single integer `t`; `n` and `m` are not assigned values; `y1` is not equal to `y2`. If `y2` > `y1`, then `y1` has been incremented by 1 and `x2` is greater than `x1 + 1` with the difference between `x2` and `x1 + 1` being even; otherwise, `y1` has been decremented by 1, `x1` has been incremented by 1, and `x2` is greater than `x1` with the difference between `x2` and `x1` being odd.
        if (y1 >= y2) :
            a = y2 - 1
        else :
            a = m - y2
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list containing the single integer `t`; `n` and `m` are not assigned values; `y1` is not equal to `y2`. If `y1` was originally greater than or equal to `y2`, then `y1` has been decremented by 1, `x1` has been incremented by 1, and `x2` is greater than `x1` with the difference between `x2` and `x1` being odd; `a` is `y2 - 1`. If `y1` was originally less than `y2`, then `y1` remains unchanged, `x1` has been incremented by 1, and `x2` is greater than `x1` with the difference between `x2` and `x1` being odd; `a` is `m - y2`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value.
        #State: `t` is `abs(y2 - y1)`, `r` is a list containing the single integer `t`, `n` and `m` are not assigned values, `y1` remains unchanged from its post-initialization state, `x1` is `x1 + a`, `x2` is `x2 - a`, `a` is `y2 - 1` if `y1` was originally `>= y2`, or `m - y2` if `y1` was originally `< y2`, `b` is an odd positive integer equal to `x2 - x1` before the modification, and `x2` is greater than `x1`, `x1` is at least 1, and `x2` is less than or equal to `n`
        if (y2 <= y1) :
            y2 = 1
            y1 -= a
            c = y1 - 1
        else :
            y2 = m
            y1 += a
            c = m - y1
        #State: `t` is `abs(1 - y1)` if `y2 <= y1`, otherwise `t` is `abs(m - y1)`. `r` is a list containing the single integer `abs(1 - y1)` if `y2 <= y1`, otherwise `r` is a list containing the single integer `abs(m - y1)`. `n` and `m` are not assigned values. `y1` remains unchanged. `x1` is `x1 + a` if `y2 > y1`, otherwise `x1` remains unchanged. `x2` is `x2 - a` if `y2 > y1`, otherwise `x2` remains unchanged. `a` is `0` if `y2 <= y1`, otherwise `a` is `m - y2`. `b` is an odd positive integer equal to `x2 - x1` before the modification. `x2` is greater than `x1`. `x1` is at least `1`. `x2` is less than or equal to `n`. `y2` is `1` if `y2 <= y1`, otherwise `y2` is `m`. `c` is `y1 - 1` if `y2 <= y1`, otherwise `c` is `m - y1`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing (None)
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
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list containing the single integer `t`; `n`, `m`, `x1`, `y1`, `x2`, and `y2` are not assigned values; `x2` is greater than `x1`; the difference between `x2` and `x1` is even; `y1` is not equal to `y2`
        if (y2 >= y1) :
            a = y1 - 1
        else :
            a = m - y1
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list containing the single integer `t`; `n`, `m`, `x1`, `y1`, `x2`, and `y2` are not assigned values; `x2` is greater than `x1`; the difference between `x2` and `x1` is even; `y1` is not equal to `y2`; if `y2` is greater than or equal to `y1`, then `a` is `y1 - 1`; otherwise, `a` is `m - y1`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program returns nothing (None)
        #State: `t` is `abs(y2 - y1)`, `r` is a list containing the single integer `abs(y2 - y1)`, `x1` is `x1 + a`, `y1` is not equal to `y2`, if `y2` is greater than or equal to `y1`, then `a` is `y1 - 1`; otherwise, `a` is `m - y1`; `b` is a positive even integer equal to `x2 - x1`; `x2` is `x2 - a`; `n`, `m`, `y2` are not assigned values; `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`.
        if (y1 <= y2) :
            y1 = 1
            y2 -= a
            c = y2 - 1
        else :
            y1 = m
            y2 += a
            c = m - y2
        #State: `t` is either `abs(y2 - 1)` or `abs(y2 - m)`, depending on whether `y1` is less than or equal to `y2` or not. `r` is a list containing the single integer `abs(y2 - 1)` if `y1` is less than or equal to `y2`, otherwise it contains `abs(y2 - y1)`. `x1` is `x1 + a`, where `a` is `0` if `y1` is less than or equal to `y2`, and `m - y1` if `y1` is greater than `y2`. `y1` is `1` if `y1` is less than or equal to `y2`, otherwise it is `m`. `y2` remains unchanged and is greater than or equal to `1` if `y1` is less than or equal to `y2`, otherwise it is less than `y1`. `a` is `0` if `y1` is less than or equal to `y2`, and `m - y1` if `y1` is greater than `y2`. `b` is a positive even integer equal to `x2 - x1`. `x2` is `x2` if `y1` is less than or equal to `y2`, otherwise it is `x2 - a`. `c` is `y2 - 1` if `y1` is less than or equal to `y2`, otherwise it is `m - y2`. `n`, `m`, `y2` are not assigned new values. `x2` is greater than `x1`, `x1` is greater than or equal to `1`, and `x2` is less than or equal to `n`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('bob')
            #This is printed: bob
            return
            #The program does not return any value.
        else :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of grid dimensions and coordinates of two points. It determines the winner of a game based on specific movement rules and prints either 'Alice', 'Bob', or 'draw' for each test case. The function does not return any value.

