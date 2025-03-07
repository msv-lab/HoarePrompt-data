#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each of the following t test cases consists of two positive integers n and k, where 1 <= n, k <= 10^{18}.
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
            #This is printed: n (where n is a positive integer such that 1 <= n <= 10^{18} and n is equal to k)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1, 1
            else :
                print('NO')
                #This is printed: NO
            #State: `t` is an integer such that 1 <= t <= 1000; `n` and `k` are the two positive integers read from the input, where 1 <= n, k <= 10^{18}; `n` is greater than or equal to `k`; `n` is not equal to `k`. If `k - 1` is less than `n - k + 1`, then `k - 1 < n - k + 1`. Otherwise, `k - 1` is not less than `n - k + 1`.
        #State: `t` is an integer such that 1 <= t <= 1000; `n` and `k` are the two positive integers read from the input, where 1 <= n, k <= 10^{18}; `n` is greater than or equal to `k`. If `n` is equal to `k`, no changes are made. Otherwise, `n` is greater than `k` and the relationship between `k - 1` and `n - k + 1` is determined: either `k - 1` is less than `n - k + 1` or `k - 1` is not less than `n - k + 1`.
    #State: `t` is an integer such that 1 <= t <= 1000; `n` and `k` are the two positive integers read from the input, where 1 <= n, k <= 10^{18}. If `n` is less than `k`, no changes are made. If `n` is equal to `k`, no changes are made. If `n` is greater than `k`, the relationship between `k - 1` and `n - k + 1` is determined: either `k - 1` is less than `n - k + 1` or `k - 1` is not less than `n - k + 1`.
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `k` from the input and prints "YES" followed by additional information if `n` is greater than or equal to `k` and certain conditions are met; otherwise, it prints "NO". Specifically, if `n` is equal to `k`, it prints "YES", "1", and `n`. If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, it prints "YES", "2", and the values `n - k + 1` and `1`. In all other cases, it prints "NO".

