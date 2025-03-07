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
        
    #State: The loop has finished executing all `t` iterations. For each iteration, the loop reads `n` and `k` from input, processes them, and prints the calculated value based on the conditions provided. The variables `t`, `n`, and `k` are not modified and retain their initial values for each test case. The list `L` and variables `tot` and `pow` are reset for each iteration.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where 1 ≤ k ≤ n ≤ 10^9. It processes these values and prints a calculated result for each test case. The function does not return any value; it only prints the results to the console. After the function concludes, the input variables `t`, `n`, and `k` are not modified and retain their initial values for each test case. The list `L` and variables `tot` and `pow` are reset for each iteration.

