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
            #This is printed: k (where k is the input integer)
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
            #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer greater than `k`, and if `(k - 1) < (n - k + 1)`, then the condition holds as is. Otherwise, the condition `(k - 1) ≥ (n - k + 1)` holds.
        #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer greater than or equal to `k`, and `a` is a list of integers. If `n` equals `k`, then `n` remains unchanged and the condition holds as is. Otherwise, if `(k - 1) < (n - k + 1)`, the condition holds as is. Otherwise, the condition `(k - 1) ≥ (n - k + 1)` holds.
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an input integer. If `n` is less than `k`, then the condition `1 ≤ t ≤ 1000` and `n < k` holds. Otherwise, if `n` is greater than or equal to `k`, the condition `1 ≤ t ≤ 1000` and `n ≥ k` holds. Additionally, if `n` equals `k`, `n` remains unchanged. If `n` does not equal `k`, then either the condition `(k - 1) < (n - k + 1)` holds, or the condition `(k - 1) ≥ (n - k + 1)` holds.
#Overall this is what the function does:The function processes a series of test cases, each containing integers \( t \), \( n \), and \( k \). It checks if \( n \geq k \). If \( n < k \), it prints "NO". If \( n = k \), it prints "YES", 1, and \( n \). If \( n > k \), it further checks if \( k - 1 < n - k + 1 \). If true, it prints "YES", 2, and \( n - k + 1 \) and 1. Otherwise, it prints "NO". The function does not return any value but prints the results directly.

