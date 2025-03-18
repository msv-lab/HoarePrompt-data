#State of the program right berfore the function call: n and k are integers such that 1 <= k <= n <= 200,000, a and b are lists of integers of length n, and for each element in a and b, 1 <= a_i, b_i <= 10^9.
def func_1(n, k, a, b):
    c = [min(a[i], b[i]) for i in range(n)]
    suff = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suff[i] = suff[i + 1] + c[i]
        
    #State: `n` and `k` remain unchanged. `a` and `b` remain unchanged. `c` remains a list of length `n` where each element `c[i]` is the minimum of `a[i]` and `b[i]`. `suff` is a list of length `n + 1` where `suff[i]` is the sum of all elements in `c` from index `i` to `n-1`, and `suff[n]` is 0.
    ans = float('inf')
    for i in range(k):
        ans = min(ans, a[i] + suff[i + 1])
        
    #State: Output State: `n` and `k` remain unchanged. `a` and `b` remain unchanged. `c` remains a list of length `n` where each element `c[i]` is the minimum of `a[i]` and `b[i]`. `suff` remains a list of length `n + 1` where `suff[i]` is the sum of all elements in `c` from index `i` to `n-1`, and `suff[n]` is 0. `ans` is now set to the minimum value of `a[i] + suff[i + 1]` for all `i` in the range from 0 to `k-1`.
    print(ans)
    #This is printed: ans (where ans is the minimum value of `a[i] + suff[i + 1]` for all `i` in the range from 0 to `k-1`)
#Overall this is what the function does:The function `func_1` accepts four parameters: `n`, `k`, `a`, and `b`. `n` and `k` are integers where 1 <= k <= n <= 200,000, and `a` and `b` are lists of integers of length `n` with each element between 1 and 10^9. The function computes the minimum value of the sum of the first `k` elements of `a` and the suffix sums of the minimum values between corresponding elements of `a` and `b`. It prints this minimum value, which represents the smallest possible sum of `a[i]` and the sum of the minimum values from `a[i+1]` to `a[n-1]` for all `i` in the range from 0 to `k-1`. The function does not return any value.

