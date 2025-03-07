#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: `t` is 0, `n` is an integer, `m` is an integer, `ans` is the sum of `n` and the expression `(n + b) // (b * b)` for each `b` from `min(n, m) + 1` to `max(n, m)`, `b` is `max(n, m) + 1`, and `min(n, m)` is equal to `max(n, m)` if `n != m`, or `n` if `n == m`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( n \) and \( m \). For each test case, it calculates the value of \( ans \) as \( n \) plus the sum of \((n + b) // (b * b)\) for each integer \( b \) from 2 to the minimum of \( n \) and \( m \). After processing all test cases, it prints the result \( ans \) for each test case.

