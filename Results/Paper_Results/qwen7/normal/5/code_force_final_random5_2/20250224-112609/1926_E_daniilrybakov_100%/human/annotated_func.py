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
        
    #State: Output State: `t` is an integer such that \(1 \leq t \leq 5 \times 10^4\), `n` is now `n // 2` raised to the power of the total number of iterations the loop executed, `k` is an input integer, `m` is \(2\) raised to the power of the total number of iterations the loop executed, `x` is \((n + 1) // 2\) for the final iteration, and `s` is the sum of `x` values from each iteration.
    #
    #In simpler terms, after the loop has executed all its iterations, `t` remains within the range of 1 to 50,000, `n` is reduced to `n` // \(2^t\)` (where \(t\) is the total number of iterations), `k` remains as the input integer, `m` is \(2^t\) (as `m` doubles every iteration), `x` is calculated as \((n + 1) // 2\) for the last iteration, and `s` is the cumulative sum of `x` values from each iteration.
#Overall this is what the function does:The function processes multiple test cases, each containing integers t, n, and k. For each test case, it calculates and prints a value based on the given n and k, where n is repeatedly halved and k is compared against a cumulative sum. The final output is derived from the difference between k and the cumulative sum, scaled by a factor related to the number of halving operations performed.

