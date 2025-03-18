#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are lists of integers where 1 ≤ a_i, b_i ≤ 10^9 for all i.
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
        
    #State: Output State: The loop has executed for all test cases, and for each test case, `temp` either holds the index where the condition `abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i])` was last true (if such an index exists) or remains `-1` if the condition was never met. The list `ans` contains the sum of the absolute differences between corresponding elements of lists `a` and `b` for all valid `i` in the range `[temp, n-1]` if `temp` is not `-1`, otherwise it contains the sum of the absolute differences for all valid `i` in the range `[0, n-1]`. The variable `i` is equal to `n` after the loop completes for each test case.
    #
    #In simpler terms, after all iterations of the loop, `temp` will hold the index where the specified condition was last true or will be `-1` if the condition was never met. The list `ans` will contain the total sum of the absolute differences between the elements of lists `a` and `b` as described above.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer t (1 ≤ t ≤ 100), followed by integers n and m (1 ≤ n ≤ m ≤ 2⋅10^5) and two lists a and b (1 ≤ a_i, b_i ≤ 10^9). For each test case, it calculates the sum of the absolute differences between corresponding elements of lists a and b, considering a specific condition. If a certain condition is met, it adjusts the calculation method. Finally, it prints the sum of these absolute differences for each test case.

