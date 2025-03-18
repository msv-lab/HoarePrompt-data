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
        
    #State: `t` is 0, `n`, `x`, `y`, and `R` remain unchanged from their last iteration values, `l` is a sorted list of `x` distinct integers from 1 to `n` with an additional element `n + l[0]` appended to it, `val` is a list of `x` elements sorted first by evenness and then by value, `sx` is the sum of all elements in `val`, `y` is the initial `y` minus the sum of `i // 2` for all elements `i` in `val`, `cons` is `x + sx - 2`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `x`, `y`, and a list of `x` distinct integers. For each test case, it calculates and prints a value `cons` which is derived from the input values and represents the number of connections needed based on specific rules.

