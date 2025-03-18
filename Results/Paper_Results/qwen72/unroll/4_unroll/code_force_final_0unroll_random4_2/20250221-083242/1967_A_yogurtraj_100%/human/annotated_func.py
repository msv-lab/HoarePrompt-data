#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and k are integers for each test case where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, and a is a list of n integers where 1 ≤ a_i ≤ 10^12.
def func():
    for ii in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        r = a[0]
        
        rem = 0
        
        y = 0
        
        for i in range(0, n - 1):
            if (i + 1) * (a[i + 1] - a[i]) > k:
                r = a[i] + k // (i + 1)
                rem = k % (i + 1)
                y = n - 1 - i
                k = 0
                break
            else:
                k -= (i + 1) * (a[i + 1] - a[i])
                r = a[i + 1]
        
        if k != 0:
            r = a[n - 1] + k // n
            print((r - 1) * n + 1 + k % n)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: The loop iterates through each test case, and for each test case, it prints the final value calculated based on the conditions in the loop. The variables `t`, `n`, `k`, and `a` are updated for each test case, but their values are reset at the start of each new test case. After all iterations, the final state of `t` is 0, and the values of `n`, `k`, and `a` are undefined for the next test case (if any). The loop does not modify any variables outside of its scope.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the number of integers `n` and a target integer `k`, followed by a list of `n` integers `a`. It then sorts the list `a` and calculates a final value based on the sorted list and the target integer `k`. The function prints this final value for each test case. After processing all test cases, the function does not return any value, but the output for each test case is the calculated final value. The function does not modify any variables outside of its scope, and the state of `t`, `n`, `k`, and `a` is reset for each new test case.

