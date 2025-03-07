#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5, a is a list of n integers where 1 ≤ a_i ≤ 10^6, and b is a list of m integers where 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: The variable `ans` contains the number of contiguous subarrays of length `m` in the list `a` where at least `k` elements of the subarray are present in the set `todo` at the start of the subarray. The sets `todo`, `done`, and `extra` are modified during the loop execution, but their final states are not guaranteed to be predictable or meaningful outside the context of the loop. The variables `t`, `n`, `m`, `k`, `a`, and `b` retain their initial values as they are not modified within the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n`, an integer `m`, and an integer `k` from input, followed by a list `a` of `n` integers and a list of `m` integers representing elements to track. It then iterates through all contiguous subarrays of length `m` in `a`, counting how many of these subarrays contain at least `k` elements from the initial set of elements to track. The function prints the count for each test case. The input variables `t`, `n`, `m`, `k`, `a`, and `b` retain their initial values after the function concludes, and the internal sets `todo`, `done`, and `extra` are used for processing but do not have a meaningful final state outside the context of the function.

