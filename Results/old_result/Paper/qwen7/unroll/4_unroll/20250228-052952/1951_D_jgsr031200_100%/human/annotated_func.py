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
        #The program returns the value of n (or k, since they are equal), which is a positive integer between 1 and 10^18.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: Output State: `h` is the sum of `n // (n - k + 1)` and `n // 1`, `n` is 0.
    #
    #Explanation: The loop iterates over each element in `costs`. Initially, `costs[0]` is `n - k + 1` and `costs[1]` is `1`. In each iteration, `curr` is set to `n` divided by the current element in `costs`, then `h` is incremented by `curr`, and `n` is reduced by `i * curr`. Since `n` starts as a positive integer and gets reduced in each iteration, it will eventually become 0. After the first iteration with `i = n - k + 1`, `curr` will be 1 because `n // (n - k + 1)` equals 1. Then `h` will increase by 1 and `n` will be reduced by `n - k + 1`. In the second iteration with `i = 1`, `curr` will be `n // 1`, which is now `n - (n - k + 1)`, so `h` will increase by `n - (n - k + 1)`, and `n` will be reduced to 0.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: [] (assuming costs is an empty list)
    #State: `h` is the sum of `n // (n - k + 1)` and `n // 1`, `n` is 0, and if `h` is less than `k`, the function does nothing. Otherwise, the function continues with the else part where `h` is adjusted accordingly.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, both of which are positive integers between 1 and \(10^{18}\). It checks if `n` is equal to `k`, in which case it prints "YES" followed by three 1s and returns `n`. If `n` is less than `k`, it prints "NO" and returns `None`. If `n` is greater than or equal to `k`, it calculates the sum of divisions of `n` by elements in the list `[n - k + 1, 1]` and stores it in `h`. If `h` is less than `k`, it prints "NO"; otherwise, it prints "YES", 2, and the list `[n - k + 1, 1]`. The function ultimately returns `n` if the conditions are met or `None` otherwise.

