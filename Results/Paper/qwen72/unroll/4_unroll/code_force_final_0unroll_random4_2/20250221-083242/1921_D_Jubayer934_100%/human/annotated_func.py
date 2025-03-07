#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and m are integers where 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop processes each test case by reading n and m, sorting the lists a and b, and calculating the sum of the minimum absolute differences between elements of a and b. The final output state is the sum of these minimum absolute differences for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers `n` and `m`, and two lists of integers `a` and `b`. It then calculates the sum of the minimum absolute differences between elements of `a` and `b` after sorting `a` in ascending order and `b` in descending order. The function prints the sum of these minimum absolute differences for each test case. The function does not return any value; it only prints the results.

