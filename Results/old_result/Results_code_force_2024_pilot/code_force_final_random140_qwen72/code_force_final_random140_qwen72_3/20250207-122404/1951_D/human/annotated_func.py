#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers where 1 ≤ n, k ≤ 10^18.
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
            print(1)
            #This is printed: 1
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1, 1 (where n and k are positive integers such that n > k and 2k < n + 2)
            else :
                print('NO')
                #This is printed: NO
            #State: *`t` is an integer where 1 ≤ t ≤ 1000, `n` and `k` are positive integers provided by the user input, where 1 ≤ n, k ≤ 10^18, and `n` is greater than or equal to `k`. Additionally, `n` is not equal to `k`. If `2k < n + 2`, then the condition `(k - 1 < n - k + 1)` holds true. Otherwise, `(k - 1) ≥ (n - k + 1)`.
        #State: *`t` is an integer where 1 ≤ t ≤ 1000, `n` and `k` are positive integers provided by the user input, where 1 ≤ n, k ≤ 10^18, and `n` is greater than or equal to `k`. If `n` is equal to `k`, no further changes are made. If `n` is greater than `k`, then if `2k < n + 2`, the condition `(k - 1 < n - k + 1)` holds true. Otherwise, `(k - 1) ≥ (n - k + 1)`.
    #State: *`t` is an integer where 1 ≤ t ≤ 1000, `n` and `k` are positive integers provided by the user input, where 1 ≤ n, k ≤ 10^18. If `n` < `k`, no changes are made. If `n` ≥ `k`, then if `n` = `k`, no further changes are made. If `n` > `k`, then if `2k < n + 2`, the condition `(k - 1 < n - k + 1)` holds true. Otherwise, `(k - 1) ≥ (n - k + 1)`.
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `k` from user input for each test case, where `1 ≤ n, k ≤ 10^18`. It evaluates whether `n` can be split into two parts such that one part is `k - 1` and the other is `n - k + 1`. If `n < k`, it prints 'NO'. If `n == k`, it prints 'YES' followed by two lines, each containing the number `1`. If `n > k` and `2k < n + 2`, it prints 'YES', followed by `2`, and then the values `n - k + 1` and `1`. If `n > k` and `2k ≥ n + 2`, it prints 'NO'. The function processes up to 1000 test cases, each time reading new values for `n` and `k`. After processing each test case, the function does not modify the values of `n` and `k` for subsequent test cases.

