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
        #The program does not return any value.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value.
    #State: `n` and `k` are positive integers such that 1 ≤ n, k ≤ 10^{18}, `n` is not equal to `k`, and `n` is greater than or equal to `k`
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: n=0, k=k, costs=[1-k, 1], h=n-k+1
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: 1-k 1
    #State: `n` is 0, `k` is `k`, `costs` is `[1-k, 1]`, and `h` is `n-k+1`. If `h` is less than `k`, then `h` equals `-k+1`. Otherwise, `h` is greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `n` and `k` (where 1 ≤ n, k ≤ 10^{18}). It prints 'YES' and additional information if `n` can be reduced to 0 by subtracting multiples of `k` or `n-k+1` a total of at least `k` times. Otherwise, it prints 'NO'. The function does not return any value.

