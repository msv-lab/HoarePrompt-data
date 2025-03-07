#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 1 <= k <= m <= n <= 2 * 10^5. a is a list of n integers where each integer is between 1 and 10^6, inclusive. b is a list of m integers where each integer is between 1 and 10^6, inclusive. The sum of n over all test cases does not exceed 2 * 10^5. The sum of m over all test cases does not exceed 2 * 10^5.
def func_1(n, m, k, a, b):
    cb = Counter(sorted(b))
    ca = Counter(sorted(a[:m]))
    ans = 0
    sm = sum((ca & cb).values())
    if (sm >= k) :
        ans += 1
    #State: `t` is an integer such that 1 <= t <= 10^4; `n`, `m`, `k` are integers such that 1 <= k <= m <= n <= 2 * 10^5; `a` is a list of `n` integers where each integer is between 1 and 10^6, inclusive; `b` is a list of `m` integers where each integer is between 1 and 10^6, inclusive; `cb` is a Counter object representing the counts of each integer in the sorted list `b`; `ca` is a Counter object representing the counts of each integer in the sorted list of the first `m` elements of `a`; `sm` is the sum of the minimum counts of each integer that appears in both `ca` and `cb`. If `sm` is greater than or equal to `k`, `ans` is set to 1. Otherwise, `ans` remains 0.
    for r in range(m, n):
        if ca[a[r]] < cb[a[r]]:
            sm += 1
        
        ca[a[r]] += 1
        
        if ca[a[r - m]] <= cb[a[r - m]]:
            sm -= 1
        
        ca[a[r - m]] -= 1
        
        if sm >= k:
            ans += 1
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n`, `m`, `k` are integers such that 1 <= k <= m <= n <= 2 * 10^5; `a` is a list of `n` integers where each integer is between 1 and 10^6, inclusive; `b` is a list of `m` integers where each integer is between 1 and 10^6, inclusive; `cb` is a Counter object representing the counts of each integer in the sorted list `b`; `ca` is a Counter object representing the counts of each integer in the last `m` elements of `a`; `sm` is the sum of the minimum counts of each integer that appears in both `ca` and `cb`; `ans` is the total number of times during the sliding window process that `sm` was at least `k`.
    return ans
    #The program returns the total number of times during the sliding window process that `sm` was at least `k`.
#Overall this is what the function does:The function `func_1` takes four parameters: `n` (length of list `a`), `m` (length of list `b`), `k` (an integer), `a` (a list of `n` integers), and `b` (a list of `m` integers). It returns the total number of times, during a sliding window process of size `m` over list `a`, that the sum of the minimum counts of common elements between the current window and list `b` is at least `k`.

