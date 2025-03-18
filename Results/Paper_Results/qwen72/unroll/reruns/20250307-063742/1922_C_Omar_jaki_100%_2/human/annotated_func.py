#State of the program right berfore the function call: t is an integer (1 ≤ t ≤ 10^4), n is an integer (2 ≤ n ≤ 10^5), a is a list of n integers (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9), m is an integer (1 ≤ m ≤ 10^5), and queries is a list of m tuples (x_i, y_i) where each x_i and y_i is an integer (1 ≤ x_i, y_i ≤ n; x_i ≠ y_i). Additionally, for each city, the closest city is determined uniquely, and the sum of n and m over all test cases does not exceed 10^5.
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
        
        u, = r()
        
        while u:
            u -= 1
            c, d = r()
            if c < d:
                print(b[(d - 1) * 2] - b[(c - 1) * 2])
            else:
                print(b[c * 2 - 1] - b[d * 2 - 1])
        
    #State: `t` is 0, `n` is unchanged, `a` is a modified list with additional boundary values, `m` is unchanged, `queries` is unchanged, and `b` is a list of calculated values.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `t`. For each test case, it reads a list of integers `a` and a series of queries. It then calculates and prints the difference in values from a list `b` for each query. The list `b` is constructed based on the differences between consecutive elements in `a`, with additional boundary values added to `a`. After processing all queries for a test case, it moves to the next test case. The function does not return any values; it only prints the results of the queries. The final state of the program is that `t` is 0, `n` and `m` are unchanged, `a` has additional boundary values, and `b` contains the calculated values for the current test case.

