#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4, and for each `i` from 1 to `t`, the following has occurred:
    #- Two integers `n` and `k` were read from input.
    #- A variable `s` was initialized to 0.
    #- A variable `m` was initialized to 1.
    #- A while loop was executed where `x` was set to `(n + 1) // 2`, `n` was halved, and if `s < k` and `k <= s + x`, the loop was exited; otherwise, `s` was incremented by `x` and `m` was doubled.
    #- The result `(2 * (k - s) - 1) * m` was printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( n \), and \( k \). For each test case, it calculates and prints a specific value based on the given \( n \) and \( k \) within certain constraints. Specifically, it computes \((2 \times (k - s) - 1) \times m\), where \( s \) and \( m \) are derived through a series of operations involving \( n \) and \( k \).

