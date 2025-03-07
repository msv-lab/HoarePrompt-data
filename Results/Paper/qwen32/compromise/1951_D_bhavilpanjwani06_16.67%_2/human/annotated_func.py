#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, n and k are integers such that 1 <= n, k <= 10^{18}.
def func_1():
    n, k = map(int, input().split())
    if (n < k) :
        print('NO')
        #This is printed: NO
    else :
        if (n == k) :
            print('YES')
            #This is printed: YES
            print(1)
            #This is printed: 1
            print(n)
            #This is printed: n (where n is equal to k)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: - The first part of the print statement is `n - k + 1`, which is a positive integer based on the conditions provided.
                #   - The second part of the print statement is the integer `1`.
                #
                #### Conclusion:
                #Given the constraints and the print statement, the output will be the value of `n - k + 1` followed by `1`.
                #
                #### Final Output:
                #Output:
            else :
                print('NO')
                #This is printed: NO
            #State: `t` is an integer such that 1 <= t <= 1000; `n` and `k` are integers read from the input for the current test case such that 1 <= n, k <= 10^{18}. Additionally, `n` is greater than or equal to `k` and `n` is not equal to `k`. If `k - 1 < n - k + 1`, then the current value of `k` satisfies this condition. Otherwise, `k - 1` is not less than `n - k + 1`.
        #State: `t` is an integer such that 1 <= t <= 1000; `n` and `k` are integers read from the input for the current test case such that 1 <= n, k <= 10^{18}. Additionally, `n` is greater than or equal to `k`. If `n` is equal to `k`, no changes are made to `n` or `k`. Otherwise, `n` is greater than `k` and `k - 1` is compared with `n - k + 1`. If `k - 1` is less than `n - k + 1`, the current value of `k` satisfies this condition. Otherwise, `k - 1` is not less than `n - k + 1`.
    #State: `t` is an integer such that 1 <= t <= 1000; `n` and `k` are integers read from the input for the current test case such that 1 <= n, k <= 10^{18}. If `n` is less than `k`, no changes are made to `n` or `k`. If `n` is equal to `k`, no changes are made to `n` or `k`. If `n` is greater than `k`, `k - 1` is compared with `n - k + 1`. If `k - 1` is less than `n - k + 1`, the current value of `k` satisfies this condition. Otherwise, `k - 1` is not less than `n - k + 1`.
#Overall this is what the function does:The function reads pairs of integers `n` and `k` from the input for multiple test cases. For each test case, it prints "YES" followed by 1 and `n` if `n` equals `k`. If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, it prints "YES" followed by 2, `n - k + 1`, and 1. Otherwise, it prints "NO".

