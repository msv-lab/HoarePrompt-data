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
        
    #State: The loop will print a number for each test case, and after all iterations, the variables `t`, `n`, and `k` will be unchanged, but the loop will have processed all the test cases. The list `L` will be empty, `tot` will be 0, and `pow` will be 1 for each iteration.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k` where 1 ≤ k ≤ n ≤ 10^9. For each test case, it calculates and prints a specific number based on the values of `n` and `k`. The function does not return any value, but it prints a result for each test case. After processing all test cases, the function concludes without modifying the input variables `t`, `n`, and `k`. The list `L` remains empty, and the variables `tot` and `pow` are reset to 0 and 1, respectively, for each test case.

