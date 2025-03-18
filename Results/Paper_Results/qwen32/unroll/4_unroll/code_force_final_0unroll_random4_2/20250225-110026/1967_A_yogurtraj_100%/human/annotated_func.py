#State of the program right berfore the function call: Each test case contains two integers n (1 ≤ n ≤ 2 · 10^5) and k (0 ≤ k ≤ 10^12) representing the number of distinct types of cards and the number of coins, respectively. The second line of each test case contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^12) representing the number of cards of type i initially available. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: The final printed result for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` representing the number of distinct types of cards, an integer `k` representing the number of coins, and a list of `n` integers representing the initial count of each card type. It calculates and prints the maximum number of additional cards that can be obtained given the number of coins and the initial availability of each card type.

