#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, representing the number of test cases. For each test case, n and k are integers where 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, representing the number of distinct types of cards and the number of coins, respectively. a is a list of n integers where 1 <= a_i <= 10^12, representing the number of cards of type i. The sum of n over all test cases does not exceed 5 * 10^5.
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
        
    #State: The loop has finished executing for all test cases. For each test case, the output is the maximum number of cards that can be bought with the given number of coins, k, such that the number of cards of each type is at most the calculated value r. The variables t, n, k, a, r, rem, and y have been updated accordingly for each test case, but the initial value of t (the number of test cases) remains unchanged.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the number of distinct types of cards (`n`), the number of coins (`k`), and a list of the number of cards of each type (`a`). It calculates and prints the maximum number of cards that can be bought with the given number of coins, ensuring that the number of cards of each type does not exceed a calculated value `r`. The function does not return any value but outputs the result for each test case. After processing all test cases, the initial value of `t` (the number of test cases) remains unchanged.

