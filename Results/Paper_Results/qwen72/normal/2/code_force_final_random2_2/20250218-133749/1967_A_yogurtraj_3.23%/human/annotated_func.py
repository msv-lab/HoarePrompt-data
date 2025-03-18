#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins available for buying new cards, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^12, representing the initial number of cards of each type. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: After all iterations of the loop, `t` is an integer where 1 ≤ t ≤ 100, `ii` is `t - 1`, `n` is the first integer from user input and must be greater than 1, `a` is a sorted list of integers provided by the user, `i` is `n - 1`, `k` is 0, `y` is 0, and `rem` is 0. If `k` is not 0, `r` is `a[n - 1] + k // n`. Otherwise, `r` is the last element of `a` (i.e., `a[n-1]`).
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of card types (`n`), the number of coins available (`k`), and a list of initial card counts (`a`). For each test case, it calculates and prints the maximum number of new cards that can be bought such that the total number of cards of each type is as equal as possible, given the constraints of the number of coins. After processing all test cases, the function concludes without returning any value, but the printed output for each test case represents the solution to the problem.

