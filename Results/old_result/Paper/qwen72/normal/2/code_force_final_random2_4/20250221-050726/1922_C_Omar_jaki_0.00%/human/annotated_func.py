#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n is an integer where 2 ≤ n ≤ 10^5, a is a list of n integers where 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9, m is an integer where 1 ≤ m ≤ 10^5, and queries is a list of m pairs (x_i, y_i) where 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i. Additionally, in every test case, for each city, the closest city is determined uniquely, and the sum of n and m over all test cases does not exceed 10^5.
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
        
    #State: After all iterations, `t` is 0 (falsy value), `n` remains an integer where 4 ≤ n ≤ 10^5, `a` is a list of n integers where 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9, `m` remains an integer where 1 ≤ m ≤ 10^5, `queries` is a list of m pairs (x_i, y_i) where 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i, `b` is a list with the last 2 * (len(a) - 3) * t elements being the cumulative sums of the differences between consecutive elements in `a` that satisfy certain conditions, `u` is 0 (falsy value), `c` and `d` are the final values returned by `r()` during the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each involving a list of city positions and a series of queries. It calculates and prints the cumulative sums of differences between city positions based on specific conditions. For each query, it prints the difference in these cumulative sums between two specified city indices. After processing all test cases, the function leaves the input variables `t`, `u`, `c`, and `d` as 0 (falsy values), and `b` as a list containing the cumulative sums of the differences. The original lists `a` and `queries` remain unchanged.

