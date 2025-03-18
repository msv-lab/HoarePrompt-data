#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, n and k are integers for each test case where 1 <= n <= 2 * 10^5 and 0 <= k <= 10^12, and a is a list of n integers such that 1 <= a_i <= 10^12.
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
        
    #State: `t` is an integer such that 1 <= t <= 100, `ii` is `t - 1`, `n` is the integer input for the last test case, `i` is `n - 2`, `a` is a sorted list of integers input by the user for the last test case, `r` is the last element of the list `a` before the loop breaks or completes. If `k` is not 0, `r` is the last element of the list `a` plus the integer division of `k` by `n`. If the loop breaks, `k` is 0, `y` is `n - 1 - i` (the number of elements remaining in the list after the break), and `rem` is `k % (i + 1)`. If the loop completes without breaking, `k` is the remaining value after all subtractions, and `r` is the last element of the list `a`. If `k` is 0, `r` is the last element of the list `a` before the loop breaks or completes, and `k` is 0.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it takes an integer `n` and a long integer `k`, along with a list of `n` integers `a`. It sorts the list `a` and then iterates through it to find a specific value `r` and a remainder `rem`. The function calculates and prints a result for each test case, which is a combination of `r`, `n`, `rem`, and `y` (the number of elements remaining in the list after a certain condition is met). The final state of the program after the function concludes is that `t` test cases have been processed, and a result has been printed for each one. The variables `ii`, `n`, `i`, `a`, `r`, `rem`, `y`, and `k` are in their final states as described in the annotated code.

