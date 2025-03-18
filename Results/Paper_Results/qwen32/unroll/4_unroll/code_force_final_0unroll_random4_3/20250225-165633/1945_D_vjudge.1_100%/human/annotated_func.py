#State of the program right berfore the function call: n and k are integers such that 1 <= k <= n <= 200,000, a is a list of n integers where 1 <= a_i <= 10^9 for each i, and b is a list of n integers where 1 <= b_i <= 10^9 for each i. The sum of n across all test cases does not exceed 2 * 10^5.
def func_1(n, k, a, b):
    c = [min(a[i], b[i]) for i in range(n)]
    suff = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suff[i] = suff[i + 1] + c[i]
        
    #State: `n` and `k` remain unchanged, `a` remains unchanged, `b` remains unchanged, `c` remains unchanged, `suff` is a list where `suff[i]` is the sum of `c[j]` for all `j` from `i` to `n-1`.
    ans = float('inf')
    for i in range(k):
        ans = min(ans, a[i] + suff[i + 1])
        
    #State: `n` and `k` remain unchanged, `a` remains unchanged, `b` remains unchanged, `c` remains unchanged, `suff` remains unchanged, `ans` is the minimum value of `a[i] + suff[i + 1]` for `i` from `0` to `k-1`.
    print(ans)
    #This is printed: ans (where ans is the minimum value of a[i] + suff[i + 1] for i from 0 to k-1)
#Overall this is what the function does:The function `func_1` calculates and prints the minimum value of the sum of an element from the first `k` elements of list `a` and the sum of the minimum elements from the corresponding positions in lists `a` and `b` starting from the next position to the end of the list.

