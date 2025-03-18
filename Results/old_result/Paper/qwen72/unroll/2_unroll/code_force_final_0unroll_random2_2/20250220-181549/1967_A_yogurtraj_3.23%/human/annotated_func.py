#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^12, representing the number of cards of each type. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: For each test case, the output state is the maximum number of cards that can be bought with the given number of coins, k, such that the total cost of the cards is minimized. The variables `t`, `n`, `k`, and `a` are not directly modified in the output state, but the loop calculates and prints the result for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the number of distinct types of cards `n` and the number of coins `k`, followed by a list `a` of `n` integers representing the number of cards of each type. The function then calculates and prints the maximum number of cards that can be bought with the given number of coins `k` such that the total cost of the cards is minimized. The variables `t`, `n`, `k`, and `a` are not modified in the output state, but the loop computes and prints the result for each test case.

