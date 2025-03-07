#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n, m, and k are integers where 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5, a is a list of n integers where 1 ≤ a_i ≤ 10^6, and b is a list of m integers where 1 ≤ b_i ≤ 10^6.
def func():
    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        todo = set(map(int, input().split()))
        
        done = set()
        
        extra = set()
        
        for j in range(m):
            if a[j] in todo:
                todo.remove(a[j])
                done.add(a[j])
            else:
                extra.add(a[j])
        
        ans = 1 if len(done) >= k else 0
        
        for r in range(m, n):
            old = a[r - m]
            if old in extra:
                extra.remove(old)
            elif old in done:
                done.remove(old)
                todo.add(old)
            if a[r] in todo:
                todo.remove(a[r])
                done.add(a[r])
            else:
                extra.add(a[r])
            if len(done) >= k:
                ans += 1
        
        print(ans)
        
    #State: The loop has completed all iterations, and the following conditions hold:
#Overall this is what the function does:The function processes a series of test cases, each defined by integers `n`, `m`, `k`, a list `a` of `n` integers, and a list `b` of `m` integers. For each test case, it determines the number of contiguous subarrays of length `m` in `a` that contain at least `k` elements from `b`. The function prints the count of such subarrays for each test case. The final state of the program is that all test cases have been processed, and the counts have been printed.

