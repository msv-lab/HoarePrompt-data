#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers a_i such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of each type initially.
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
        
    #State: Output State: All iterations of the loop have completed, and the value of `r` is determined based on whether `k` is zero or not. If `k` is zero, `r` will be the last element of the sorted list `a` plus any remaining value of `k` divided by the length of the list `a`. If `k` is not zero, `r` will be the last element of the sorted list `a` plus the entire value of `k` divided by the length of the list `a`.
    #
    #In more detail, after all iterations of the loop:
    #- If `k` is zero, `r` is calculated as `a[n-1] + k // n`.
    #- If `k` is non-zero, `r` is calculated as `a[n-1] + k // n`, and `k` will be adjusted to account for the remainder, which is added to `y`.
    #
    #The variable `y` represents the number of elements in the list `a` that were not fully adjusted by the loop, and `rem` is the remainder when `k` is divided by the number of elements processed before the loop broke out. However, since we are considering the final state after all iterations, `rem` and `y` do not affect the final value of `r` directly; they are used during the loop to adjust `r` and `k`.
    #
    #The final output will be `(r - 1) * n + 1` if `k` is zero, or `r` itself if `k` is non-zero, as per the loop's final print statement.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \), an integer \( k \), and a list of \( n \) integers \( a \). It sorts the list \( a \) and then iterates through it to determine the maximum value \( r \) based on the condition involving \( k \). Depending on whether \( k \) is zero or not, it calculates \( r \) either as the last element of the sorted list \( a \) plus the quotient of \( k \) divided by the length of \( a \), or as the last element of \( a \) plus the entire value of \( k \) divided by the length of \( a \). Finally, it prints the result, which is either \((r - 1) \times n + 1\) if \( k \) is zero, or simply \( r \) if \( k \) is non-zero.

