#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^18.
def func_1(n, k):
    if (n == k) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(1)
        #This is printed: 1
        return
        #The program returns the value of n (which is equal to k)
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^18, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: 'NO'
        return
        #The program returns None
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^18, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: Output State: `costs` is `[n - k + 1, 1]`, `h` is the sum of `n // i` for each `i` in `costs`.
    #
    #In this output state, the variable `h` is updated to be the sum of `n // i` for each `i` in the list `costs`. The list `costs` remains unchanged, and `n` is reduced according to the loop's logic but its exact value depends on the initial value of `n` and the values in `costs`.
    if (h < k) :
        print('NO')
        #This is printed: 'NO'
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: - The output will be the elements of the list `costs` printed as `n - k + 1 1`.
        #
        #Output:
    #State: `costs` is `[n - k + 1, 1]`, `h` is the sum of `n // i` for each `i` in `costs`. If `h` is less than `k`, the function does not change `h`. If `h` is greater than or equal to `k`, the function does not change `h` either.
#Overall this is what the function does:The function accepts two parameters, n and k, both of which are positive integers with a constraint of 1 ≤ n, k ≤ 10^18. If n equals k, it prints "YES" followed by 1 twice and returns the value of n. If n is less than k, it prints "NO" and returns None. Otherwise, it calculates the sum of `n // i` for each `i` in the list `costs` where `costs` is initialized as `[n - k + 1, 1]`. If this sum is less than k, it prints "NO"; otherwise, it prints "YES", 2, and the elements of the list `costs`. The function returns None in all cases except when n equals k.

