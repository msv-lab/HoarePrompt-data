#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x. The sum of x over all test cases does not exceed 2⋅10^5. The first line of each test case contains three integers n, x, and y. The second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: Output State: The output state will be the sum of `x` (which is the second element of the tuple returned by `R()` in each iteration) plus `sx` (which accumulates the value based on the conditions given in the loop) minus 2, printed for each iteration.
    #
    #To break it down further:
    #- `t` starts as a positive integer between 1 and 10^4.
    #- For each iteration, `t` is decremented by 1.
    #- `n`, `x`, and `y` are assigned from the tuple returned by `R()`.
    #- A list `l` is created from another tuple returned by `R()`, sorted, and modified.
    #- A list `val` is created based on differences between elements of `l`.
    #- `val` is sorted again with a custom key.
    #- A variable `sx` accumulates values based on conditions involving `y` and elements of `val`.
    #- Finally, `cons` is calculated as `x + sx - 2` and printed.
    #
    #Since the exact values of `R()` are not specified, we can't give a numerical output state. However, the process described above will be repeated until `t` reaches 0, at which point all iterations will have completed, and the final state will be the accumulated `cons` values printed during each iteration.
#Overall this is what the function does:The function processes input data for multiple test cases. For each test case, it reads three integers \( n \), \( x \), and \( y \) along with \( x \) distinct integers from 1 to \( n \). Based on these inputs, it calculates and prints a value \( \text{cons} \) which is defined as \( x + \text{sx} - 2 \), where \( \text{sx} \) is computed based on certain conditions involving \( y \) and the differences between the read integers. This process repeats for each test case until all \( t \) test cases are processed.

