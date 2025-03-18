#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are positive integers such that 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 10^9 for all i.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        temp = -1
        
        ans = []
        
        a = sorted(map(int, input().split()))[:n]
        
        b = sorted(map(int, input().split()), reverse=True)[:m]
        
        for i in range(n):
            if abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i]):
                temp = i
                break
            ans.append(abs(a[i] - b[i]))
        
        if temp != -1:
            for i in range(temp, n):
                ans.append(abs(a[i] - b[-(n - i)]))
        
        print(sum(ans))
        
    #State: Output State: The sum of absolute differences between the first `n` smallest elements of list `a` and the first `m` largest elements of list `b`, adjusted based on the condition in the loop. If the condition is met within the loop, the remaining differences are calculated using the corresponding elements from the end of list `b`.
#Overall this is what the function does:The function processes multiple test cases, each containing integers t, n, m, a_i, and b_i. For each test case, it sorts the lists a and b, then calculates the sum of absolute differences between the first n smallest elements of list a and the first m largest elements of list b. If a certain condition is met during the calculation, it adjusts the remaining differences using elements from the end of list b. The function outputs the sum of these absolute differences for each test case.

