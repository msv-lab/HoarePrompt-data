#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b, representing the dimensions of the board and the initial positions of Alice's and Bob's chips.
def func_1():
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program does not return any value.
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is `r[0]`, `m` is `r[1]`, `x1` is `r[2]`, `y1` is `r[3]`, `x2` is `r[4]`, `y2` is `r[5]`, and `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. Additionally, `x2` is greater than `x1`.
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program does not return any value.
        #State: *`t` is an integer where 1 ≤ t ≤ 10^4, `n` is `r[0]`, `m` is `r[1]`, `x1` is `r[2]`, `y1` is `r[3]`, `x2` is `r[4]`, `y2` is `r[5]`, and `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. Additionally, `x2` is greater than `x1`. The difference between `x2` and `x1` is odd. `y1` is not equal to `y2`.
        if (y2 > y1) :
            y1 += 1
            x1 += 1
        else :
            y1 -= 1
            x1 += 1
        #State: *`t` is an integer where 1 ≤ t ≤ 10^4, `n` is `r[0]`, `m` is `r[1]`, `x1` is `r[2] + 1`, `x2` is `r[4]`, `y2` is `r[5]`, and `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. Additionally, `x2` is greater than `x1`. The difference between `x2` and `x1` is odd. `y1` is not equal to `y2`. If `y2` > `y1`, then `y1` is `r[3] + 1`. Otherwise, `y1` is `r[3] - 1` and the difference between `x2` and `x1` is even.
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program does not return any value.
        if (y1 >= y2) :
            a = y2 - 1
        else :
            a = m - y2
        #State: *`t` is an integer where 1 ≤ t ≤ 10^4, `n` is `r[0]`, `m` is `r[1]`, `x1` is `r[2] + 1`, `x2` is `r[4]`, `y2` is `r[5]`, and `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. Additionally, `x2` is greater than `x1`, the difference between `x2` and `x1` is even, and `y1` is not equal to `y2`. If `y1` ≥ `y2`, then `a` is `r[5] - 1`. Otherwise, `y1` is less than `y2`, and `a` is `r[1] - r[5]`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value.
        #State: `t` is `abs(y2 - y1)`, `n` is `r[0]`, `m` is `r[1]`, `x1` is `r[2] + 1 + a`, `x2` is `r[4] - a`, `y2` is `r[5]`, `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b, `x2` is greater than `x1`, the difference between `x2` and `x1` is even, and `y1` is not equal to `y2`, if `y1` ≥ `y2`, then `a` is `r[5] - 1`. Otherwise, `y1` is less than `y2`, and `a` is `r[1] - r[5]`, `b` is `x2 - x1`. Additionally, `x2 > x1`, `x1 ≥ 1`, and `x2 ≤ n`.
        if (y2 <= y1) :
            y2 = 1
            y1 -= a
            c = y1 - 1
        else :
            y2 = m
            y1 += a
            c = m - y1
        #State: *`t` is `abs(y2 - y1)`, `n` is `r[0]`, `m` is `r[1]`, `x1` is `r[2] + 1 + a`, `x2` is `r[4] - a`, `y2` is `r[5]`, `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b, `x2` is greater than `x1`, the difference between `x2` and `x1` is even, `y1` is not equal to `y2`, `a` is `r[5] - 1` if `y2 <= y1` and `r[1] - r[5]` otherwise, `b` is `x2 - x1`, `x2 > x1`, `x1 ≥ 1`, `x2 ≤ n`, `c` is `y1 - 1` if `y2 <= y1` and `m - (y1 + (m - y2))` otherwise.
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
            #The program does not return any value.
        #State: *`t` is an integer where 1 ≤ t ≤ 10^4, `n` is `r[0]`, `m` is `r[1]`, `x1` is `r[2]`, `y1` is `r[3]`, `x2` is `r[4]`, `y2` is `r[5]`, and `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. Additionally, `x2` is greater than `x1`. The difference between `x2` and `x1` is even. `y1` is not equal to `y2`.
        if (y2 >= y1) :
            a = y1 - 1
        else :
            a = m - y1
        #State: *`t` is an integer where 1 ≤ t ≤ 10^4, `n` is `r[0]`, `m` is `r[1]`, `x1` is `r[2]`, `y1` is `r[3]`, `x2` is `r[4]`, `y2` is `r[5]`, and `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b] where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. Additionally, `x2` is greater than `x1`, the difference between `x2` and `x1` is even, and `y1` is not equal to `y2`. If `y2` is greater than or equal to `y1`, `a` is set to `y1 - 1`. If `y2` is less than `y1`, `a` is set to `m - y1`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value.
        #State: `t` is the absolute value of the difference between `y2` and `y1`, `n` is `r[0]`, `m` is `r[1]`, `x1` is `x_a + a`, `y1` is `r[3]`, `x2` is `r[4] - a`, `y2` is `r[5]`, `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b], `x2` is greater than `x1`, the difference between `x2` and `x1` is even, `y1` is not equal to `y2`, `b` is `x2 - x1`. Additionally, `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`.
        if (y1 <= y2) :
            y1 = 1
            y2 -= a
            c = y2 - 1
        else :
            y1 = m
            y2 += a
            c = m - y2
        #State: *`t` is the absolute value of the difference between `y2` and `y1`, `n` is `r[0]`, `m` is `r[1]`, `x1` is `x_a + a`, `y1` is either 1 or `m`, `x2` is `r[4] - a`, `y2` is either `r[5] - a` or `r[5] + a`, `r` is a list of six integers [h, w, x_a, y_a, x_b, y_b], `x2` is greater than `x1`, the difference between `x2` and `x1` is even, `y1` is not equal to `y2`, `b` is `x2 - x1`, `x2` is greater than `x1`, `x1` is greater than or equal to 1, `x2` is less than or equal to `n`. If `y1` is less than or equal to `y2`, then `y1` is set to 1, `y2` is set to `r[5] - a`, and `c` is `r[5] - a - 1`. Otherwise, `y1` is set to `m`, `y2` is set to `r[5] + a`, and `c` is `m - y2`.
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
#Overall this is what the function does:The function `func_1` processes a single test case involving a game played on a rectangular board. It takes no explicit parameters but reads input from the standard input, expecting six integers: `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b`, which represent the dimensions of the board and the initial positions of Alice's and Bob's chips, respectively. The function determines the outcome of the game based on the positions of the chips and prints one of three possible results: 'Alice', 'Bob', or 'draw'. The function does not return any value. After the function concludes, the input values are consumed, and the program state reflects the printed result of the game.

