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
        #The program does not return any value.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing (None)
    #State: `n` and `k` are positive integers such that 1 ≤ n, k ≤ 10^{18}, `n` is not equal to `k`, and `n` is greater than or equal to `k`
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: n is 0, h is the sum of the quotients from each division operation performed in the loop.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: costs (where costs is a list or iterable whose elements will be printed separated by spaces)
    #State: `n` is 0 and `h` is the sum of the quotients from each division operation performed in the loop. If `h` is less than `k`, then `h` remains less than `k`. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` (where 1 ≤ n, k ≤ 10^{18}). It prints 'YES' followed by 1, 1, 1 if `n` equals `k`. If `n` is less than `k`, it prints 'NO'. If `n` is greater than or equal to `k`, it calculates a list of costs and checks if the sum of quotients from division operations is at least `k`. If so, it prints '2', 'YES', and the list of costs; otherwise, it prints 'NO'. The function does not return any value in any case.

