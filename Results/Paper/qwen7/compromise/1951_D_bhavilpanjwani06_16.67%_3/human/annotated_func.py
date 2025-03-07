#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 1 ≤ n, k ≤ 10^{18}.
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
            #This is printed: n (where n is the integer such that 1 ≤ n ≤ 10^18 and n is equal to k)
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
            #State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that 1 ≤ k ≤ 10^18, and n is greater than k. If k - 1 < n - k + 1, no changes are made to `n` and `k`. Otherwise, the condition k - 1 ≥ n - k + 1 holds true.
        #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that 1 ≤ k ≤ 10^18, and if `n` equals `k`, no changes are made to `n` and `k`. If `n` is greater than `k`, the condition `k - 1 ≥ n - k + 1` holds true.
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that 1 ≤ k ≤ 10^18. If `n` is less than `k`, no changes are made to `n` and `k`. If `n` equals `k`, no changes are made to `n` and `k`. If `n` is greater than `k`, the condition `k - 1 ≥ n - k + 1` holds true.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers: t, n, and k. It checks the relationship between n and k and prints 'YES' or 'NO' based on specific conditions. If n is less than k, it prints 'NO'. If n equals k, it prints 'YES', 1, and n. If n is greater than k and k - 1 is less than or equal to n - k + 1, it prints 'YES', 2, n - k + 1, and 1. In all cases, it does not return any value but modifies and prints the values of n and k as per the conditions.

