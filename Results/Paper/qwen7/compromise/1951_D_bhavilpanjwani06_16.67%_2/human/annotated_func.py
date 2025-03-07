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
            print(n)
            #This is printed: n (where n is equal to k)
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
            #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer, `k` is an input integer, and `n` is greater than `k`. If `(k - 1 < n - k + 1)` is true, no changes are made to the variables. Otherwise, the condition `(k - 1 ≥ n - k + 1)` is true.
        #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer, `k` is an input integer, and `n` is greater than or equal to `k`. If `n` equals `k`, no changes are made to the variables. Otherwise, if `(k - 1 ≥ n - k + 1)` is true, no changes are made to the variables.
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer, and `k` is an input integer. If `n` is less than `k`, no changes are made to the variables. Otherwise, if `n` is greater than or equal to `k`, and the condition `(k - 1 ≥ n - k + 1)` is true, no changes are made to the variables. If the condition is false, no changes are made to the variables as well.
#Overall this is what the function does:The function processes three integers: `t`, `n`, and `k`. It checks if `t` is within the range 1 to 1000, and if `n` and `k` are positive integers up to \(10^{18}\). Based on the relationships between `n` and `k`, it prints either "YES" or "NO". If `n` is less than `k`, it prints "NO". If `n` equals `k`, it prints "YES", `1`, and `n`. If `n` is greater than `k` and `(k - 1 < n - k + 1)`, it prints "YES", `2`, `n - k + 1`, and `1`. Otherwise, it prints "NO". The function does not return any value but modifies the output through printing.

