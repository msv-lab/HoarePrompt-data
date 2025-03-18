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
            #This is printed: k (where k is the integer read from the input and n is equal to k)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1, 1 (where n - k + 1 is an integer greater than or equal to 1)
            else :
                print('NO')
                #This is printed: NO
            #State: `t` is an integer such that 1 ≤ t ≤ 1000; `n` and `k` are integers where 1 ≤ n, k ≤ \(10^{18}\), `n` is greater than or equal to `k`, and `n` is not equal to `k`. Additionally, if `k - 1 < n - k + 1`, the current value of `k` satisfies this condition. Otherwise, `k - 1` is not less than `n - k + 1`.
        #State: `t` is an integer such that 1 ≤ t ≤ 1000; `n` and `k` are integers where 1 ≤ n, k ≤ \(10^{18}\) and `n` is greater than or equal to `k`. If `n` is equal to `k`, no changes are made to `n` or `k`. Otherwise, `n` is not equal to `k`, and if `k - 1 < n - k + 1`, the condition holds true. Otherwise, `k - 1` is not less than `n - k + 1`.
    #State: `t` is an integer such that 1 ≤ t ≤ 1000; `n` and `k` are integers where 1 ≤ n, k ≤ \(10^{18}\). If `n` is less than `k`, no changes are made to `n` or `k`. If `n` is equal to `k`, no changes are made to `n` or `k`. If `n` is greater than `k`, `k - 1` is compared with `n - k + 1`. If `k - 1` is less than `n - k + 1`, the condition holds true. Otherwise, `k - 1` is not less than `n - k + 1`.
#Overall this is what the function does:The function reads two integers `n` and `k` from the input and prints "YES" followed by specific values if `n` is greater than or equal to `k` and certain conditions are met. If `n` is less than `k`, it prints "NO".

