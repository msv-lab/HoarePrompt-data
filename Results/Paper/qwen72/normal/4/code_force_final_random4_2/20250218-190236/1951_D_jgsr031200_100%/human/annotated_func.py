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
        
    #State: `n` and `k` are positive integers such that 1 <= n, k <= 10^18, and n is not equal to k. Additionally, n is greater than or equal to k. `costs` is a list with two elements: `[n - k + 1, 1]`. `h` is the sum of the quotients of `n` divided by each element in `costs` before the loop starts, and `n` is the remainder after subtracting the product of each element in `costs` and its corresponding quotient from the initial `n`.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: n - k + 1, 1 (where n and k are positive integers such that 1 <= n, k <= 10^18, n >= k, and n != k)
    #State: `n` and `k` are positive integers such that 1 <= n, k <= 10^18, and n is not equal to k. Additionally, n is greater than or equal to k. `costs` is a list with two elements: `[n - k + 1, 1]`. `h` is the sum of the quotients of `n` divided by each element in `costs` before the loop starts, and `n` is the remainder after subtracting the product of each element in `costs` and its corresponding quotient from the initial `n`. If `h` < `k`, the current value of `h` is less than `k`. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` (1 <= n, k <= 10^18). It prints 'YES' and the numbers 1, 1, 1 if `n` equals `k`. If `n` is less than `k`, it prints 'NO'. If `n` is greater than or equal to `k` and the sum of the quotients of `n` divided by `n - k + 1` and `1` is less than `k`, it prints 'NO'. Otherwise, it prints 'YES', the numbers 2, and the values `n - k + 1` and `1`. The function does not return any value.

