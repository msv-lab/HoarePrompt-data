#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
def func():
    for tc in range(int(input())):
        N = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = defaultdict(int)
        
        for i in range(N):
            cnt[a[i]] += 1
        
        t = 0
        
        for i in range(N):
            if cnt[i] == 1:
                t += 1
            if t >= 2 or cnt[i] == 0:
                print(i)
                break
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, N is a positive integer such that 1 ≤ N ≤ 2 ⋅ 10^5, and a is a list of N non-negative integers where each integer a_i satisfies 0 ≤ a_i < N. The sum of all N values across all test cases does not exceed 2 ⋅ 10^5. After executing the loop, for each test case, the variable `i` is the first integer in the list `a` that either appears exactly once or causes the count of any previously seen integer to reach zero, or `i` is the last integer in the list `a` if no such integer is found.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \(N\), a list of \(N\) non-negative integers \(a\), and calculates a value \(t\). It then finds the first integer in the list \(a\) that either appears exactly once or causes the count of any previously seen integer to reach zero. If such an integer is found, it prints the integer and breaks the loop; otherwise, it prints the last integer in the list \(a\). The function does not return any value but outputs the results for each test case.

