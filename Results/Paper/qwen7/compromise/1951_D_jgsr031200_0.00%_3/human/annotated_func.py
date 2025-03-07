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
        #The program returns the value of n (which is equal to k)
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
    #Explanation: The loop iterates over each element in the `costs` list. Initially, the first element of `costs` is `n - k + 1` and the second is `1`. In each iteration, `curr` is set to `n` divided by the current element in `costs`, then `h` is incremented by `curr` and `n` is decreased by `i * curr`. Since `n` is always reduced by a value derived from itself, it will eventually reach 0. The final value of `h` is the sum of `n // (n - k + 1)` and `n // 1`, both of which are integers.
    if (h < k) :
        print('NO')
        #This is printed: 'NO'
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: [] (assuming costs is an empty list)
    #State: `h` is the sum of `n // (n - k + 1)` and `n // 1`, `n` is 0, and if `h` is less than `k`, the function does nothing; otherwise, the function continues to execute the else part.
#Overall this is what the function does:The function accepts two parameters, n and k, both of which are positive integers within the range of 1 to 10^18. If n equals k, it prints 'YES' followed by 1 twice and returns the value of n. If n is less than k, it prints 'NO' and returns None. Otherwise, it calculates the sum of divisions of n by each element in the list [n - k + 1, 1], prints 'NO' if this sum is less than k, and prints 'YES', 2, and the list [n - k + 1, 1] if the sum is greater than or equal to k.

