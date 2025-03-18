#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5. a is a list of n integers where each integer is in the range 1 ≤ a_i ≤ 10^6. b is a list of m integers where each integer is in the range 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations, `done` contains elements from `a` that were in `todo` and processed, `todo` contains elements from `a` that were in `todo` but not processed, `extra` contains elements from `a` that were not in `todo`, and `ans` is the total count of iterations where `len(done) >= k`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it determines how many times a sliding window of size `m` over list `a` contains at least `k` elements that are also in list `b`. It prints the count of such occurrences for each test case.

