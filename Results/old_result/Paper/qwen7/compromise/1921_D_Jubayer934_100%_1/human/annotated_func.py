#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers where 1 ≤ a_i, b_i ≤ 10^9.
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
        
    #State: After all iterations, `i` is equal to `n-1`, `temp` is either `-1` or its final value determined during the loop, and `ans` is a list containing the absolute differences between each element in `a` and the corresponding element in `b`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers t, n, m, a_i, and b_i. It calculates the sum of absolute differences between the first n elements of sorted lists a and b (where b is sorted in descending order). If a certain condition is met during the calculation, it adjusts the result list accordingly. Finally, it prints the sum of the absolute differences for each test case.

