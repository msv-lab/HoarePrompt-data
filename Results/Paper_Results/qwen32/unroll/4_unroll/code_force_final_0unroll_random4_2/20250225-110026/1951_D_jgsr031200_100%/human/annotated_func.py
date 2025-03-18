#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
def func_1(n, k):
    if (n == k) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(1)
        #This is printed: 1
        return
        #The program returns nothing (None)
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is not equal to k.
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value.
    #State: `n` and `k` are positive integers such that 1 ≤ n, k ≤ 10^{18}, `n` is not equal to `k`, and `n` is greater than or equal to `k`
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: n is 0, k is unchanged, costs is [n - k + 1, 1], h is the sum of n // (n - k + 1) and n.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: 1 1
    #State: `n` is 0, `k` is unchanged, `costs` is `[n - k + 1, 1]`, `h` is the sum of `n // (n - k + 1)` and `n`. If `h` is less than `k`, then `h` is less than `k`. Otherwise, `h` is not less than `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `n` and `k` (where 1 ≤ n, k ≤ 10^{18}). It prints "YES" and additional information if it is possible to perform a series of operations such that the sum of the operations is at least `k`. Otherwise, it prints "NO". The function does not return any value (None).

