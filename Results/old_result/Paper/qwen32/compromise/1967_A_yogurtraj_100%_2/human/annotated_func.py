#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, k is a non-negative integer such that 0 <= k <= 10^12, and a is a list of n integers where each integer a_i is such that 1 <= a_i <= 10^12. The sum of n over all test cases does not exceed 5 * 10^5.
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
        
    #State: For the final test case processed, `t` remains the same, `ii` is `t-1`, `n` and `k` are from the last test case, `a` is the sorted list from the last test case, `r` is the final effective maximum value, `rem` is the remainder of `k` after the last increment (if applicable), `y` is the number of elements left unchanged (if applicable), and the final printed value is `(r - 1) * n + 1 + k % n` if `k` is not zero, otherwise `(r - 1) * n + 1 + rem + y`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, a non-negative integer `k`, and a list `a` of `n` integers. For each test case, it calculates and prints a specific result based on the values of `n`, `k`, and the sorted list `a`. The result is derived by determining an effective maximum value `r` and adjusting it according to the remaining value of `k` after processing the list.

