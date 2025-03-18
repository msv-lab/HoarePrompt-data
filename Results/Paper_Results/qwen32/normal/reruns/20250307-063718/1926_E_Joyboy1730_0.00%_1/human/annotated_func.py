#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * k - 1))
                break
            tot += a
            k -= tot
            pow *= 2
        
    #State: `t` is 0, `n` is 0, `k` is adjusted by the cumulative sum of `tot` values across all iterations, `L` remains unchanged, `tot` is the sum of processed elements in `L` across all iterations, `pow` is `2` raised to the total number of iterations.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k` where `1 ≤ k ≤ n`. For each test case, it performs a series of calculations and prints a result based on the values of `n` and `k`.

