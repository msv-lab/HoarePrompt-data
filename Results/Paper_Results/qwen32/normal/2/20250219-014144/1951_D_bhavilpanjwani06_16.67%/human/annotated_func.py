#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, there are two positive integers n and k such that 1 ≤ n, k ≤ 10^{18}.
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
            #This is printed: n (where n is equal to k for the current test case)
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
            #State: `t` is an integer such that 1 ≤ t ≤ 1000, and for each of the remaining t-1 test cases, there are two positive integers n and k such that 1 ≤ n, k ≤ 10^{18}. Additionally, n is greater than or equal to k, and n is not equal to k. For the current test case, either `k - 1 < n - k + 1` or `k - 1` is not less than `n - k + 1`.
        #State: `t` is an integer such that 1 ≤ t ≤ 1000, and for each of the remaining t-1 test cases, there are two positive integers n and k such that 1 ≤ n, k ≤ 10^{18} and n is greater than or equal to k. If n is equal to k, then no specific change is made to n or k for the current test case. Otherwise, for the current test case, either `k - 1 < n - k + 1` or `k - 1` is not less than `n - k + 1`.
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, and for each of the remaining t-1 test cases, there are two positive integers n and k such that 1 ≤ n, k ≤ 10^{18}. If the current value of `n` is less than `k`, then no specific change is made to `n` or `k` for the current test case. Otherwise, `n` is greater than or equal to `k`. If `n` equals `k`, no specific change is made to `n` or `k`. If `n` is greater than `k`, then either `k - 1 < n - k + 1` or `k - 1` is not less than `n - k + 1`.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two positive integers `n` and `k`. For each test case, it prints 'YES' followed by the number of integers and the integers themselves if certain conditions are met; otherwise, it prints 'NO'. Specifically, if `n` is less than `k`, it prints 'NO'. If `n` equals `k`, it prints 'YES', followed by `1` and `n`. If `n` is greater than `k` and `k - 1` is less than `n - k + 1`, it prints 'YES', followed by `2`, `n - k + 1`, and `1`. In all other cases, it prints 'NO'.

