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
        #The program returns None
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
        
    #State: `n = 0`, `h = (n - k + 1) // (n - k + 1) + (n - k + 1) // 1`, `costs = [n - k + 1, 1]`.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: - The code snippet `print('YES')` will execute because the condition `h >= k` is true.
        #
        #Output:
        print(*costs)
        #This is printed: 0 1
    #State: *`n` is 0, `h` is calculated as `(n - k + 1) // (n - k + 1) + (n - k + 1) // 1`, and `costs` is a list with values `[n - k + 1, 1]`. If `h` is less than `k`, then `h < k`. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, both of which are positive integers such that 1 <= n, k <= 10^18. The function performs the following actions based on the values of `n` and `k`:

1. If `n` is equal to `k`, it prints 'YES', followed by two '1's, and returns `None`.
2. If `n` is less than `k`, it prints 'NO' and returns nothing.
3. If `n` is greater than `k`, it calculates a list `costs` with values `[n - k + 1, 1]` and a variable `h` which is the sum of `n // (n - k + 1)` and `n // 1`. It then prints 'NO' if `h` is less than `k`, or prints '2', 'YES', and the values in `costs` if `h` is greater than or equal to `k`.

The final state of the program after the function concludes is that `n` is 0, `h` is calculated as described, and `costs` is a list with values `[n - k + 1, 1]`. The function does not return any value in any case.

