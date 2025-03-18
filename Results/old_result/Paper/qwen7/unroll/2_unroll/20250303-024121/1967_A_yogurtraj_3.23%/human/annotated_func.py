#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of each type initially.
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
            print((r - 1) * n + 1)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of each type after redistribution according to the loop's logic. The variable r holds the maximum value of the cards after redistribution, rem holds the remaining redistribution points, and y holds the count of cards that received the final increment.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t`, followed by two integers `n` and `k`, and a list `a` of `n` integers. For each test case, it redistributes the values in list `a` based on the value of `k`. It calculates the maximum value `r` that can be achieved after redistribution and any remaining redistribution points `rem`. Additionally, it counts the number of cards `y` that receive the final increment. Finally, it prints the result based on the calculated values.

