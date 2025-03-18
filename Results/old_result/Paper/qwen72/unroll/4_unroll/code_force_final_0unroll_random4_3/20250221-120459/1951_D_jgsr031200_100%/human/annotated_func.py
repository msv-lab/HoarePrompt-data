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
        #The program returns None.
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
        
    #State: `n` is 0, `k` remains the same, `costs` remains the same, `h` is the sum of the initial values of `n // (n - k + 1)` and `n // 1`.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES (if k is 0 or less)
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: [elements of the `costs` list separated by spaces] (where `costs` is the list of integers)
    #State: *`n` is 0, `k` remains the same, `costs` remains the same, `h` is the sum of the initial values of `n // (n - k + 1)` and `n // 1`. If `h` is less than `k`, then `h` is less than `k`. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` (where 1 <= n, k <= 10^18). If `n` equals `k`, it prints 'YES', followed by two '1's and returns `None`. If `n` is less than `k`, it prints 'NO' and returns `None`. If `n` is greater than or equal to `k`, it calculates a series of values and prints 'YES' followed by '2' and the elements of the `costs` list if the sum of certain divisions (`h`) is greater than or equal to `k`. Otherwise, it prints 'NO' and returns `None`. In all cases, the function modifies `n` to 0 and does not return any value.

