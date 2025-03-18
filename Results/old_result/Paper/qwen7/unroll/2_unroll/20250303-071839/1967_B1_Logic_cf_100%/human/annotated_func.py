#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: Output State: The value of `t`, followed by `t` lines, each containing the result of the computation for each input pair `[n, m]`. For each pair, the result is calculated by initializing `ans` to `n`, then adding `(n + b) // (b * b)` for each `b` from 2 to the minimum of `n` and `m`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( t \), \( n \), and \( m \). For each test case, it calculates a value based on \( n \) and \( m \) using a specific formula: starting with \( ans = n \), it adds \( (n + b) // (b * b) \) for each \( b \) from 2 up to the minimum of \( n \) and \( m \). The function then prints the result for each test case, outputting \( t \) lines of results.

