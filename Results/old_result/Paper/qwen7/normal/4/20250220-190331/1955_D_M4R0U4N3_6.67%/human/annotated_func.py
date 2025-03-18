#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2⋅10^5. a is a list of n integers such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n. b is a list of m integers such that 1 ≤ b_i ≤ 10^6 for all 1 ≤ i ≤ m. The sum of n over all test cases does not exceed 2⋅10^5, and the sum of m over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all iterations, the following conditions hold:
    #
    #- The variable `ans` will be incremented by 1 each time the length of `done` reaches or exceeds `k`.
    #- The set `todo` will contain elements that were originally in `a` but are neither in `done` nor `extra`.
    #- The set `done` will contain elements that were moved from `todo` to `done` as per the conditions inside the loop.
    #- The set `extra` will contain elements from `a` that were never in `todo`.
    #- The variable `r` will be equal to `n`.
    #- The value of `ans` will be the total number of times the length of `done` reached or exceeded `k` during the entire execution of the loop.
    #
    #In summary, `ans` will reflect how many times the condition `len(done) >= k` was met throughout the loop's execution, considering all elements in `a` have been processed.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it analyzes a list of integers `a` and determines how many times the count of elements in `done` (elements that satisfy certain conditions) reaches or exceeds a specified threshold `k`. It does this by iterating through the list `a`, managing sets `todo`, `done`, and `extra` to track elements based on their presence and movement between these sets. The function ultimately outputs the total count of such occurrences for each test case.

