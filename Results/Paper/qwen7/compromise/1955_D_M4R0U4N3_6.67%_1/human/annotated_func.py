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
        
    #State: Output State: After the loop executes all iterations, `ans` will hold the total count of times the length of `done` met or surpassed the threshold `k`. The variable `r` will be set to `n - 1`, indicating the last index processed in the loop. The variable `old` will store the value of the last element (`a[r - m]`) that was checked within the loop. The set `extra` will contain all elements from `a` that were not in `todo` and hence added to `extra` during the loop. The set `done` will contain all elements from `a` that were removed from `todo`. The set `todo` will be empty as it will have been emptied out during the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( m \), and \( k \), and two lists \( a \) and \( b \). For each test case, it counts the number of times the set of completed tasks \( done \) reaches or exceeds the threshold \( k \) as elements are processed from list \( a \). It then prints the total count of such occurrences across all test cases.

