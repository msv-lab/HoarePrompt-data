#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^18.
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
            #This is printed: n (where n is equal to k and both are input integers such that 1 ≤ n ≤ 10^18 and 1 ≤ k ≤ 10^18)
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1, 1 (where n - k + 1 is the result of the expression n - k + 1)
            else :
                print('NO')
                #This is printed: NO
            #State: *`t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer such that 1 ≤ n ≤ 10^18, `k` is an input integer such that 1 ≤ k ≤ 10^18, `n` is greater than or equal to `k`, and `n` is not equal to `k`. If `k - 1 < n - k + 1`, the condition holds true. Otherwise, `k - 1` is greater than or equal to `n - k + 1`.
        #State: *`t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer such that 1 ≤ n ≤ 10^18, `k` is an input integer such that 1 ≤ k ≤ 10^18, and `n` is greater than or equal to `k`. If `n` is equal to `k`, the condition holds true. Otherwise, if `k - 1 < n - k + 1`, the condition holds true. If neither of these conditions hold, `k - 1` is greater than or equal to `n - k + 1`.
    #State: *`t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer such that 1 ≤ n ≤ 10^18, and `k` is an input integer such that 1 ≤ k ≤ 10^18. If `n` < `k`, the condition holds true. If `n` ≥ `k`, the condition holds true if `n` = `k` or if `k - 1 < n - k + 1`. If neither of these conditions hold, `k - 1` is greater than or equal to `n - k + 1`.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input. It then checks if `n` is less than `k`. If so, it prints "NO". If `n` is equal to `k`, it prints "YES", followed by "1" and the value of `n`. If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, it prints "YES", followed by "2" and the values `n - k + 1` and `1`. Otherwise, it prints "NO". The function does not return any value; it only prints the results based on the conditions.

