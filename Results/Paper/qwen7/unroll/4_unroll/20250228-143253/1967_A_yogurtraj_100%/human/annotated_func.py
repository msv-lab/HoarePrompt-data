#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of type i initially.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of type i after redistributing the cards according to the given algorithm. The final value of r is determined based on the redistribution process, and the final output prints the total count of cards after redistribution.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes the number of card types (n), a redistribution limit (k), and a list of initial card counts (a). It redistributes the cards according to a specific algorithm to ensure the redistribution limit is met. After processing each test case, it outputs the total count of cards after redistribution. The function does not return any value but prints the results for each test case.

