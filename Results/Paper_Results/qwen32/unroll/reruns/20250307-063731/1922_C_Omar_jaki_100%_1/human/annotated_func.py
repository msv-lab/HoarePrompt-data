#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 10^5, a is a list of n integers such that 0 <= a_1 < a_2 < ... < a_n <= 10^9, m is an integer such that 1 <= m <= 10^5, and for each query, x_i and y_i are integers such that 1 <= x_i, y_i <= n and x_i != y_i. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. Additionally, for each city, the closest city is determined uniquely.
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
        
    #State: `t` is 0, `a` is the last processed list of city positions padded with -1000000000.0 and 2000000000.0, and `b` is the last computed list of cumulative sums. The query results are printed directly.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of city coordinates and a set of queries. For each query, it calculates and prints the cumulative distance sum to the closest city for the specified cities, ensuring that the closest city is uniquely determined.

