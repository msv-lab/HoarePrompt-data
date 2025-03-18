#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, x, and y are integers such that 4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), and 0 <= y <= n - x. The list of x integers contains distinct values from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: The loop prints the value of `cons` for each test case, which is the minimum number of connected components that can be formed in a cycle graph with `n` vertices, given the constraints of `x` chosen vertices and `y` additional edges.
#Overall this is what the function does:The function `func` reads multiple test cases from the input. For each test case, it takes the number of vertices `n`, the number of chosen vertices `x`, and the number of additional edges `y`. It processes these inputs to determine the minimum number of connected components that can be formed in a cycle graph with `n` vertices, considering the constraints of `x` chosen vertices and `y` additional edges. The function prints the result for each test case, which is the minimum number of connected components. The function does not return any value.

