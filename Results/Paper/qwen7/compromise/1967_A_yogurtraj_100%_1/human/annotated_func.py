#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}; a is a list of n integers such that 1 ≤ a_i ≤ 10^{12}.
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
        
    #State: Output State: The loop has executed all its iterations, meaning `ii` is equal to the total number of test cases provided. After all iterations, the variable `n` will be 0 since it is decremented or remains 0 after the loop's conditions are met. The variable `k` will be 0 because it is fully reduced by the loop's operations. The variable `r` will hold the final result calculated based on the last iteration's conditions, which could be `a[n - 1] + k // n` if `k` is not 0, or simply `a[n - 1]` if `k` is 0. The variable `rem` will be 0 since it is set to `k % (i + 1)` when `k` is reduced to 0. The variable `y` will be 0 because it is only set during the loop and does not change afterward. The list `a` remains sorted and unchanged unless modified within the loop, and the overall postcondition covers all possible outcomes of the loop's execution.
    #
    #In summary, after all iterations, `ii` equals the total number of test cases, `n` is 0, `k` is 0, `r` is the final calculated result, `rem` is 0, `y` is 0, and `a` remains sorted.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \), \( k \), and a list \( a \) of \( n \) integers. For each test case, it sorts the list \( a \) and calculates a final value \( r \) based on the values in \( a \) and the integer \( k \). It then prints the result of the calculation, which depends on whether \( k \) is zero or not. After processing all test cases, the function outputs the final results for each case.

