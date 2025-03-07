#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
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
                #This is printed: n - k + 1, 1 (where n - k + 1 is a positive integer greater than 1 based on the given conditions)
            else :
                print('NO')
                #This is printed: NO
            #State: `t` is an integer such that 1 ≤ t ≤ 1000; `n` and `k` are positive integers such that 1 ≤ n, k ≤ \(10^{18}\) and are assigned the values read from the input. Additionally, `n` is greater than or equal to `k`. `n` is not equal to `k`. If `k - 1 < n - k + 1`, the current value of `k` satisfies this condition. Otherwise, `k - 1` is not less than `n - k + 1`.
        #State: `t` is an integer such that 1 ≤ t ≤ 1000; `n` and `k` are positive integers such that 1 ≤ n, k ≤ \(10^{18}\) and are assigned the values read from the input. Additionally, `n` is greater than or equal to `k`. If `n` is equal to `k`, no changes are made to `n` or `k`. Otherwise, `n` is not equal to `k`, and if `k - 1 < n - k + 1`, the current value of `k` satisfies this condition. Otherwise, `k - 1` is not less than `n - k + 1`.
    #State: `t` is an integer such that 1 ≤ t ≤ 1000; `n` and `k` are positive integers such that 1 ≤ n, k ≤ \(10^{18}\). If `n` is less than `k`, no changes are made to `n` or `k`. If `n` is greater than or equal to `k`, no changes are made to `n` or `k` if `n` equals `k`. Otherwise, if `n` is not equal to `k`, `k - 1` is compared to `n - k + 1`; no specific change is indicated based on this comparison alone.
#Overall this is what the function does:The function reads two positive integers `n` and `k` for each of `t` test cases. It prints "YES" followed by 1 and `n` if `n` equals `k`. If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, it prints "YES" followed by 2, `n - k + 1`, and 1. Otherwise, it prints "NO".

