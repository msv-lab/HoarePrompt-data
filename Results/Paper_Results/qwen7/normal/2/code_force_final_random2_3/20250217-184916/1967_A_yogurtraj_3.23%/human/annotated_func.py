#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and k are integers satisfying 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}, and for each test case, a list of n integers a_1, a_2, ..., a_n is provided where 1 ≤ a_i ≤ 10^{12}.
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
        
    #State: Output State: The loop has completed all its iterations, meaning `ii` (which represents the index of the current test case) is equal to the total number of test cases. After the final iteration, the value of `r` is determined as follows: if `k` is not zero, then `r` is `a[n-1] + k // n`. Otherwise, `r` is simply `a[n-1]`. The variable `rem` is 0, and `y` is 0 since no further increments or conditions were met to change their values beyond the third iteration.
    #
    #In more detail:
    #- `ii` equals the total number of test cases.
    #- If `k` is not zero, then `r` is set to `a[n-1] + k // n`.
    #- If `k` is zero, then `r` is set to `a[n-1]`.
    #- `rem` remains 0.
    #- `y` remains 0.
#Overall this is what the function does:The function processes up to 100 test cases, each consisting of a list of up to 200,000 integers and a threshold value k. For each test case, it calculates a result based on the sorted list of integers and the threshold value k. If k is non-zero, the result is the last element of the list plus k divided by the list length, adjusted by any remainder and additional count. If k is zero, the result is simply the last element of the list. The function outputs the calculated result for each test case.

