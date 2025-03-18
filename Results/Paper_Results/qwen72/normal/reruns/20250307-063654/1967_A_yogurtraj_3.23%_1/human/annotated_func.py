#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, and a is a list of n integers where 1 ≤ a_i ≤ 10^12. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: `ii` is `t - 1`, `n` is the last `n` value provided by the input, `k` is 0, `a` is a sorted list of integers provided by the input, `r` is the last element of the sorted list `a` or the element calculated as `a[i] + k // (i + 1)` where the condition `(i + 1) * (a[i + 1] - a[i]) > k` was met, `rem` is the remainder of `k` divided by `i + 1` when the condition was met, and `y` is `n - 1 - i` where the condition was met or 0 if it never was. If `k` was not 0, `r` is updated to `a[n - 1] + k // n`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n`, an integer `k`, and a list of `n` integers `a`. For each test case, it calculates and prints a specific integer value based on the sorted list `a` and the value of `k`. The final state of the program after the function concludes is that `ii` is `t - 1`, `n` is the last `n` value provided by the input, `k` is 0, `a` is a sorted list of integers provided by the input, `r` is the last element of the sorted list `a` or a calculated value, `rem` is the remainder of `k` divided by `i + 1` when a specific condition was met, and `y` is `n - 1 - i` where the condition was met or 0 if it never was. The function does not return any value but prints the result for each test case.

