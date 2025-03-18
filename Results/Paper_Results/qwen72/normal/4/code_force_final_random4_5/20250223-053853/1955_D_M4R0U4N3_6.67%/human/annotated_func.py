#State of the program right berfore the function call: The function should take three parameters: a list of integers `a` of length `n`, a list of integers `b` of length `m`, and an integer `k`. The conditions are 1 <= k <= m <= n <= 2 * 10^5, and the elements of `a` and `b` are integers in the range 1 to 10^6. The function should be called within a loop that processes `t` test cases, where 1 <= t <= 10^4.
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
        
    #State: The loop processes `t` test cases, and for each test case, it prints the number of valid subarrays of length `m` in the list `a` that contain at least `k` elements from the set `todo`. After all iterations, the variables `n`, `m`, `k`, and `a` retain their initial values for each test case, while the sets `todo`, `done`, and `extra` are reset for each new test case. The variable `ans` is reset to 0 at the start of each test case and is used to accumulate the count of valid subarrays, which is printed at the end of each test case.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it takes a list of integers `a` of length `n`, a list of integers `b` of length `m`, and an integer `k`. It then counts the number of subarrays of length `m` in `a` that contain at least `k` elements from the set `b`. After processing each test case, it prints the count of such valid subarrays. The function does not return any value; it only prints the result for each test case. The input variables `n`, `m`, `k`, and `a` retain their initial values for each test case, while the sets `todo`, `done`, and `extra` are reset for each new test case.

