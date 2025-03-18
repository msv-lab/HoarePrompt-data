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
        
    #State: After all iterations, `s` will be the cumulative sum of `x` for each iteration until the condition `s >= k` or `k > s + x` is met, `n` will be 0, `m` will be \(2^t\) (where \(t\) is the total number of iterations), and `x` will be 1 since `n` becomes 0.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of integers t, n, and k. It calculates and prints a result based on the given conditions. Specifically, for each test case, it computes a value derived from n, k, and t, ensuring that 1 ≤ t ≤ 5 ⋅ 10^4 and 1 ≤ k ≤ n ≤ 10^9. After processing all test cases, it outputs the calculated result for each case.

