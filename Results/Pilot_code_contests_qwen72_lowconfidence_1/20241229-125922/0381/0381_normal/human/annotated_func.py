#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 10^5, K is an integer such that 1 ≤ K ≤ N, and a is a list of N integers where each a_i satisfies |a_i| ≤ 10^9.
def func():
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    total = [0] * (n + 1)
    asum = [0] * (n + 1)
    for i in xrange(n):
        asum[i + 1] = asum[i] + a[i]
        
        if a[i] > 0:
            total[i + 1] = total[i] + a[i]
        else:
            total[i + 1] = total[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 10^5, `k` is an integer such that 1 ≤ k ≤ n, `a` is a list of integers read from input with length `n`, `total` is a list of length `n + 1` where `total[i]` is the sum of all positive integers in `a[:i]` for 0 ≤ i ≤ n, `asum` is a list of length `n + 1` where `asum[i]` is the cumulative sum of the first `i` elements of `a` for 0 ≤ i ≤ n.
    ans = 0
    for i in xrange(n - k + 1):
        tmp = asum[i + k] - asum[i]
        
        ans = max(ans, tmp + total[i] + total[n] - total[i + k], total[i] + total[n
            ] - total[i + k])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^5\), `k` is an integer such that \(1 \leq k \leq n\), `a` is a list of integers with length `n`, `total` is a list of length `n + 1` where `total[i]` is the sum of all positive integers in `a[:i]` for \(0 \leq i \leq n\), `asum` is a list of length `n + 1` where `asum[i]` is the cumulative sum of the first `i` elements of `a` for \(0 \leq i \leq n\), `ans` is the maximum value of \(\max\left(\text{asum}[i + k] - \text{asum}[i] + \text{total}[i] + \text{total}[n] - \text{total}[i + k], \text{total}[i] + \text{total}[n] - \text{total}[i + k]\right)\) for \(0 \leq i \leq n - k\). If `n < k`, `ans` is 0.
    print(ans)
#Overall this is what the function does:The function reads two integers `N` and `K` from the input, followed by a list `a` of `N` integers. It calculates the maximum possible sum of a subarray of length `K` in `a`, while also considering the sum of positive integers outside this subarray. The function then prints this maximum sum. The function does not return any value. The final state of the program is that `N`, `K`, and `a` are unchanged, and the result of the computation is printed to the console. If `N < K`, the function will print `0`.

