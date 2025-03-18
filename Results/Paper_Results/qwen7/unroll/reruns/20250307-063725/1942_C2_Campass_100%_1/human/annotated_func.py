#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x; the sum of x over all test cases does not exceed 2⋅10^5; the first line of each test case contains three integers n, x, and y; the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
def func():
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        n, x, y = R()
        
        sx = 0
        
        l = list(R())
        
        l.sort()
        
        l.append(n + l[0])
        
        val = []
        
        for i in range(1, x + 1):
            c = l[i] - l[i - 1] - 1
            val.append(c)
        
        val.sort(key=lambda x: (1 - x & 1, x))
        
        for i in val:
            c = i // 2
            if y < c:
                sx += y * 2
                break
            sx += i
            y -= c
        
        cons = x + sx - 2
        
        print(cons)
        
    #State: Output State: The output state will be the value of `cons` printed after all iterations of the loop have completed.
    #
    #To understand this output state, let's break down what happens inside the loop:
    #
    #1. `t` starts as the first integer returned by `R()`.
    #2. The loop continues as long as `t` is non-zero.
    #3. For each iteration:
    #   - `t` is decremented by 1.
    #   - `n`, `x`, and `y` are assigned values from `R()`.
    #   - A list `l` is created from `R()`, sorted, and modified by appending `n + l[0]`.
    #   - A list `val` is constructed based on differences between consecutive elements in `l`.
    #   - `val` is sorted based on specific criteria.
    #   - A variable `sx` accumulates values from `val` under certain conditions.
    #   - `cons` is updated based on `x`, `sx`, and subtracting 2.
    #
    #The final value of `cons` after all iterations of the loop is printed, representing the output state of the program.
#Overall this is what the function does:The function processes input data for multiple test cases. For each test case, it reads three integers \( n \), \( x \), and \( y \), followed by \( x \) distinct integers from 1 to \( n \). It then calculates and prints a value based on these inputs, specifically \( \text{cons} = x + \text{sx} - 2 \), where \( \text{sx} \) is derived from the differences between consecutive elements in the sorted list of input integers.

