#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and a is a list of n integers in strictly increasing order (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9). m is an integer such that 1 ≤ m ≤ 10^5, and for each query, x_i and y_i are integers such that 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i.
def func():
    r = lambda : map(int, input().split())
    t, = r()
    while t:
        t -= 1
        
        r()
        
        a = -1000000000.0, *r(), 2000000000.0
        
        b = [0, 0]
        
        for w, x, y, z in zip(a, a[1:], a[2:], a[3:]):
            v = y - x
            b += b[-2] + v ** (v > x - w), b[-1] + v ** (v > z - y)
        
        print(b, 'B')
        
        u, = r()
        
        while u:
            u -= 1
            c, d = r()
            if c < d:
                print(b[(d - 1) * 2] - b[(c - 1) * 2])
            else:
                print(b[c * 2 - 1] - b[d * 2 - 1])
        
    #State: Output State: `u` is a falsy value (0), `a` is a list with at least 7 elements, `c` and `d` are the return values from function `r()` after the loop has finished executing, `b` is a list where the last two elements are the cumulative results of the additions and comparisons performed within the loop for all iterations.
    #
    #Explanation: After the loop has completed all its iterations, the variable `u` will be a falsity value (0) because the loop condition `u` is no longer true. The list `a` will have at least 7 elements due to the updates made within the loop. The variables `c` and `d` will hold the most recent values returned by the function `r()` after the loop has finished executing. The list `b` will remain unchanged from its final state after the last iteration of the loop, with the last two elements being the cumulative results of the additions and comparisons performed during all iterations.
#Overall this is what the function does:The function processes a list of integers `a` and handles multiple queries. For each query, it calculates and prints the difference between specific elements in the list `a`. Initially, it reads the number of test cases, then for each test case, it reads the list `a`, performs some calculations, and handles the queries. Finally, it outputs the differences for each query based on the calculated values stored in the list `b`.

