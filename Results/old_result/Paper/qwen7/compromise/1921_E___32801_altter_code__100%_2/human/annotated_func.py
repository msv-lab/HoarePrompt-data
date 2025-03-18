#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six integers h, w, x_a, y_a, x_b, y_b such that 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9, and it is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. Additionally, the sum of h over all test cases does not exceed 10^6.
def func_1():
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program does not return any value since there is no return statement in the provided code snippet.
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4, r is a list containing six integers [n, m, x1, y1, x2, y2], where n, m, x1, y1, x2, and y2 are the integers obtained from the input split and converted to integers, and x2 is greater than x1
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns None
        #State: t is a positive integer such that 1 ≤ t ≤ 10^4, r is a list containing six integers [n, m, x1, y1, x2, y2], where n, m, x1, y1, x2, and y2 are the integers obtained from the input split and converted to integers, x2 is greater than x1, and the difference (x2 - x1) is odd, and y1 is not equal to y2
        if (y2 > y1) :
            y1 += 1
            x1 += 1
        else :
            y1 -= 1
            x1 += 1
        #State: t is a positive integer such that 1 ≤ t ≤ 10^4, r is a list containing six integers [n, m, x1 + 1, y, x2, y2], where n, m, x1, y1, x2, and y2 are the integers obtained from the input split and converted to integers, x2 is greater than x1, the difference (x2 - x1) is odd, and y is either y1 + 1 or y2 - 1 depending on whether y2 > y1 or y2 <= y1, respectively.
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns a list [n, m, x1 + 1, y, x2, y2] where n and m are integers, x1 + 1 and x2 are integers with x2 being greater than x1 and the difference (x2 - x1) being odd, and y is equal to y1 which is also equal to y2.
        #State: t is a positive integer such that 1 ≤ t ≤ 10^4, r is a list containing six integers [n, m, x1 + 1, y, x2, y2], where n, m, x1, y1, x2, and y2 are the integers obtained from the input split and converted to integers, x2 is greater than x1, the difference (x2 - x1) is odd, and y is either y1 + 1 or y2 - 1 depending on whether y2 > y1 or y2 <= y1, respectively. Additionally, y1 is not equal to y2.
        if (y1 >= y2) :
            a = y2 - 1
        else :
            a = m - y2
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `r` is a list containing six integers [n, m, x1 + 1, y, x2, y2], where n, m, x1, y1, x2, and y2 are the integers obtained from the input split and converted to integers, x2 is greater than x1, the difference (x2 - x1) is odd, and y is y2 - 1. Additionally, y1 is not equal to y2. In the if part, if `y1` is greater than or equal to `y2`, then `a` is set to `y2 - 1`. In the else part, if `y1` is less than `y2`, then `a` is set to `m - y2`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: 'draw'
            return
            #The program returns None
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `r` is a list containing six integers [n, m, x1 + a, y, x2 - a, y2], `b` is the value of (x2 - a) - x1, where x2 - a is greater than x1, the difference ((x2 - a) - x1) is even, and y is y2 - 1; `t` is equal to the absolute value of y2 - y1, and the condition (x2 > x1 and x1 ≥ 1 and x2 ≤ n) holds.
        if (y2 <= y1) :
            y2 = 1
            y1 -= a
            c = y1 - 1
        else :
            y2 = m
            y1 += a
            c = m - y1
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `r` is a list containing six integers [n, m, x1 + a, y, x2 - a, y2], `b` is the value of (x2 - a) - x1, and the difference ((x2 - a) - x1) is even. `y` is either y2 - 1 or 0, depending on whether y2 is less than or equal to y1 or not. If y2 <= y1, then y is 0 and `t` is equal to the absolute value of 1 - y1. If y2 > y1, then y is y2 - 1 and `t` is equal to the absolute value of y2 - y1. `c` is either y1 - 1 or m - y1, depending on the same condition as above. The condition (x2 > x1 and x1 ≥ 1 and x2 ≤ n) holds.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns a value of `t` which is the absolute value of the difference between `y2` and `y1` if `y2` is greater than `y1`, otherwise it returns the absolute value of `1 - y1`.
        else :
            print('draw')
            #This is printed: 'draw'
            return
            #The program returns None
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program does not return any value since there is no return statement in the provided code snippet.
        #State: t is a positive integer such that 1 ≤ t ≤ 10^4, r is a list containing six integers [n, m, x1, y1, x2, y2], where n, m, x1, y1, x2, and y2 are the integers obtained from the input split and converted to integers, and (x2 - x1) % 2 == 0, and y1 is not equal to y2
        if (y2 >= y1) :
            a = y1 - 1
        else :
            a = m - y1
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `r` is a list containing six integers [n, m, x1, y1, x2, y2], where n, m, x1, y1, x2, and y2 are the integers obtained from the input split and converted to integers, and (x2 - x1) % 2 == 0, and y1 is not equal to y2. If `y2` is greater than or equal to `y1`, then `a` is `y1 - 1`. If `y2` is less than `y1`, then `a` is `m - y1`.
        b = x2 - x1
        t = abs(y2 - y1)
        x1 += a
        x2 -= a
        if (x2 <= x1 or x1 < 1 or x2 > n) :
            print('draw')
            #This is printed: draw
            return
            #The program returns None
        #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `r` is a list containing six integers [n, m, x1 + a, y1, x2 - a, y2], `b` is the difference between `x2 - a` and `x1`, `t` is the absolute difference between `y2` and `y1`. `x2` is greater than or equal to `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`
        if (y1 <= y2) :
            y1 = 1
            y2 -= a
            c = y2 - 1
        else :
            y1 = m
            y2 += a
            c = m - y2
        #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `r` is a list containing six integers [n, m, x1 + a, y1, x2 - a, y2]. Depending on whether `y1` is less than or equal to `y2`, `y2` is adjusted as follows: if `y1` <= `y2`, then `y2` is set to `y2 - a`; otherwise, `y2` is set to `y2 + a`. `b` is the difference between `x2 - a` and `x1`, `t` is the absolute difference between `y2` and `y1`, `x2` is greater than or equal to `x1`, `x1` is greater than or equal to 1, and `x2` is less than or equal to `n`.
        if (b // 2 > a and abs(x2 - c) >= x1 + c and 1 <= y1 <= m and 1 <= x1 <= n) :
            print('bob')
            #This is printed: bob
            return
            #The program does not return any value since there is no return statement in the given code snippet.
        else :
            print('draw')
            #This is printed: 'draw'
            return
            #The program returns None
#Overall this is what the function does:The function processes input coordinates (x1, y1) and (x2, y2) to determine if player Alice or Bob wins based on certain conditions. The function reads six integers from input representing the number of test cases, grid dimensions (n, m), and coordinates of two points. It then checks several conditions involving the coordinates and prints either "Alice", "Bob", or "draw" based on these conditions. If the conditions are met, it may adjust the coordinates and return a modified list of coordinates or the absolute difference between y-coordinates. Otherwise, it returns None.

