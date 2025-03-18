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
        
    #State: The loop finishes executing for all `t` test cases. For each test case, the list `L` is populated with values calculated from `n` and `k`, and the appropriate value based on the conditions is printed. The variables `n` and `k` are reset for each test case, and `t` is decremented to 0. The final state of `t` is 0, and `L`, `tot`, and `pow` are reset to their initial states for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where 1 ≤ k ≤ n ≤ 10^9. The function then calculates a sequence of values based on `n` and `k`, and prints a specific value derived from these calculations for each test case. After processing all test cases, the function terminates, and the final state of the program is that all test cases have been processed and the appropriate values have been printed.

