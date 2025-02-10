#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
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
                #This is printed: n - k + 1 1
            else :
                print('NO')
                #This is printed: NO
            #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer, `k` is an input integer, and n is greater than k. If the condition `(k - 1 < n - k + 1)` is satisfied, the condition remains unchanged. Otherwise, the condition `(k - 1 ≥ n - k + 1)` holds true.
        #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer, `k` is an input integer, and `n` is greater than or equal to `k`. If `n` equals `k`, then `n` remains unchanged. Otherwise, if the condition `(k - 1 < n - k + 1)` is satisfied, the condition remains unchanged. Otherwise, the condition `(k - 1 ≥ n - k + 1)` holds true.
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer, `k` is an input integer. If `n` is less than `k`, then `n` remains unchanged and `k` remains unchanged. Otherwise, `n` is greater than or equal to `k`, and if `n` equals `k`, then `n` remains unchanged. If `n` does not equal `k`, then the condition `(k - 1 < n - k + 1)` is checked. If the condition is true, `n` remains unchanged. If the condition is false, then `(k - 1 ≥ n - k + 1)` holds true.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers: t, n, and k. For each test case, it checks if n is less than k. If so, it prints 'NO'. If n equals k, it prints 'YES' followed by 1 twice. If n is greater than k and the condition (k - 1 < n - k + 1) is satisfied, it prints 'YES' followed by 2 and two integers representing the values of n - k + 1 and 1. Otherwise, it prints 'NO'. The function does not return any value but prints the results for each test case.

