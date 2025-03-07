#State of the program right berfore the function call: n and k are positive integers such that 1 <= n, k <= 10^{18}.
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
    #State: n and k are positive integers such that 1 <= n, k <= 10^{18}, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: `n` and `k` are positive integers such that 1 <= n, k <= 10^{18}, `n` is not equal to `k`, and `n` is greater than or equal to `k`
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: n is 0, k is unchanged, costs is unchanged, h is the sum of the quotients from the divisions performed in each iteration.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: the elements of the `costs` list separated by spaces
    #State: `n` is 0, `k` is unchanged, `costs` is unchanged, and `h` is the sum of the quotients from the divisions performed in each iteration. If `h` is less than `k`, then `h` remains less than `k`. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two parameters `n` and `k`, which are positive integers such that 1 <= n, k <= 10^{18}. Depending on the values of `n` and `k`, the function prints specific messages and values. If `n` equals `k`, it prints 'YES', followed by two '1's. If `n` is less than `k`, it prints 'NO'. If `n` is greater than or equal to `k`, it performs a series of calculations and prints 'NO' if the sum of the quotients is less than `k`, or 'YES' followed by the elements of a list `costs` if the sum is greater than or equal to `k`. The function does not return any value.

