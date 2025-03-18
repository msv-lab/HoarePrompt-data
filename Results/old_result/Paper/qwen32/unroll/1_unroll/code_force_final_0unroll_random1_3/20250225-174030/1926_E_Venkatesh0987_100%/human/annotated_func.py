#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: The output is a series of integers, each corresponding to the result of the computation for each test case. The exact values depend on the input values of `n` and `k` for each test case.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers `n` and `k`. For each test case, it calculates and prints an integer value based on the relationship between `n` and `k`. Specifically, if `k` is greater than half of `n` plus one, it performs a series of calculations involving halving and powers of two to determine the output. Otherwise, it directly computes `2 * k - 1`. The output is a series of integers, each corresponding to a test case.

