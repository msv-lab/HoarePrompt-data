#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, n and k are integers for each test case such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: The loop executes `t` times, and for each iteration, it reads a pair of integers `n` and `k` from the input. It then calculates and prints a value based on the values of `n` and `k`. After all iterations, the variables `t`, `n`, and `k` remain unchanged, but the list `L` and the variables `tot` and `pow` are reset to their initial states (empty list, 0, and 1 respectively) for each iteration.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case is defined by two integers `n` and `k` (where 1 ≤ k ≤ n ≤ 10^9). For each test case, the function calculates a specific value based on `n` and `k` and prints it. The function reads the number of test cases `t` (where 1 ≤ t ≤ 5 · 10^4) from the input and processes each test case in a loop. After processing all test cases, the function does not return any value, but it prints the calculated values for each test case. The state of the program after the function concludes is that all input values have been processed, and the results have been printed to the console.

