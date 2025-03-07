#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4. For each test case, n and k are integers such that 1 <= k <= n <= 10^9.
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
        
    #State: `n` is 0; `k` remains the same as the initial input integer; `s` is the sum of `(n + 1) // 2` for each iteration; `m` is `2^i` where `i` is the number of iterations; the value printed is `(2 * (k - s) - 1) * m`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k` (where `1 <= k <= n <= 10^9`). For each test case, it calculates and prints a specific integer value based on the relationship between `n` and `k`.

