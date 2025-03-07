#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: `t` is 0, `n` is 0, `L` is a list with elements corresponding to the number of iterations, `tot` is the sum of all elements in `L`, `pow` is 2 raised to the power of the number of iterations, and `k` is either `k - tot` if the loop did not break early, or `2 * k - 1` if the loop broke early and printed `pow * (2 * k - 1)`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `1 ≤ k ≤ n ≤ 10^9`. The function processes each test case and prints a result based on the values of `n` and `k`. Specifically, it calculates and prints a value that is `pow * (2 * k - 1)` if a certain condition is met during the processing, where `pow` is a power of 2. If the condition is not met, the function does not print anything for that test case. After processing all test cases, the function concludes with `t` being 0, `n` being 0, `L` being an empty list, `tot` being 0, and `pow` being 1.

