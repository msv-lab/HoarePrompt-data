#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and m are integers such that 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop executes for each test case, and for each test case, it prints the sum of the absolute differences between elements of the sorted list `a` and elements of the sorted list `b` (in reverse order if necessary). The variables `t`, `n`, `m`, `a_i`, and `b_i` remain unchanged, but the lists `a` and `b` are sorted and possibly truncated to the lengths `n` and `m` respectively. The list `ans` is populated with the absolute differences and then cleared for the next test case. The variable `temp` is used to determine the point at which the loop should switch to using elements from the end of `b` instead of the beginning.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it takes two integers `n` and `m` and two lists of integers `a_i` and `b_i`. It computes the sum of the absolute differences between elements of the sorted list `a` (of length `n`) and elements of the sorted list `b` (of length `m`, in reverse order if necessary). The function prints this sum for each test case. The input variables `t`, `n`, `m`, `a_i`, and `b_i` remain unchanged, but the lists `a` and `b` are sorted and possibly truncated to the lengths `n` and `m` respectively.

