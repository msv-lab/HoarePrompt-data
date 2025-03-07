#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, k is a non-negative integer such that 0 <= k <= 10^12, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^12. The sum of n over all test cases does not exceed 5 * 10^5.
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
        
    #State: A series of printed values, each corresponding to the result of a test case, based on the provided inputs and the logic of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n`, a non-negative integer `k`, and a list `a` of `n` integers. It calculates and prints a specific value based on these inputs, which represents a result derived from the sorted list and the value of `k`.

