#State of the program right berfore the function call: The function `func_1` is expected to take input parameters, but the function definition provided does not include any parameters. The correct function definition should include parameters for the board dimensions `h` and `w`, and the initial positions of Alice's and Bob's chips `(x_a, y_a)` and `(x_b, y_b)`. The input should be structured as multiple test cases, each consisting of six integers: `h`, `w`, `x_a`, `y_a`, `x_b`, and `y_b`, where `1 \le x_a, x_b \le h \le 10^6`, `1 \le y_a, y_b \le w \le 10^9`, and it is guaranteed that either `x_a \ne x_b` or `y_a \ne y_b`.
def func_1():
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns without any value.
    #State: `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, `y2` is equal to `r[5]`, and `x2` is greater than `x1`.
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing.
        #State: `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, `y2` is equal to `r[5]`, `x2` is greater than `x1`, the difference between `x2` and `x1` is an odd number, and `y1` is not equal to `y2`.
        if (y2 > y1) :
            y1 += 1
            x1 += 1
        else :
            y1 -= 1
            x1 += 1
        #State: *`n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1`, `x2` is equal to `r[4]`, `x2` is greater than `x1`, the difference between `x2` and `x1` is an even number, and `y1` is not equal to `y2`. If `y2` > `y1`, then `y1` is equal to `r[3] + 1` and `y2` is greater than `y1`. Otherwise, `y1` is equal to `r[3] - 1` and `y2` is less than or equal to `y1`.
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program does not return any value.
        #State: *`n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1`, `x2` is equal to `r[4]`, `x2` is greater than `x1`, the difference between `x2` and `x1` is an even number, and `y1` is not equal to `y2`. If `y2` > `y1`, then `y1` is equal to `r[3] + 1` and `y2` is greater than `y1`. Otherwise, `y1` is equal to `r[3] - 1` and `y2` is less than or equal to `y1`. Additionally, `y1` is not equal to `y2`.
        if (y1 >= y2) :
            a = y2 - 1
        else :
            a = m - y2
        #State: *`n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1`, `x2` is equal to `r[4]`, `x2` is greater than `x1`, the difference between `x2` and `x1` is an even number, and `y1` is not equal to `y2`. If `y1` >= `y2`, then `y1` is `r[3] - 1`, `y2` is less than or equal to `y1`, and `a` is `y2 - 1`. Otherwise, `y1` is `r[3] + 1`, `y2` is greater than `y1`, and `a` is equal to `r[1] - y2`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value.
        #State: `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1 + a`, `x2` is equal to `r[4] - a`, the difference between `x2` and `x1` is an even number, `y1` is not equal to `y2`, if `y1` >= `y2`, then `y1` is `r[3] - 1`, `y2` is less than or equal to `y1`, and `a` is `y2 - 1`. Otherwise, `y1` is `r[3] + 1`, `y2` is greater than `y1`, and `a` is equal to `r[1] - y2`. `b` is equal to `x2 - x1`, `t` is the absolute difference between `y2` and `y1`. Additionally, `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`.
        if (y2 <= y1) :
            y2 = 1
            y1 -= a
            c = y1 - 1
        else :
            y2 = m
            y1 += a
            c = m - y1
        #State: *`n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1 + a`, `x2` is equal to `r[4] - a`, the difference between `x2` and `x1` is an even number, `b` is equal to `x2 - x1`, `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`. If `y2` <= `y1`, then `y1` is `r[3] - 1`, `y2` is 1, `a` is 0, `t` is the absolute difference between `y2` and `y1`, and `c` is `y1 - 1`. Otherwise, if `y2` > `y1`, then `y1` is `r[3] + 1 + a`, `y2` is equal to `m`, `a` is `r[1] - y2`, `t` is the absolute difference between `y2` and `y1`, and `c` is `m - y1`.
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
            #The program returns nothing.
        #State: *`n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, `y2` is equal to `r[5]`, and `x2` is greater than `x1`. Additionally, the difference between `x2` and `x1` is even, and `y1` is not equal to `y2`.
        if (y2 >= y1) :
            a = y1 - 1
        else :
            a = m - y1
        #State: *`n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, `y2` is equal to `r[5]`, `x2` is greater than `x1`, the difference between `x2` and `x1` is even, and `y1` is not equal to `y2`. If `y2` is greater than or equal to `y1`, `a` is set to `y1 - 1`. If `y2` is less than `y1`, `a` is set to `m - y1`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value.
        #State: `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + a`, `y1` is equal to `r[3]`, `x2` is equal to `r[4] - a`, `y2` is equal to `r[5]`, `x2` is greater than `x1`, the difference between `x2` and `x1` is even, `y1` is not equal to `y2`, `b` is equal to `x2 - x1 - a`, `t` is equal to `abs(y2 - y1)`, and `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`.
        if (y1 <= y2) :
            y1 = 1
            y2 -= a
            c = y2 - 1
        else :
            y1 = m
            y2 += a
            c = m - y2
        #State: *`n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + a`, `x2` is equal to `r[4] - a`, `x2` is greater than `x1`, the difference between `x2` and `x1` is even, `x1` is greater than or equal to 1, `x2` is less than or equal to `n`, `b` is equal to `x2 - x1 - a`, `t` is equal to `abs(y2 - y1)`, and `y1` is not equal to `y2`. If `y1` <= `y2`, then `y1` is 1 and `y2` is `r[5] - a`, and `c` is equal to `y2 - 1`. Otherwise, `y1` is `m` and `y2` is `r[5] + a`, and `c` is equal to `m - y2`.
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
#Overall this is what the function does:The function `func_1` reads a list of six integers from the input, representing the dimensions of a board (`h`, `w`) and the initial positions of Alice's and Bob's chips (`x_a`, `y_a`, `x_b`, `y_b`). It then determines the outcome of a game between Alice and Bob based on the positions of their chips. The function prints either 'Alice', 'bob', or 'draw' depending on the game's result and does not return any value. The final state of the program is that the input has been processed, and the game's outcome has been printed to the console.

