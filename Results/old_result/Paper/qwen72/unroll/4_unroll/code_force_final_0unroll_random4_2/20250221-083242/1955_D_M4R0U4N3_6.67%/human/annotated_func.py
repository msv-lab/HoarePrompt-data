#State of the program right berfore the function call: The function should accept three parameters: n, m, and k (1 ≤ k ≤ m ≤ n ≤ 2 · 10^5), and two lists of integers: a (length n, 1 ≤ a_i ≤ 10^6) and b (length m, 1 ≤ b_i ≤ 10^6). The function should also handle multiple test cases, where the number of test cases t is given (1 ≤ t ≤ 10^4). The sum of n over all test cases does not exceed 2 · 10^5, and the sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has processed all test cases, and for each test case, it has printed the number of valid segments of length `m` in the list `a` where at least `k` elements from the list `b` are present. The variables `n`, `m`, `k`, `a`, `b`, `todo`, `done`, `extra`, and `ans` are reset and reinitialized for each test case, so they do not retain their values between test cases. After the loop, the program has finished executing and there are no more test cases to process.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, and two lists of integers `a` and `b`. For each test case, it calculates the number of valid segments of length `m` in the list `a` where at least `k` elements from the list `b` are present. The function prints the result for each test case. The variables `n`, `m`, `k`, `a`, `b`, `todo`, `done`, `extra`, and `ans` are reset and reinitialized for each test case, so they do not retain their values between test cases. After processing all test cases, the program has finished executing.

