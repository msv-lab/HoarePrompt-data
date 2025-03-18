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
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, n is not equal to k, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: `n` is `0`, `k` is a positive integer such that 1 ≤ k ≤ 10^{18}, `n` is not equal to `k`, `n` is greater than or equal to `k` (this condition is no longer valid because `n` is `0`), `costs` is a list `[n - k + 1, 1]`, `h` is `2 * (n // i)`, `curr` is `n // i`, `i` is `n - k + 1` (this `i` value is from the first iteration and does not change the final state)
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: 1 - k, 1 (where k is a positive integer such that 1 ≤ k ≤ 10^{18})
    #State: `n` is `0`, `k` is a positive integer such that 1 ≤ k ≤ 10^{18}, `n` is not equal to `k`, `costs` is a list `[n - k + 1, 1]`, `i` is `n - k + 1`, `curr` is `n // i`, and `h` is `2 * (n // i)`. If `h` is less than `k`, then no further changes are made. Otherwise, no further changes are made either.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` (where 1 ≤ n, k ≤ 10^{18}). It prints 'YES' and additional values if `n` can be reduced to 0 by subtracting multiples of `n - k + 1` and 1, such that the total number of subtractions is at least `k`. Otherwise, it prints 'NO'. The function does not return any value.

