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
    #State: n and k are positive integers such that 1 <= n, k <= 10^18, and n is not equal to k. Additionally, n is greater than or equal to k.
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: After the loop executes, `n` is 0, `h` is the sum of the initial values of `n // (n - k + 1)` and `n // 1`, and `costs` remains unchanged.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: [elements of costs] (where costs is the unchanged list of elements)
    #State: *After the loop executes, `n` is 0, `h` is the sum of the initial values of `n // (n - k + 1)` and `n // 1`, and `costs` remains unchanged. If `h` is less than `k`, the current value of `h` is less than `k`. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` (where 1 <= n, k <= 10^18) and performs the following actions based on the values of `n` and `k`:

1. If `n` is equal to `k`, it prints 'YES', followed by two '1's.
2. If `n` is less than `k`, it prints 'NO'.
3. If `n` is greater than or equal to `k` and the sum of `n // (n - k + 1)` and `n // 1` is less than `k`, it prints 'NO'.
4. If `n` is greater than or equal to `k` and the sum of `n // (n - k + 1)` and `n // 1` is greater than or equal to `k`, it prints 'YES', followed by '2' and the elements of the list `[n - k + 1, 1]`.

In all cases, the function does not return any value.

