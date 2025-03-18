#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and k is a non-negative integer such that 0 <= k <= 10^12. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^12. The sum of n over all test cases does not exceed 5 * 10^5.
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
        
    #State: A series of printed results for each test case, where each result is calculated based on the conditions described in the code.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, a non-negative integer `k`, and a list `a` of `n` integers. For each test case, it calculates and prints a result based on the values of `n`, `k`, and the sorted list `a`. The result is derived by determining the maximum value that can be achieved by incrementing the elements of the list within the constraint `k`.

