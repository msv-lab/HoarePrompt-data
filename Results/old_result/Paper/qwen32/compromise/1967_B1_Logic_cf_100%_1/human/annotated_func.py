#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 · 10^6. The sum of n and the sum of m over all test cases do not exceed 2 · 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: `t` is an input integer such that 1 ≤ `t` ≤ 10^4, `n` and `m` are integers, `ans` is `n + sum((n + b) // (b * b) for b in range(2, min(n, m) + 1))` for each pair of `n` and `m` provided, `T` has completed all iterations up to `t`.
#Overall this is what the function does:The function reads a positive integer `t` representing the number of test cases. For each test case, it reads two positive integers `n` and `m`, computes a value based on these inputs using a specific formula, and prints the result. The computation involves summing a series derived from `n` and `m` for each test case.

