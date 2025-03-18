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
        
    #State: The loop executes `t` times, and for each iteration, it reads `n` and `k` from the input, processes them, and prints a value if the condition is met. After all iterations, `t` remains unchanged, and `n` and `k` are not defined (as they are re-assigned in each iteration). The list `L` is empty at the end of each iteration. The variables `tot` and `pow` are reset to 0 and 1, respectively, at the start of each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 ≤ t ≤ 50,000`. It then processes `t` test cases. For each test case, it reads two integers `n` and `k` from the input, where `1 ≤ k ≤ n ≤ 1,000,000,000`. The function calculates a value based on `n` and `k` and prints it if a certain condition is met. After processing all test cases, the function does not return any value, and the input variables `n` and `k` are not defined outside the loop. The list `L` is empty at the end of each iteration, and the variables `tot` and `pow` are reset for each test case.

