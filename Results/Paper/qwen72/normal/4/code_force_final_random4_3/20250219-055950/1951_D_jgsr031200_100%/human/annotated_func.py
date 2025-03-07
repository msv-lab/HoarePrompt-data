#State of the program right berfore the function call: n and k are positive integers such that 1 <= n, k <= 10^18.
def func_1(n, k):
    if (n == k) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(1)
        #This is printed: 1
        return
        #The program returns nothing.
    #State: n and k are positive integers such that 1 <= n, k <= 10^18, and n is not equal to k.
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: n and k are positive integers such that 1 <= n, k <= 10^18, n is not equal to k, and n is greater than or equal to k.
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: `i` is 1, `costs` is `[n - k + 1, 1]`, `curr` is `n // 1`, `h` is `h + (n // (n - k + 1)) + (n % (n - k + 1) // 1)`, `n` is `n % (n - k + 1) % 1`
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: 1 - k 1 (where k is the value of k)
    #State: *`i` is 1, `costs` is `[n - k + 1, 1]`, `curr` is `n // 1`, `h` is `h + (n // (n - k + 1)) + (n % (n - k + 1) // 1)`, and `n` is `n % (n - k + 1) % 1`. If `h` is less than `k`, `h` remains less than `k`. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` (where 1 <= n, k <= 10^18) and performs the following actions: If `n` is equal to `k`, it prints 'YES' followed by two '1's and returns. If `n` is less than `k`, it prints 'NO' and returns. If `n` is greater than `k`, it calculates a series of values and prints 'NO' if the sum of these values is less than `k`. Otherwise, it prints 'YES', followed by '2', and the values in the `costs` list. The function does not return any value.

