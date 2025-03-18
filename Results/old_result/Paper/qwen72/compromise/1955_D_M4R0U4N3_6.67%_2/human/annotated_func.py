#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5, representing the lengths of arrays a and b and the required number of matching elements. a is a list of n integers where 1 ≤ a_i ≤ 10^6, and b is a list of m integers where 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has completed all iterations. `r` is `n`, `m` is less than `n`, `old` is `a[n - m - 1]`, `a` remains unchanged, `todo` contains elements from `a` that were not processed by the loop, `done` contains elements from `a` that were in `todo` and have been processed by the loop, `extra` contains elements from `a` that were not in `todo` and have been processed by the loop, and `ans` is the total number of times the length of `done` was greater than or equal to `k` during the loop execution.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, and lists `a` and `b`. For each test case, it checks how many contiguous subarrays of length `m` in `a` contain at least `k` elements that are also in `b`. The function prints the count of such subarrays for each test case. The function does not return any value. After the function concludes, the input lists `a` and `b` remain unchanged, and the internal sets `todo`, `done`, and `extra` are no longer relevant.

