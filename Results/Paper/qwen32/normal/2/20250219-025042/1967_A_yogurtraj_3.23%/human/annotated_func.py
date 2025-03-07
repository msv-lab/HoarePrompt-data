#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and k is a non-negative integer such that 0 <= k <= 10^12. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^12. The sum of n across all test cases does not exceed 5 * 10^5.
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
        
    #State: the output state you calculate.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, a non-negative integer `k`, and a list `a` of `n` integers. For each test case, it calculates and prints a specific value based on the sorted list `a` and the value `k`. The output represents a computed result that depends on how much of `k` can be distributed among the elements of `a` while maintaining a certain order condition.

