#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4; for each test case, n is an integer such that 2 <= n <= 10^5, a is a list of n integers such that 0 <= a_1 < a_2 < ... < a_n <= 10^9, m is an integer such that 1 <= m <= 10^5, and for each query, x_i and y_i are integers such that 1 <= x_i, y_i <= n and x_i != y_i; the sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5.
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
        
    #State: 
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives a list of distinct integers in increasing order and a series of queries. Each query consists of two indices, and the function outputs the absolute difference between the elements at these indices in the list.

