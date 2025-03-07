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
        
    #State: All test cases have been processed, `i` equals `n`, `temp` is either -1 or the index where the condition was first violated, `ans` is a list containing the sum of absolute differences between corresponding elements of lists `a` and `b` for all valid indices as per the loop logic, and the variables `a`, `b`, and `temp` retain their final states after processing all test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers t, n, m, a_i, and b_i. For each test case, it sorts two lists, a and b, of lengths n and m respectively. It then calculates the sum of absolute differences between corresponding elements of these lists, considering a specific condition. If a certain condition is violated during the process, it adjusts the sum calculation. Finally, it prints the sum of these absolute differences for each test case.

