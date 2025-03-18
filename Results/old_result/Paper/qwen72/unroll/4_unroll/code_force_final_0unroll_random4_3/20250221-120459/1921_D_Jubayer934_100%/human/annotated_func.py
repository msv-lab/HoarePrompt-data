#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and m are integers such that 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, b_i is a list of m integers where 1 ≤ b_i ≤ 10^9, and the sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop processes each test case, and for each test case, it prints the sum of the minimum absolute differences between elements of the sorted list `a` and the reversed sorted list `b`. The variables `t`, `n`, `m`, `a_i`, and `b_i` are not directly modified by the loop, but the loop uses their values to compute the result for each test case. After all iterations, the loop has completed its execution, and the final output state is the sum of the minimum absolute differences for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads two integers `n` and `m`, followed by two lists of integers `a` and `b` of lengths `n` and `m` respectively. It computes the sum of the minimum absolute differences between elements of the sorted list `a` and elements of the reversed sorted list `b`. The function prints the sum for each test case. The input variables `t`, `n`, `m`, `a_i`, and `b_i` are not modified by the function, and the final state of the program is the printed sum for each test case.

