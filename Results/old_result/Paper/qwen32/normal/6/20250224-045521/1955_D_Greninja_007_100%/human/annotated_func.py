#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case: n, m, and k are integers such that 1 <= k <= m <= n <= 2 * 10^5. a is a list of n integers where each integer is in the range 1 <= a_i <= 10^6. b is a list of m integers where each integer is in the range 1 <= b_i <= 10^6. The sum of n over all test cases does not exceed 2 * 10^5. The sum of m over all test cases does not exceed 2 * 10^5.
def func_1(n, m, k, a, b):
    cb = Counter(sorted(b))
    ca = Counter(sorted(a[:m]))
    ans = 0
    sm = sum((ca & cb).values())
    if (sm >= k) :
        ans += 1
    #State: `t` is an integer such that 1 <= t <= 10^4; `n`, `m`, and `k` are integers such that 1 <= k <= m <= n <= 2 * 10^5; `a` is a list of `n` integers where each integer is in the range 1 <= a_i <= 10^6; `b` is a sorted list of `m` integers where each integer is in the range 1 <= b_i <= 10^6; `cb` is a Counter object representing the frequency of each element in the sorted list `b`; `ca` is a Counter object representing the frequency of each element in the sorted sublist `a[:m]`. If `sm` is greater than or equal to `k`, then `ans` is the sum of the minimum frequency values of common elements between `ca` and `cb` plus 1. Otherwise, `ans` remains the sum of the minimum frequency values of common elements between `ca` and `cb`.
    for r in range(m, n):
        if ca[a[r]] < cb[a[r]]:
            sm += 1
        
        ca[a[r]] += 1
        
        if ca[a[r - m]] <= cb[a[r - m]]:
            sm -= 1
        
        ca[a[r - m]] -= 1
        
        if sm >= k:
            ans += 1
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n`, `m`, and `k` are integers such that 1 <= k <= m <= n <= 2 * 10^5; `a` is a list of `n` integers where each integer is in the range 1 <= a_i <= 10^6; `b` is a sorted list of `m` integers where each integer is in the range 1 <= b_i <= 10^6; `cb` is a Counter object representing the frequency of each element in the sorted list `b`; `ca` is a Counter object representing the frequency of each element in the sorted sublist `a[n-m:n]`; `ans` is the number of windows of `m` consecutive elements in `a` where the count of elements in `ca` that have a frequency less than or equal to their frequency in `cb` is greater than or equal to `k`.
    return ans
    #The program returns `ans`, which is the number of windows of `m` consecutive elements in `a` where the count of elements in `ca` that have a frequency less than or equal to their frequency in `cb` is greater than or equal to `k`.
#Overall this is what the function does:The function calculates the number of windows of `m` consecutive elements in the list `a` where at least `k` elements have frequencies in the window that are less than or equal to their frequencies in the list `b`.

