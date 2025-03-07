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
        
    #State: `n` is 0, `k` remains unchanged, `costs` remains unchanged, `h` is `k + (n - k + 1) // (n - k + 1)`.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: [elements of the `costs` list separated by spaces] (where `costs` is a list of integers that remains unchanged)
    #State: *`n` is 0, `k` remains unchanged, `costs` remains unchanged, `h` is `k + (n - k + 1) // (n - k + 1)`. If `h` is less than `k`, the current value of `h` is less than `k`. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` within the range 1 to 10^18. It prints 'YES' and the numbers 1, 1, 1 if `n` equals `k`. If `n` is less than `k`, it prints 'NO'. If `n` is greater than or equal to `k` and the calculated value of `h` (which involves some arithmetic operations on `n` and `k`) is less than `k`, it prints 'NO'. Otherwise, it prints 'YES' followed by the numbers 2 and the elements of the `costs` list. The function does not return any value.

