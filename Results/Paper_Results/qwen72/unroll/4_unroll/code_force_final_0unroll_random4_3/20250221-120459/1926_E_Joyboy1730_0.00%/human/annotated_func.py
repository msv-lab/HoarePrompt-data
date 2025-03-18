#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: The loop reads `t` pairs of integers `(n, k)` from the input, and for each pair, it prints a value calculated based on the given logic. After all iterations, the variables `t`, `n`, and `k` are unchanged, but the internal variables `L`, `tot`, `pow`, and `a` are reset or modified within each iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each of the `t` test cases, it reads a pair of integers `n` and `k` from the input. The function then performs a series of calculations and prints a value for each test case based on the logic defined within the loop. The function does not return any value. After the function concludes, the variables `t`, `n`, and `k` are unchanged, but the internal variables `L`, `tot`, `pow`, and `a` are reset or modified within each iteration of the loop.

