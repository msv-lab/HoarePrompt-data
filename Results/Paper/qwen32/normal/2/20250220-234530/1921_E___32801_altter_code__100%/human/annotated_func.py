#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6.
def func_1():
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing (None)
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] for one of the test cases; Each of the next t-1 lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6; `n` is the first element of `r`; `m` is the second element of `r`; `x1` is the third element of `r`; `y1` is the fourth element of `r`; `x2` is the fifth element of `r`; `y2` is the sixth element of `r`. Additionally, `x2` is greater than `x1`.
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing (None)
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] for one of the test cases; Each of the next t-1 lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6; `n` is the first element of `r`; `m` is the second element of `r`; `x1` is the third element of `r`; `y1` is the fourth element of `r`; `x2` is the fifth element of `r`; `y2` is the sixth element of `r`. Additionally, `x2` is greater than `x1` and `(x2 - x1) % 2 != 0`. `y1` is not equal to `y2`.
        if (y2 > y1) :
            y1 += 1
            x1 += 1
        else :
            y1 -= 1
            x1 += 1
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] for one of the test cases; Each of the next t-1 lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6; `n` is the first element of `r`; `m` is the second element of `r`; `x1` is the third element of `r` plus 1; `y1` is the fourth element of `r` plus 1 if `y2` is greater than `y1`, otherwise `y1` is the fourth element of `r` minus 1; `x2` is the fifth element of `r`; `y2` is the sixth element of `r`. Additionally, `x2` is greater than `x1` and `(x2 - x1) % 2 != 0`. `y1` is not equal to `y2`.
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns None
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] for one of the test cases; Each of the next t-1 lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6; `n` is the first element of `r`; `m` is the second element of `r`; `x1` is the third element of `r` plus 1; `y1` is the fourth element of `r` plus 1 if `y2` is greater than `y1`, otherwise `y1` is the fourth element of `r` minus 1; `x2` is the fifth element of `r`; `y2` is the sixth element of `r`. Additionally, `x2` is greater than `x1` and `(x2 - x1) % 2 != 0`. `y1` is not equal to `y2`. Furthermore, `y1` is not equal to `y2` (which is already stated in the precondition), ensuring that the if condition `(y1 == y2)` is false.
        if (y1 >= y2) :
            a = y2 - 1
        else :
            a = m - y2
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] for one of the test cases; Each of the next t-1 lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6; `n` is the first element of `r`; `m` is the second element of `r`; `x1` is the third element of `r` plus 1; `y1` is the fourth element of `r` plus 1 if `y2` is greater than `y1`, otherwise `y1` is the fourth element of `r` minus 1; `x2` is the fifth element of `r`; `y2` is the sixth element of `r`. Additionally, `x2` is greater than `x1` and `(x2 - x1) % 2 != 0`. `y1` is not equal to `y2`. If `y1` is greater than or equal to `y2`, then `a` is `y2 - 1`. Otherwise, if `y1` is less than `y2`, then `a` is `m - y2`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value.
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b]; `n` is the first element of `r`; `m` is the second element of `r`; `x1` is the third element of `r` plus 1 plus (`y2 - 1` if `y1` ≥ `y2` else `m - y2`); `y1` is the fourth element of `r` plus 1 if `y2` > `y1`, otherwise `y1` is the fourth element of `r` minus 1; `x2` is the fifth element of `r` minus (`y2 - 1` if `y1` ≥ `y2` else `m - y2`); `y2` is the sixth element of `r`; `x2` is greater than `x1` and `(x2 - x1) % 2 != 0`; `y1` is not equal to `y2`; `a` is `y2 - 1` if `y1` ≥ `y2`, otherwise `a` is `m - y2`; `b` is `x2 - x1`; `t` is the absolute difference between `y2` and `y1`; `x2` is greater than `x1`, `x1` is at least 1, and `x2` is not greater than `n`.
        if (y2 <= y1) :
            y2 = 1
            y1 -= a
            c = y1 - 1
        else :
            y2 = m
            y1 += a
            c = m - y1
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b]; `n` is the first element of `r`; `m` is the second element of `r`; `x1` is `r[2] + 1` if `y2 > y1`, otherwise `r[2] + 2`; `y1` is `r[3] - 1`; `x2` is the fifth element of `r`; `y2` is `r[6]` if `y2 > y1`, otherwise `1`; `a` is `0` if `y2 > y1`, otherwise `m - y2`; `b` is `x2 - x1`; `t` is the absolute difference between `y2` and `y1`; `x2` is greater than `x1`, `x1` is at least 1, and `x2` is not greater than `n`; `(x2 - x1) % 2 != 0`; `c` is `m - y1` if `y2 > y1`, otherwise `r[3] - 2`.
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
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] for one of the test cases; Each of the next t-1 lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6; `n` is the first element of `r`; `m` is the second element of `r`; `x1` is the third element of `r`; `y1` is the fourth element of `r`; `x2` is the fifth element of `r`; `y2` is the sixth element of `r`. Additionally, `x2` is greater than `x1` and `(x2 - x1) % 2 == 0`. `y1` is not equal to `y2`.
        if (y2 >= y1) :
            a = y1 - 1
        else :
            a = m - y1
        #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] for one of the test cases; Each of the next t-1 lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6; `n` is the first element of `r`; `m` is the second element of `r`; `x1` is the third element of `r`; `y1` is the fourth element of `r`; `x2` is the fifth element of `r`; `y2` is the sixth element of `r`. Additionally, `x2` is greater than `x1` and `(x2 - x1) % 2 == 0`. `y1` is not equal to `y2`. If `y2` is greater than or equal to `y1`, then `a` is `y1 - 1`. Otherwise, `a` is `m - y1`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program returns None
        #State: `t` is `abs(y2 - y1)`, `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b], `n` is the first element of `r`, `m` is the second element of `r`, `x1` is the third element of `r` plus `a`, `y1` is the fourth element of `r`, `x2` is the fifth element of `r` minus `a`, `y2` is the sixth element of `r`, `x2` is greater than `x1` and `(x2 - x1) % 2 == 0`, `y1` is not equal to `y2`, `a` is `y1 - 1` if `y2` is greater than or equal to `y1`, otherwise `a` is `m - y1`, `b` is `x2 - x1`, `x2` is greater than `x1`, `x1` is at least 1, and `x2` is less than or equal to `n`.
        if (y1 <= y2) :
            y1 = 1
            y2 -= a
            c = y2 - 1
        else :
            y1 = m
            y2 += a
            c = m - y2
        #State: `t` is `abs(y2 - 1)` if `y1 <= y2`, otherwise `t` is 0. `r` remains a list of six integers `[h, w, x_a, y_a, x_b, y_b]`. `n` is the first element of `r`, `m` is the second element of `r`, `x1` is the third element of `r` plus `a`, `y1` is 1 if `y1 <= y2`, otherwise `y1` is `m`, `x2` is the fifth element of `r` minus `a`, `y2` remains the same if `y1 <= y2`, otherwise `y2` becomes `m`, `a` is 0, `b` is `x2 - x1`, `x2` is greater than `x1` and `(x2 - x1) % 2 == 0`, `y1` is not equal to `y2` if `y1 <= y2`, otherwise `y1` is equal to `y2`, `x1` is at least 1, `x2` is less than or equal to `n`, and `c` is `t` if `y1 <= y2`, otherwise `c` is 0.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing (None)
        else :
            print('draw')
            #This is printed: draw
            return
            #The program returns None
#Overall this is what the function does:The function reads input values representing dimensions and coordinates of two points on a grid. It then determines and prints the winner ('Alice' or 'Bob') based on specific conditions related to the positions and movements of these points, or it prints 'draw' if neither player wins. The function does not return any value.

