#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        s = 0
        
        i = 0
        
        d = n
        
        h = n
        
        p = 1
        
        g = 0
        
        if k > (n + 1) // 2:
            while s < k and d > 0:
                s += (d + 1) // 2
                d -= (d + 1) // 2
                i += 1
            while p <= i - 1:
                g += (h + 1) // 2
                h -= (h + 1) // 2
                p += 1
            f = k - g
            y = 2 ** (i - 1) * (2 * f - 1)
            print(y)
        else:
            print(2 * k - 1)
        
    #State: The output state consists of `t` lines, each containing the result of the respective test case based on the provided logic.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k`. For each test case, it calculates and prints a value based on the relationship between `n` and `k`. If `k` is greater than half of `n` plus one, it performs a series of calculations involving halving `n` and accumulating values until it reaches the desired `k`. Otherwise, it directly computes the result as `2 * k - 1`. The output is `t` lines, each corresponding to the result of a test case.

