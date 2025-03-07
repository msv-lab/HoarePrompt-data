#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n, m, and k are integers such that 1 <= k <= m <= n <= 2 * 10^5, a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, b is a list of m integers where each integer b_i satisfies 1 <= b_i <= 10^6.
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
        
    #State: The loop iterates `t` times, and for each iteration, it processes the lists `a` and `b` to determine the number of valid subarrays of length `m` in `a` where at least `k` elements are present in `b`. The variable `ans` holds the count of such valid subarrays for each test case, and it is printed after each iteration. The variables `n`, `m`, `k`, `a`, `todo`, `done`, `extra`, and `ans` are reset at the beginning of each iteration, so their values are not carried over between test cases. After all iterations, the values of `t`, `n`, `m`, `k`, `a`, and `b` remain unchanged, but the output of the program will be the printed values of `ans` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, and a list `a` of `n` integers. For each test case, it determines the number of valid subarrays of length `m` in `a` where at least `k` elements are present in the set `todo`, which is derived from user input. The function prints the count of such valid subarrays for each test case. The values of `t`, `n`, `m`, `k`, `a`, and `b` remain unchanged after the function execution, but the output of the program will be the printed values of `ans` for each test case.

