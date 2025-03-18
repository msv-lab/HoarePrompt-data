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
            if c == 1:
                sx += 1
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
        
        cons = min(n - 2, cons)
        
        print(cons)
        
    #State: Output State: The output state will be the value of `cons` printed after all iterations of the loop have finished.
    #
    #To understand this output state, let's break down what happens in each iteration of the loop:
    #
    #1. **Initialization**: `t` is a tuple of integers. The loop continues as long as `t` is non-empty.
    #2. **Decrement and Input**: `t` is decremented by 1, and then three values `n`, `x`, and `y` are read from some function `R()`.
    #3. **List Manipulation**: A list `l` is created from another function `R()` and sorted. The list is then modified by appending `n + l[0]`.
    #4. **Value Calculation**: A list `val` is created where each element represents the difference between consecutive elements in `l` minus one. This list is then sorted based on specific criteria.
    #5. **Summation**: For each element in `val`, a value `c` is calculated. Depending on the value of `y`, `sx` (a cumulative sum) is updated.
    #6. **Cons Calculation**: `cons` is calculated as `x + sx - 2` and is capped at `n - 2`.
    #
    #The final value of `cons` after all iterations of the loop is printed. Since the exact values of `n`, `x`, `y`, and the lists generated from `R()` are not specified, we cannot provide a numerical output state. However, the output state will always be the value of `cons` computed after all iterations of the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing integers n, x, and y, followed by x distinct integers from 1 to n. It calculates a value `cons` based on the given conditions for each test case and prints the final value of `cons` for each test case. The value of `cons` is determined through a series of operations including sorting, calculating differences, and updating a cumulative sum.

