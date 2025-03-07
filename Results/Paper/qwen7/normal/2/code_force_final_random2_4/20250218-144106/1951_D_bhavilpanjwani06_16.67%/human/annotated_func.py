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
            print(n)
            #This is printed: k
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
            #State: t is an integer such that 1 ≤ t ≤ 1000, n is an input integer, k is an input integer, and n is greater than k. If k - 1 is less than n - k + 1, then no change is made to the variables. Otherwise, the condition k - 1 ≥ n - k + 1 holds true.
        #State: t is an integer such that 1 ≤ t ≤ 1000, n is an input integer, k is an input integer, and if n equals k, then no change is made to the variables. Otherwise, if k - 1 ≥ n - k + 1 holds true, then the condition k - 1 ≥ n - k + 1 is maintained.
    #State: t is an integer such that 1 ≤ t ≤ 1000, n is an input integer, k is an input integer. If n is less than k, then no change is made to the variables. Otherwise, if k - 1 ≥ n - k + 1 holds true, then the condition k - 1 ≥ n - k + 1 is maintained.
#Overall this is what the function does:The function processes a series of test cases, each containing three integers: t, n, and k. For each test case, it checks if n is less than k. If so, it prints 'NO'. If n equals k, it prints 'YES', 1, and n. If n is greater than k and k - 1 is less than n - k + 1, it prints 'YES', 2, n - k + 1, and 1. Otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

