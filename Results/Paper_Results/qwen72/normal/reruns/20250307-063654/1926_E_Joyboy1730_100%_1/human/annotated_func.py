#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
            L.append(m)
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * (k - tot) - 1))
            tot += a
            pow *= 2
        
    #State: `t` is 0, `n` is 0, `k` is an input integer, `L` is a list containing the sequence of values of `(n + 1) // 2` calculated during each iteration, `m` is the last value of `(n + 1) // 2` calculated, `tot` is the sum of all elements in `L`, `pow` is 2 raised to the power of the number of elements in `L`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where 1 ≤ k ≤ n ≤ 10^9. It then processes `n` to generate a sequence of values, and for each value in this sequence, it checks if the cumulative total `tot` plus the current value includes `k`. If so, it prints a calculated result based on the current power of 2 and the position of `k` within the current value. After processing all test cases, the function does not return any value, but it prints the results for each test case.

