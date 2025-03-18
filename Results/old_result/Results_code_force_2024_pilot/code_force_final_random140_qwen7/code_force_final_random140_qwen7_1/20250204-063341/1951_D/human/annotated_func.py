#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^18.
def func_1():
    n, k = map(int, input().split())
    if (n < k) :
        print('NO')
        #This is printed: 'NO'
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
                #This is printed: n - k + 1, 1
            else :
                print('NO')
                #This is printed: 'NO'
            #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer greater than `k`, and the function evaluates whether `(k - 1 < n - k + 1)`. If the condition is true, the function does not change `t`. If the condition is false, the function also does not change `t`. Therefore, `t` remains within the range 1 ≤ t ≤ 1000.
        #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer greater than or equal to `k`. If `n` equals `k`, the function does not change `t`. Otherwise, `t` remains within the range 1 ≤ t ≤ 1000 regardless of the evaluation of the condition `(k - 1 < n - k + 1)`.
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer. If `n` is less than `k`, then `t` remains within the range 1 ≤ t ≤ 1000. If `n` is greater than or equal to `k`, then `t` also remains within the range 1 ≤ t ≤ 1000, and if `n` equals `k`, `t` is unchanged.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `t` (1 ≤ t ≤ 1000) and two positive integers `n` and `k` (1 ≤ n, k ≤ 10^18). For each test case, it checks if `n` is less than `k`. If true, it prints "NO". If `n` equals `k`, it prints "YES" followed by 1 twice. If `n` is greater than `k` and `(k - 1 < n - k + 1)` is true, it prints "YES" followed by 2 and `n - k + 1`. If none of these conditions are met, it prints "NO". The function does not return any value but prints the results for each test case.

