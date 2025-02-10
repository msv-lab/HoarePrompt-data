#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b, and the sum of h over all test cases does not exceed 10^6.
def func_1():
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: 'draw'
        return
        #The program returns None
    #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, `y2` is equal to `r[5]`. `x2` is greater than `x1`
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns None
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, `y2` is equal to `r[5]`. `x2` is greater than `x1`, and the difference `(x2 - x1)` is odd, and `y1` is not equal to `y2`.
        if (y2 > y1) :
            y1 += 1
            x1 += 1
        else :
            y1 -= 1
            x1 += 1
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1`, and `x2` is equal to `r[4]`. The difference `(x2 - x1)` is odd, `y1` is not equal to `y2`. If `y2` is greater than `y1`, then `y1` is incremented by 1. Otherwise, `y1` is decremented by 1.
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns None
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1`, and `x2` is equal to `r[4]`. The difference `(x2 - x1)` is odd, `y1` is not equal to `y2`, and `y1` is not equal to `y2` after being adjusted (either incremented by 1 or decremented by 1).
        if (y1 >= y2) :
            a = y2 - 1
        else :
            a = m - y2
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1`, and `x2` is equal to `r[4]`. The difference `(x2 - x1)` is odd, `y1` is not equal to `y2`, and `y1` is adjusted to either `y2 - 1` or `m - y2` depending on whether `y1` is greater than or equal to `y2`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program returns None
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1 + a`, `x2` is equal to `r[4] - a`, `b` is the difference between `x2` and `x1`, which is odd, `t` is the absolute value of `y2 - y1`, `x2` is greater than `x1`, `x1` is at least 1, and `x2` is less than or equal to `n`.
        if (abs(y2 - 1) < abs(y2 - m)) :
            y2 = 1
            y1 -= a
            c = y1 - 1
        else :
            y2 = m
            y1 += a
            c = m - y1
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1 + a`, `x2` is equal to `r[4] - a`, `b` is the difference between `x2` and `x1`, which is odd, `t` is the absolute value of `y2 - y1`, `x2` is greater than `x1`, `x1` is at least 1, `x2` is less than or equal to `n`. If `abs(y2 - 1) < abs(y2 - m)`, then `y1` is `y2 - a` and `c` is `y1 - 1`. Otherwise, `y1` is increased by `a` and `c` is `m - y1`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('Alice')
            #This is printed: Alice
            return
            #The program does not return any value since there is no return statement in the given code.
        else :
            print('draw')
            #This is printed: 'draw'
            return
            #The program returns None
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: 'bob'
            return
            #The program returns None
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, `y2` is equal to `r[5]`, `x2` is greater than `x1`, and `(x2 - x1) % 2 == 0`, and `y1` is not equal to `y2`
        if (y2 >= y1) :
            a = y1 - 1
        else :
            a = m - y1
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, `y2` is equal to `r[5]`, `x2` is greater than `x1`, and `(x2 - x1) % 2 == 0`, and `y1` is not equal to `y2`, and if `y2` is greater than or equal to `y1`, then `a` is equal to `y1 - 1`; otherwise, `a` is equal to `m - y1`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is increased by `a`, `x2` is greater than `x1`, and `(x2 - x1) % 2 == 0`, `y1` is not equal to `y2`, `b` is equal to `x2 - x1`, `a` is equal to `y1 - 1` if `y2` is greater than or equal to `y1`; otherwise, `a` is equal to `m - y1`, `t` is equal to `abs(y2 - y1)`, `x2` is decreased by `a`, `x2` is greater than or equal to `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`.
        if (abs(y1 - 1) < abs(y1 - m)) :
            y1 = 1
            y2 -= a
            c = y2 - 1
        else :
            y1 = m
            y2 += a
            c = m - y2
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is increased by `a`, `x2` is greater than or equal to `x1`, `x1` is greater than or equal to 1, `x2` is less than or equal to `n`, `y1` is adjusted to either 1 or `m` depending on the condition, `y2` is adjusted accordingly (either decreased by `a` or increased by `a`), `b` is equal to `x2 - x1`, `a` is calculated as `m - y1` if `y2` is less than `y1` or `y1 - 1` if `y2` is greater than or equal to `y1`, and `t` is equal to `abs(y2 - y1)`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('bob')
            #This is printed: 'bob'
            return
            #The program does not return any value since there is no return statement in the provided code snippet.
        else :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value since there is no return statement in the provided code snippet.
#Overall this is what the function does:The function processes input coordinates (x1, y1) and (x2, y2) to determine if player Alice or Bob wins based on certain conditions. It reads six integers from input representing the coordinates and dimensions of a grid. Depending on the relative positions of the coordinates and their differences, it prints either "Alice", "Bob", or "draw". The function does not return any value.

