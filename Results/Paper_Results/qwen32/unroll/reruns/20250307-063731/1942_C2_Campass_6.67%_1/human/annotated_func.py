#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and y is an integer such that 0 ≤ y ≤ n - x. The sum of x over all test cases does not exceed 2 · 10^5. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: The loop will execute `t` times, processing each test case independently. After all test cases are processed, the value of `t` will be 0, indicating that no more test cases remain to be processed. The variables `n`, `x`, `y`, `l`, `sx`, `val`, and `cons` will reflect the state of the last test case processed. However, since the loop processes each test case independently and the state is not carried over between test cases, the final state of these variables will be the state after processing the last test case.
    #
    #Thus, the output state after all iterations will be:
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `x`, and `y`, and a list of `x` distinct integers. For each test case, it calculates and prints a result based on these inputs, representing a computed value `cons` that is the minimum of `n - 2` and a derived value from the input list and parameters.

