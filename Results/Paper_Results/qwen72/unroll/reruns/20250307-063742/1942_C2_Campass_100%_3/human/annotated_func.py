#State of the program right berfore the function call: The function `func` is incomplete and lacks parameters. Based on the problem description, the function should accept parameters `n`, `x`, `y`, and a list of `x` distinct integers representing the vertices Bessie has chosen. The parameters should satisfy the conditions: `4 <= n <= 10^9`, `2 <= x <= min(n, 2 * 10^5)`, `0 <= y <= n - x`, and the list of chosen vertices should contain distinct integers from 1 to n.
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
        
    #State: The loop will print a series of integers, each representing the value of `cons` for each iteration of the loop. The value of `t` will be 0 after all iterations. The values of `n`, `x`, `y`, `l`, `val`, and `sx` will be different for each iteration, but their final values will depend on the last iteration of the loop.
#Overall this is what the function does:The function `func` reads input values and processes them to calculate and print a series of integers. Each integer represents the value of `cons` for a given set of parameters `n`, `x`, `y`, and a list of `x` distinct integers. The function does not return any value. After processing all input sets, the function will have printed `t` integers, where `t` is the number of test cases provided in the initial input. The final state of the program includes `t` being reduced to 0, and the values of `n`, `x`, `y`, `l`, `val`, and `sx` being the last computed values for the final test case.

