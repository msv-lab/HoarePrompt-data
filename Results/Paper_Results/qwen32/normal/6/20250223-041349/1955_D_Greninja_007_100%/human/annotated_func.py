#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5. a is a list of n integers where each element satisfies 1 ≤ a_i ≤ 10^6. b is a list of m integers where each element satisfies 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of m over all test cases does not exceed 2 · 10^5.
def func_1(n, m, k, a, b):
    cb = Counter(sorted(b))
    ca = Counter(sorted(a[:m]))
    ans = 0
    sm = sum((ca & cb).values())
    if (sm >= k) :
        ans += 1
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n`, `m`, and `k` are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5; `a` is a list of `n` integers where each element satisfies 1 ≤ a_i ≤ 10^6; `b` is a list of `m` integers where each element satisfies 1 ≤ b_i ≤ 10^6; `cb` is a `Counter` object that counts the occurrences of each element in the sorted list `b`; `ca` is a `Counter` object that counts the occurrences of each element in the sorted sublist `a[:m]`; `sm` is the sum of the minimum of the counts of each element in `ca` and `cb`. If `sm` is greater than or equal to `k`, then `ans` is set to 1. Otherwise, `ans` remains 0.
    for r in range(m, n):
        if ca[a[r]] < cb[a[r]]:
            sm += 1
        
        ca[a[r]] += 1
        
        if ca[a[r - m]] <= cb[a[r - m]]:
            sm -= 1
        
        ca[a[r - m]] -= 1
        
        if sm >= k:
            ans += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n`, `m`, and `k` are integers such that 1 ≤ k ≤ m < n ≤ 2 · 10^5, `a` is a list of `n` integers where each element satisfies 1 ≤ a_i ≤ 10^6, `b` is a list of `m` integers where each element satisfies 1 ≤ b_i ≤ 10^6, `cb` is a `Counter` object that counts the occurrences of each element in the sorted list `b`, `ca` is a `Counter` object that counts the occurrences of each element in the last `m` elements of `a`, `sm` is the sum of the minimum of the counts of each element in `ca` and `cb`, and `ans` is incremented each time `sm` was greater than or equal to `k` during the loop iterations.
    return ans
    #The program returns `ans` which is incremented each time `sm` was greater than or equal to `k` during the loop iterations.
#Overall this is what the function does:The function calculates and returns the number of times a sliding window of size `m` over the list `a` has at least `k` common elements with the list `b`.

