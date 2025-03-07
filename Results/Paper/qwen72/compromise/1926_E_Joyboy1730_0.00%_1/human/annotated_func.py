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
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n` and `k` from input. After the loop, `t` is reduced by the number of iterations completed. The variables `n` and `k` are reset to their initial values for each iteration, and `L` is reset to an empty list for each iteration. The variable `tot` is reset to 0 for each iteration, and `pow` is reset to 1 for each iteration. The loop prints a value for each test case based on the conditions provided, but the final state of `t` is the only variable that is consistently affected by the loop, reducing it by the number of iterations.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case involves integers `n` and `k` such that 1 ≤ k ≤ n ≤ 10^9. For each test case, it calculates and prints a specific value based on the conditions provided. The function reads the number of test cases `t` from the input, and for each test case, it reads `n` and `k` from the input. After processing all test cases, the value of `t` is reduced by the number of test cases processed. The function does not return any value; it only prints the results for each test case.

