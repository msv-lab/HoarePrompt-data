#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        s = 0
        
        m = 1
        
        while n:
            x = (n + 1) // 2
            n //= 2
            if s < k and k <= s + x:
                break
            s += x
            m *= 2
        
        print((2 * (k - s) - 1) * m)
        
    #State: All test cases have been processed and their respective outputs have been printed. The variables `n`, `k`, `s`, and `m` are in their initial state for the next iteration (if there were more test cases, but there aren't).
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers `n` and `k` (where `1 ≤ k ≤ n`). For each test case, it calculates and prints a specific integer value based on the relationship between `n` and `k`. After processing all test cases, the function concludes without altering any global state or input values.

