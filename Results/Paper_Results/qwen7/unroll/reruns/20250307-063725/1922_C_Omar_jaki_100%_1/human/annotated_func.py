#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 10^5, a is a list of n integers in strictly increasing order (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9), m is an integer such that 1 ≤ m ≤ 10^5, and for each query, x_i and y_i are integers such that 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i.
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
        
    #State: Output State: The output state will be a series of differences calculated based on the values of `b` array after processing each query.
    #
    #Explanation: Given the complexity of the code, it's important to break down what happens inside the loop:
    #
    #1. **Initialization and Input**: 
    #   - `t` is decremented and `r()` is called, which presumably provides some input.
    #   - `a` is initialized with very large negative and positive values, followed by a call to `r()` which presumably fills the rest of the list with `n` integers in strictly increasing order.
    #   - `b` is initialized as `[0, 0]`.
    #   - For each set of four consecutive elements `(w, x, y, z)` in `a`, the difference `v = y - x` is calculated, and then two new values are appended to `b` based on conditions involving `v`.
    #
    #2. **Query Processing**:
    #   - `u` is decremented and `r()` is called, which presumably provides the number of queries.
    #   - For each query, two indices `c` and `d` are read.
    #   - If `c < d`, the difference between the values at indices `(d-1)*2` and `(c-1)*2` in `b` is printed.
    #   - Otherwise, the difference between the values at indices `c*2-1` and `d*2-1` in `b` is printed.
    #
    #Since the exact values of `a` and the results of `r()` calls are not provided, we cannot determine the exact values of `b`. However, the final state of `b` will depend on the operations performed during each iteration of the loop, which involve calculating differences and appending them to `b`.
    #
    #The output state will be a series of these differences, printed out according to the conditions specified in the inner while loop.
#Overall this is what the function does:The function processes a series of test cases. Each test case includes an integer `t`, an integer `n`, a list `a` of `n` integers in strictly increasing order, and multiple queries defined by pairs of integers `(x_i, y_i)`. For each query, it calculates and prints the difference between specific elements in an auxiliary array `b`, which is constructed based on the differences between consecutive elements in `a`. The final output consists of a series of these differences, printed according to the conditions specified in the queries.

