#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^12, representing the number of cards of type i initially available. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: `ii` is `t - 1`, `t` is an integer such that 1 ≤ t ≤ 100, `n` and `k` are input integers for the last test case, `a` is a sorted list of integers for the last test case. If `k` is not 0, `rem` is `k % (n - 1)`, `y` is `n - 1 - i`, and `r` is `a[n - 1] + k // n`. Otherwise, `rem` is 0, `k` is 0, `y` is 0, and `r` is `a[n-1]`.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of distinct types of cards `n`, the number of coins `k`, and a list `a` of initial card availabilities. For each test case, it calculates and prints the maximum number of cards that can be purchased with the given coins, considering the initial availability of each type of card. After processing all test cases, the function concludes, and the final state is that `ii` is `t - 1`, `t` is an integer such that 1 ≤ t ≤ 100, `n` and `k` are the input integers for the last test case, and `a` is a sorted list of integers for the last test case. If `k` is not 0 after processing, `rem` is `k % (n - 1)`, `y` is `n - 1 - i`, and `r` is `a[n - 1] + k // n`. Otherwise, `rem` is 0, `k` is 0, `y` is 0, and `r` is `a[n-1]`.

