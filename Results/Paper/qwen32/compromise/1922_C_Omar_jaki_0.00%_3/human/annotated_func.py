#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, a is a list of n integers where 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9, m is an integer such that 1 ≤ m ≤ 10^5, and for each query, x_i and y_i are integers such that 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i. Additionally, for each city in each test case, the closest city is uniquely determined. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5.
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
        
    #State: - The loop will continue until `t` becomes 0.
    #   - At the end of all iterations, `t` will be 0, indicating no more test cases.
    #   - The values of `a`, `b`, `u`, `c`, and `d` will reflect the state after the last iteration.
    #
    #### Final Output State:
    #
    #- `t` will be 0 because all test cases have been processed.
    #- `a` will be the list of integers from the last test case, modified with `-1000000000.0` and `2000000000.0`.
    #- `b` will be the list computed based on the differences in `a` for the last test case.
    #- `u` will be 0 because all queries for the last test case have been processed.
    #- `c` and `d` will be the last pair of query indices processed in the last test case.
    #
    #### Conclusion:
    #
    #The final output state after all iterations of the loop have finished is:
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives a list of city positions and a series of queries. Each query asks for the index of the city closest to the midpoint between two specified cities. The function outputs the result for each query.

