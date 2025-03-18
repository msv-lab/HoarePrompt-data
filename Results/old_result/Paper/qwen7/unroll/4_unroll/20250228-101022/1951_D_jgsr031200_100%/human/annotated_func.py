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
        #The program returns k (or n, since n equals k) as both are positive integers equal to each other and within the range of 1 to 10^18.
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
    #Explanation: The loop iterates over each element in `costs`. The first element of `costs` is `n - k + 1` and the second is `1`. In each iteration, `curr` is set to `n` divided by the current element in `costs`, then `h` is incremented by `curr`, and `n` is decreased by `i * curr`. After the first iteration (`i = n - k + 1`), `n` becomes 0 because `n // (n - k + 1)` will be at most 1 (if `n` is just slightly larger than `k-1`) and subtracting `(n - k + 1) * 1` from `n` will make it zero. In the second iteration (`i = 1`), `curr` will be `n // 1`, which is 0 since `n` is now 0, so no changes are made to `h` or `n`. Therefore, `h` becomes the sum of `n // (n - k + 1)` and `n // 1`, and `n` remains 0.
    if (h < k) :
        print('NO')
        #This is printed: 'NO'
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: Output:
    #State: `h` is the sum of `n // (n - k + 1)` and `n // 1`, and `n` is 0. Regardless of whether `h` is less than `k` or greater than or equal to `k`, the final values of `h` and `n` remain unchanged.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`, which are positive integers within the range of 1 to 10^18. If `n` equals `k`, it prints 'YES' followed by 1 and 1, then returns `k` (or `n`). If `n` is less than `k`, it prints 'NO' and returns `None`. If `n` is greater than or equal to `k`, it calculates the sum of `n // (n - k + 1)` and `n // 1`, stores these values in `h` and `n`, respectively, and prints 'YES', 2, and the values of `costs`. Finally, it returns `None` if `h` is less than `k`, otherwise, it returns `None`.

