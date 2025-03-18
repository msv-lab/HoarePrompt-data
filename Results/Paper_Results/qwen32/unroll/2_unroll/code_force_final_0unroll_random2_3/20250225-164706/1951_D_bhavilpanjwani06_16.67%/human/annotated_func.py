#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n and k are integers such that 1 <= n, k <= 10^{18}.
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
                #This is printed: n - k + 1, 1 (where n - k + 1 is the difference between n and k plus 1)
            else :
                print('NO')
                #This is printed: NO
            #State: `t` is an integer such that 1 <= t <= 1000; `n` and `k` are integers read from the input such that 1 <= n, k <= 10^{18}, `n` is greater than or equal to `k`, and `n` is not equal to `k`. Additionally, if `k - 1` is less than `n - k + 1`, then `k - 1` is less than `n - k + 1`; otherwise, `k - 1` is not less than `n - k + 1`.
        #State: `t` is an integer such that 1 <= t <= 1000; `n` and `k` are integers read from the input such that 1 <= n, k <= 10^{18}, and `n` is greater than or equal to `k`. If `n` is equal to `k`, then no changes are made to `n` or `k`. Otherwise, `n` is not equal to `k`, and the relationship between `k - 1` and `n - k + 1` is determined, where either `k - 1` is less than `n - k + 1` or `k - 1` is not less than `n - k + 1`.
    #State: `t` is an integer such that 1 <= t <= 1000; `n` and `k` are integers read from the input such that 1 <= n, k <= 10^{18}. If `n` is less than `k`, then no changes are made to `n` or `k`. If `n` is greater than or equal to `k`, and `n` is equal to `k`, then no changes are made to `n` or `k`. If `n` is greater than `k`, and `n` is not equal to `k`, then the relationship between `k - 1` and `n - k + 1` is determined, where either `k - 1` is less than `n - k + 1` or `k - 1` is not less than `n - k + 1`.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input and prints "YES" followed by specific values if `n` is greater than or equal to `k` and certain conditions are met; otherwise, it prints "NO".

