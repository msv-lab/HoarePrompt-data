#State of the program right berfore the function call: The function should actually be defined with parameters to match the problem description, such as `def func_1(t, test_cases):`, where `t` is an integer representing the number of test cases, and `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. Each tuple must satisfy the conditions 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and it is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6.
def func_1():
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing.
    #State: `r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, and `y2` is equal to `r[5]`. Additionally, `x2` is greater than `x1`.
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program does not return any value.
        #State: *`r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, and `y2` is equal to `r[5]`. Additionally, `x2` is greater than `x1`, and the difference between `x2` and `x1` is an odd number. `y1` is not equal to `y2`.
        if (y2 > y1) :
            y1 += 1
            x1 += 1
        else :
            y1 -= 1
            x1 += 1
        #State: *`r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1`, and `x2` is equal to `r[4]`. Additionally, `x2` is greater than `x1`, and the difference between `x2` and `x1` is an odd number. `y1` is not equal to `y2`. If `y2` > `y1`, then `y1` is equal to `r[3] + 1` and `y2` is equal to `r[5]`. Otherwise, `y1` is equal to `r[3] - 1` and `y2` is equal to `r[5]`.
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing.
        #State: *`r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1`, and `x2` is equal to `r[4]`. Additionally, `x2` is greater than `x1`, and the difference between `x2` and `x1` is an odd number. `y1` is not equal to `y2`. If `y2` > `y1`, then `y1` is equal to `r[3] + 1` and `y2` is equal to `r[5]`. Otherwise, `y1` is equal to `r[3] - 1` and `y2` is equal to `r[5]`. `y1` is not equal to `y2`.
        if (y1 >= y2) :
            a = y2 - 1
        else :
            a = m - y2
        #State: *`r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1`, and `x2` is equal to `r[4]`. Additionally, `x2` is greater than `x1`, and the difference between `x2` and `x1` is an odd number. `y1` is not equal to `y2`. If `y1` >= `y2`, then `y1` is equal to `r[3] - 1`, `y2` is equal to `r[5]`, and `a` is equal to `r[5] - 1`. Otherwise, if `y1` < `y2`, then `y1` is equal to `r[3] + 1`, `y2` is equal to `r[5]`, and `a` is equal to `r[1] - r[5]`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value.
        #State: `r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1 + a`, `x2` is equal to `r[4] - a`, `y1` is not equal to `y2`. If `y1` >= `y2`, then `y1` is equal to `r[3] - 1`, `y2` is equal to `r[5]`, and `a` is equal to `r[5] - 1`. Otherwise, if `y1` < `y2`, then `y1` is equal to `r[3] + 1`, `y2` is equal to `r[5]`, and `a` is equal to `r[1] - r[5]`. `b` is equal to `x2 - x1`, and the difference between `x2` and `x1` is an odd number. `t` is equal to `abs(y2 - y1)`. Additionally, `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`.
        if (y2 <= y1) :
            y2 = 1
            y1 -= a
            c = y1 - 1
        else :
            y2 = m
            y1 += a
            c = m - y1
        #State: `r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + 1 + a`, `x2` is equal to `r[4] - a`, `b` is equal to `x2 - x1`, and the difference between `x2` and `x1` is an odd number. `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`. If `y2 <= y1`, then `x1` is equal to `r[2] + 1 + (r[5] - 1)`, `x2` is equal to `r[4] - (r[5] - 1)`, `y1` is equal to `r[3] - 1 - (r[5] - 1)`, `y2` is equal to 1, `a` is equal to `r[5] - 1`, `b` is equal to `x2 - x1`, the difference between `x2` and `x1` is an odd number, `t` is equal to `abs(1 - (r[3] - 1))`, and `c` is equal to `y1 - 1`. Otherwise, if `y2 > y1`, then `y1` is now equal to `y1 + a`, `y1` is not equal to `y2`, `y1` is less than `y2`, `y2` is now equal to `m`, `c` is equal to `m - y1`, and `t` is equal to `abs(y2 - y1)`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing.
        else :
            print('draw')
            #This is printed: draw
            return
            #The program returns nothing.
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing.
        #State: `r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, and `y2` is equal to `r[5]`. Additionally, `x2` is greater than `x1`, and the difference between `x2` and `x1` is even. `y1` is not equal to `y2`.
        if (y2 >= y1) :
            a = y1 - 1
        else :
            a = m - y1
        #State: *`r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2]`, `y1` is equal to `r[3]`, `x2` is equal to `r[4]`, and `y2` is equal to `r[5]`. Additionally, `x2` is greater than `x1`, and the difference between `x2` and `x1` is even. `y1` is not equal to `y2`. If `y2` is greater than or equal to `y1`, `a` is equal to `y1 - 1`. If `y2` is less than `y1`, `a` is equal to `m - y1`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program does not return any value.
        #State: `r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + a`, `y1` is equal to `r[3]`, `x2` is equal to `r[4] - a`, and `y2` is equal to `r[5]`. Additionally, `x2` is greater than `x1`, and the difference between `x2` and `x1` is even. `y1` is not equal to `y2`. If `y2` is greater than or equal to `y1`, `a` is equal to `y1 - 1`. If `y2` is less than `y1`, `a` is equal to `m - y1`. `b` is equal to `x2 - x1`. `t` is equal to `abs(y2 - y1)`. `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`.
        if (y1 <= y2) :
            y1 = 1
            y2 -= a
            c = y2 - 1
        else :
            y1 = m
            y2 += a
            c = m - y2
        #State: `r` is a list of integers, `t` is an integer representing the number of test cases, `test_cases` is a list of tuples, each containing six integers (h, w, x_a, y_a, x_b, y_b) representing the dimensions of the board and the initial positions of Alice's and Bob's chips. `n` is equal to `r[0]`, `m` is equal to `r[1]`, `x1` is equal to `r[2] + a`, `x2` is equal to `r[4] - a`, and `y2` is equal to `r[5]`. `x2` is greater than `x1`, and the difference between `x2` and `x1` is even. `y1` is not equal to `y2`. `b` is equal to `x2 - x1`. `t` is equal to `abs(y2 - y1)`. `x2` is greater than `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`. If `y1` is less than or equal to `y2`, `y1` is set to 1, `a` is set to 0, and `c` is set to `y2 - 1`. If `y1` is greater than `y2`, `y1` is set to `m`, `a` is set to `m - y1`, and `c` is set to `m - y2`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('bob')
            #This is printed: bob
            return
            #The program does not return any value.
        else :
            print('draw')
            #This is printed: draw
            return
            #The program returns nothing.
#Overall this is what the function does:The function `func_1` reads a single line of input containing six integers (n, m, x1, y1, x2, y2) and determines the outcome of a game between Alice and Bob. The game is played on a board of dimensions n x m, with Alice's chip initially at position (x1, y1) and Bob's chip at position (x2, y2). The function prints 'Alice', 'bob', or 'draw' based on the positions and the rules of the game. The function does not return any value.

