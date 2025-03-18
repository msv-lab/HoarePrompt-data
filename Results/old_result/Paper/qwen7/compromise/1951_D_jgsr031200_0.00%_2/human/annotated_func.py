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
        
    #State: Output State: `costs` is `[n - k + 1, 1]`, `h` is the sum of `n` divided by each value in `costs` (ignoring the last element since it's always 1), `n` is 0.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: 1 1
    #State: Postcondition: `costs` is `[n - k + 1, 1]`, `h` is the sum of `n` divided by each value in `costs` (ignoring the last element since it's always 1), `n` is 0, and if `h` is less than `k`, the function does not change `h`. Otherwise, `h` is adjusted based on the condition being true or false.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` (both between 1 and \(10^{18}\)). It checks if `n` equals `k`, in which case it prints "YES" three times and returns `n`. If `n` is less than `k`, it prints "NO" and returns `None`. If `n` is greater than or equal to `k`, it calculates the sum of `n` divided by each value in the list `[n - k + 1, 1]` and stores it in `h`. If `h` is less than `k`, it prints "NO"; otherwise, it prints "YES", "2", and the list `[n - k + 1, 1]`. The function returns `n` if it equals `k` or `None` otherwise.

