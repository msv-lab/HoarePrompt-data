#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 1 <= k <= m <= n <= 2 * 10^5. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 10^6. b is a list of m integers where each element b_i satisfies 1 <= b_i <= 10^6. The sum of n over all test cases does not exceed 2 * 10^5. The sum of m over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop has executed `t` times, where `t` is the initial integer input. For each test case, the final `ans` value represents the number of times during the sliding window process that the number of elements in the `done` set was greater than or equal to `k`. The sets `todo`, `done`, and `extra` are reset at the start of each test case and are only relevant within the context of that specific test case.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it evaluates a sliding window of size `m` over a list `a` of `n` integers, checking if at least `k` elements from a given set `b` (represented by the `todo` set) are present within the window. It returns the count of how many times this condition is met as the window slides through the list `a`.

