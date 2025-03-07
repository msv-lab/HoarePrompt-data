#State of the program right berfore the function call: The function should accept multiple test cases. For each test case, the inputs are three integers n, k, and x where 1 ≤ n ≤ 2 · 10^5, 1 ≤ k, x ≤ n, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        a.reverse()
        
        sum1 = sum(a)
        
        ans = []
        
        for i in range(k + 1):
            if i == 0:
                sums = sum1 - 2 * sum(a[:x])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: For each test case, the loop prints the maximum value from the list `ans` which contains the results of the modified sums after iterating through the specified range. The variables `n`, `k`, `x`, and the list `a` are unchanged after the loop finishes executing for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it accepts three integers `n`, `k`, and `x`, and a list of `n` integers. It calculates a series of modified sums based on these inputs and prints the maximum of these sums. The variables `n`, `k`, `x`, and the list `a` are not modified after the function processes each test case.

