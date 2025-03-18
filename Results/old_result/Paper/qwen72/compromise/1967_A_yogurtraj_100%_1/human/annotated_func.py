#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^12, representing the number of cards of type i you have at the beginning. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: For each test case, the output state will be a single integer representing the maximum number of cards that can be made equal by spending at most k coins. The variables t, n, k, a, r, rem, and y will have been updated and used during the loop, but the final output will be the calculated integer for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`, and a list of integers `a`. For each test case, it calculates and prints the maximum number of cards that can be made equal by spending at most `k` coins. The function reads the number of test cases `t` from input, and for each test case, it reads `n` and `k`, and a list `a` of `n` integers. After processing, the function prints the result for each test case, and the variables `t`, `n`, `k`, `a`, `r`, `rem`, and `y` are updated and used during the loop, but they do not retain any meaningful state after the function concludes.

