#State of the program right berfore the function call: Each test case contains two integers n (1 ≤ n ≤ 2 · 10^5) and k (0 ≤ k ≤ 10^12), where n is the number of distinct types of cards and k is the number of coins. The second line of each test case contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^12), where a_i is the number of cards of type i initially available. The number of test cases t (1 ≤ t ≤ 100) is provided at the beginning, and the sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: A series of printed values, one for each test case, representing the final calculated value based on the distribution of coins among the card types.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of distinct card types `n`, a number of coins `k`, and a list of integers `a_1, a_2, ..., a_n` representing the initial count of cards for each type. For each test case, it calculates and prints a value based on the distribution of coins among the card types, which is derived from the given inputs.

