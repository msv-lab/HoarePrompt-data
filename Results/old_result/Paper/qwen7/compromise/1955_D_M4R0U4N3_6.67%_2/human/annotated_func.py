#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 ⋅ 10^5. a is a list of n integers such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n. b is a list of m integers such that 1 ≤ b_i ≤ 10^6 for all 1 ≤ i ≤ m. The sum of n over all test cases does not exceed 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: The loop will execute until `r` reaches `n-1`. After all iterations, the following will be true:
    #- `r` will be equal to `n-1`.
    #- `ans` will contain the total number of times the condition `len(done) >= k` was met during the loop's execution.
    #- The sets `todo`, `done`, and `extra` will reflect the final state of these sets after processing all elements from index `m` to `n-1` in the list `a` according to the rules specified in the loop body.
    #
    #All integers in `todo` have been processed and either moved to `done` or added to `extra`. The final value of `ans` will be the cumulative count of times the condition `len(done) >= k` was satisfied throughout the entire loop execution.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes integers t, n, m, and k, and lists a (of length n) and b (of length m) as inputs. It maintains three sets: todo, done, and extra. It iterates through the list a from index m to n-1, updating these sets based on certain conditions. Finally, it prints the total number of times the condition `len(done) >= k` is met during the iteration.

