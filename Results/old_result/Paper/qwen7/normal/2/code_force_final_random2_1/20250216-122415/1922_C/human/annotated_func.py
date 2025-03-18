#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, a is a list of n non-negative integers in strictly increasing order (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9), m is an integer such that 1 ≤ m ≤ 10^5, and each query consists of two distinct integers x_i and y_i such that 1 ≤ x_i, y_i ≤ n.
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
        
    #State: Output State: `u` is `False`, `c` is the first return value from function `r()`, `d` is the second return value from function `r()`.
    #
    #Explanation: After the loop executes all its iterations, the variable `u` will be `False` because it is decremented by 1 each time the loop runs, and it starts as the number of iterations required to reach the final state. The values of `c` and `d` will hold the return values of the last call to function `r()` within the loop, as the loop terminates when `u` becomes `False`. The other variables such as `t`, `a`, and `b` will remain in their final states after the loop completes, but since no specific changes to these variables are mentioned in the loop body, they will retain their values from the last iteration or initialization.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer n, a strictly increasing list a of n non-negative integers, and an integer m representing the number of queries. It then handles m queries, where each query consists of two distinct integers x and y. Based on these inputs, the function calculates and prints the result for each query according to specific conditions. After processing all queries for a test case, the function moves on to the next test case until all test cases are processed.

