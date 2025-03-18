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
        
    #State: Output State: `t` is `False`, `y` is `-2`, `sx` is `-10`, `cons` is `1`.
    #
    #Explanation: After the loop has executed all its iterations, the variable `t` becomes `False` because it was decremented until it reached `0`. The variable `y` is reduced by the integer division of each element in `val` by 2 for every iteration, which, based on the given information, results in `y` being `-2`. The variable `sx` accumulates the sum of all elements in `val` plus twice the minimum of `y` and `c` for each element minus `c`, leading to `sx` being `-10`. Finally, `cons` is calculated as `x + sx - 2`, which, given the previous values, results in `cons` being `1`.
#Overall this is what the function does:The function processes multiple test cases, each containing integers n, x, and y, followed by x distinct integers from 1 to n. It calculates and prints a value `cons` based on the given inputs and the sorted differences between consecutive elements in the list of x distinct integers. The final output is determined by the sum of certain elements and the value of y, adjusted according to specific conditions.

