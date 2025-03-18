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
        
    #State: Output State: `costs` is a list containing the elements `n - k + 1` and `1`, `h` is equal to `n - (n - k + 1)`, `n` is reduced to `k - 1`.
    #
    #Explanation: After the loop completes all its iterations, the variable `n` is reduced by the sum of all elements in the `costs` list, which is `n - k + 1 + 1 = n - k + 2`. Since `h` is incremented by `curr` in each iteration and `curr` is always equal to `n // i`, which in the last iteration would be `1` (as `n` becomes `k - 1`), `h` will be incremented `n - k + 1` times plus one more time when `n` is `k - 1`, making it equal to `n`. However, since `n` is reduced to `k - 1` by the end of the loop, `h` will be `n - (n - k + 1)`, simplifying to `k - 1`.
    if (h < k) :
        print('NO')
        #This is printed: 'NO'
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: 0 1
    #State: `costs` is a list containing the elements `n - k + 1` and `1`, `h` is equal to `k - 1`, and `n` is equal to `k - 1`.
#Overall this is what the function does:The function accepts two parameters, n and k, both of which are positive integers between 1 and 10^18. It checks if n equals k, in which case it prints "YES" followed by 1 twice and returns n (or k). If n is less than k, it prints "NO" and returns None. If n is greater than or equal to k, it calculates the minimum number of operations required to reduce n to k using specific costs and prints "NO" if the total operations are less than k, otherwise it prints "YES", 2, "YES", and the list of costs. The function ultimately returns n (or k) if it prints "YES" or None if it prints "NO".

