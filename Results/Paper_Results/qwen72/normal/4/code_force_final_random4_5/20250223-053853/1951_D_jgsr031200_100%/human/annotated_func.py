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
    #State: n and k are positive integers such that 1 <= n, k <= 10^18, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: n and k are positive integers such that 1 <= n, k <= 10^18, and n is not equal to k. Additionally, n is greater than or equal to k.
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: `n` is 0, `k` remains unchanged, `costs` remains unchanged, `h` is the sum of the initial values of `n // (n - k + 1)` and `n // 1`.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: [elements of costs separated by spaces]
    #State: *`n` is 0, `k` remains unchanged, `costs` remains unchanged, `h` is the sum of the initial values of `n // (n - k + 1)` and `n // 1`. If `h` is less than `k`, the condition `h < k` holds. Otherwise, the condition `h >= k` holds.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` (where 1 <= n, k <= 10^18) and performs the following actions based on the values of `n` and `k`:

- If `n` equals `k`, it prints 'YES' followed by two '1's.
- If `n` is less than `k`, it prints 'NO'.
- If `n` is greater than or equal to `k`, it calculates a list `costs` with two elements: `n - k + 1` and `1`. It then iterates over `costs`, performing a series of operations that reduce `n` to 0. After the operations, if the sum of the calculated values (`h`) is less than `k`, it prints 'NO'. Otherwise, it prints 'YES', followed by '2' and the elements of `costs`.

In all cases, the function does not return any value. After the function concludes, `n` is 0, `k` remains unchanged, and `costs` remains unchanged.

