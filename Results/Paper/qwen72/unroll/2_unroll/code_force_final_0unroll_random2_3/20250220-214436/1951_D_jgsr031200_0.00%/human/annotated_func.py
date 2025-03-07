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
    #State: `n` and `k` are positive integers such that 1 <= n, k <= 10^18, and `n` is not equal to `k`. Additionally, `n` is greater than or equal to `k`.
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: `n` is 0, `h` is the sum of the quotients of `n` divided by each element in `costs` before the loop starts, and `costs` remains `[n - k + 1, 1]` (but `n` is now 0).
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: 1 - k, 1 (where k is a positive integer)
    #State: `n` is 0, `h` is the sum of the quotients of `n` divided by each element in `costs` before the loop starts, and `costs` remains `[n - k + 1, 1]` (but `n` is now 0). If `h` is less than `k`, the current value of `h` is less than `k`. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` (where 1 <= n, k <= 10^18) and performs the following actions based on the input values:

- If `n` is equal to `k`, it prints "YES" followed by two "1"s and then returns.
- If `n` is less than `k`, it prints "NO" and then returns.
- If `n` is greater than or equal to `k`, it calculates the sum of the quotients of `n` divided by each element in the list `[n - k + 1, 1]` and updates `n` accordingly. If the sum of these quotients (`h`) is less than `k`, it prints "NO". Otherwise, it prints "2", "YES", and the elements of the list `[n - k + 1, 1]` (which are `1 - k` and `1`).

In all cases, the function does not return any value.

