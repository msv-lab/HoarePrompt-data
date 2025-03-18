#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case contains n (2 ≤ n ≤ 10^5) cities with coordinates a_1, a_2, ..., a_n (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9) in ascending order, and m (1 ≤ m ≤ 10^5) queries. Each query consists of two integers x_i and y_i (1 ≤ x_i, y_i ≤ n; x_i ≠ y_i), representing the cities between which the minimum travel cost needs to be calculated. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. For each city, the closest city is determined uniquely.
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
        
    #State: The loop completes all iterations, and the final output state is that `t` is 0, all test cases have been processed, and the results for each query in each test case have been printed.
#Overall this is what the function does:The function processes multiple test cases, each containing a list of city coordinates and a list of queries. For each test case, it calculates and prints the minimum travel cost between pairs of cities specified in the queries. The function does not return any value; instead, it prints the results directly. After processing all test cases, the function completes, and the final state is that all test cases have been processed and the results for each query have been printed.

