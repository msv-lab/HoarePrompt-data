#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x; the sum of x over all test cases does not exceed 2⋅10^5; the first line of each test case contains three integers n, x, and y; the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: Output State: The output state will be the value printed by the loop after all iterations are completed.
    #
    #To understand this output state, let's break down the loop:
    #
    #1. **Initialization**: `t` is set to the first integer returned by the lambda function `R()`. This initializes the loop condition.
    #
    #2. **Loop Execution**:
    #   - `t` is decremented by 1 in each iteration.
    #   - New values `n`, `x`, and `y` are assigned from `R()`.
    #   - A variable `sx` is initialized to 0.
    #   - A list `l` is populated with elements from `R()`, sorted, and modified by appending `n + l[0]`.
    #   - A list `val` is created where each element represents the difference between consecutive elements in `l` minus 1.
    #   - `val` is sorted based on specific criteria.
    #   - For each element in `val`, a calculation is performed to update `sx` based on conditions involving `y`.
    #   - `cons` is calculated as `x + sx - 2` and clamped to be at most `n - 2`.
    #
    #3. **Final Output**: The value of `cons` is printed after the loop completes.
    #
    #Since the exact values of `R()` and the initial state of `t` are not specified, the final output state will depend on these values. However, the general process described above will determine the value of `cons` which is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, x, and y, followed by x distinct integers from 1 to n. It calculates and prints a value (`cons`) for each test case based on the given inputs. The value `cons` is derived through a series of operations including sorting, calculating differences, and applying conditional updates. The final output for each test case is the computed value of `cons`, which is constrained to be at most `n - 2`.

