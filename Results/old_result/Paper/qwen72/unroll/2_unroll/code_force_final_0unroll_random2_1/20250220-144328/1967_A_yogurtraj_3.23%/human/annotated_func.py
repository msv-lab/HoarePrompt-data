#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^12, representing the number of cards of type i. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: For each test case, the output state consists of the value of `r` and `rem` being the final computed values, and `y` being the number of elements in `a` that were not processed due to the break condition. The variable `k` is set to 0 if the loop breaks, otherwise it is the remaining value after the loop completes. The loop prints the calculated result for each test case. The values of `t`, `n`, `a`, and the initial `k` for each test case are unchanged.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of distinct types of cards `n`, the number of coins `k`, and a list `a` of integers representing the number of cards of each type. For each test case, it calculates and prints a result based on the distribution of cards and the available coins. The result is a single integer that represents a specific computation involving the cards and coins, but the exact meaning of this result is not explicitly defined. The function does not return any values; it only prints the results. The input variables `t`, `n`, `a`, and the initial `k` for each test case remain unchanged after the function execution.

