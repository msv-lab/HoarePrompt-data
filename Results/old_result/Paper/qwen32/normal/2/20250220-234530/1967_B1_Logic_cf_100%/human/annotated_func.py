#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n and m are positive integers such that 1 <= n, m <= 2 * 10^6. The sum of all n and the sum of all m across all test cases do not exceed 2 * 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: The loop has executed `t` times, where `t` is the initial input integer. For each iteration, `n` and `m` are read as integers from the input, and `ans` is calculated as `n + Σ((n + b) // (b * b))` for `b` ranging from 2 to `min(n, m)`. After each iteration, the result `ans` is printed.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two positive integers `n` and `m`. For each test case, it calculates a value `ans` based on the formula `n + Σ((n + b) // (b * b))` for `b` ranging from 2 to `min(n, m)`, and then prints the result.

