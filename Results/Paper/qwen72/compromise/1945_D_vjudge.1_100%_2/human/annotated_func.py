#State of the program right berfore the function call: n and k are integers such that 1 <= k <= n <= 200,000, a and b are lists of integers of length n, where 1 <= a_i, b_i <= 10^9.
def func_1(n, k, a, b):
    c = [min(a[i], b[i]) for i in range(n)]
    suff = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suff[i] = suff[i + 1] + c[i]
        
    #State: `suff` is a list of integers of length `n + 1` where `suff[i]` is the sum of all elements in `c` from index `i` to `n-1`, and `suff[n]` is 0.
    ans = float('inf')
    for i in range(k):
        ans = min(ans, a[i] + suff[i + 1])
        
    #State: `ans` is the minimum value of `a[i] + suff[i + 1]` for all `i` in the range from 0 to `k-1`. The list `suff` remains unchanged.
    print(ans)
    #This is printed: ans (where ans is the minimum value of `a[i] + suff[i + 1]` for all `i` in the range from 0 to `k-1`)
#Overall this is what the function does:The function `func_1` accepts four parameters: `n`, `k`, `a`, and `b`. `n` and `k` are integers with 1 <= k <= n <= 200,000, and `a` and `b` are lists of integers of length `n` with each element between 1 and 10^9. The function computes and prints the minimum value of `a[i] + suff[i + 1]` for all `i` in the range from 0 to `k-1`, where `suff` is a list of integers of length `n + 1` representing the suffix sums of the list `c`, which contains the minimum values of corresponding elements in `a` and `b`. The function does not return any value.

