#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5 ⋅ 10^4. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^9.
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
        
    #State: Output State: The value of `t` will be processed sequentially. For each `t`, the loop will compute a specific value based on the inputs `n` and `k`. The final output will be a series of computed values printed for each `t` from 1 to `t`. Each computed value is derived from the logic inside the loop, which essentially calculates a modified geometric progression based on the inputs `n` and `k`.
#Overall this is what the function does:The function processes a series of test cases (up to 50,000). For each test case, it reads two integers \( n \) and \( k \) where \( 1 \leq k \leq n \leq 10^9 \). It then computes a specific value based on these inputs using a loop, which involves modifying \( n \) and \( k \) according to certain conditions. Finally, it prints the computed value for each test case.

