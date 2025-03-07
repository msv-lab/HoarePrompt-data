#State of the program right berfore the function call: Each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 2 · 10^6. The input starts with an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. The sum of n and the sum of m over all test cases do not exceed 2 · 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: For each test case, the output is the final value of `ans` after the loop has computed the sum of `n` and the integer divisions `(n + b) // (b * b)` for all `b` from 2 to `min(n, m)`. The variable `t` remains unchanged, and each test case's `n` and `m` are processed independently to produce a separate output value.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers `n` and `m`. For each test case, it calculates a result based on `n` and the integer divisions `(n + b) // (b * b)` for all `b` from 2 to `min(n, m)`, and prints this result. The number of test cases is specified by the input integer `t`.

