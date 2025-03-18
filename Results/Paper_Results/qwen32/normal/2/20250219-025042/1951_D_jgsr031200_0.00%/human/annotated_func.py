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
        
    #State: `costs` is `[n - k + 1, 1]`; `curr` is `n`; `h` is `h + n`; `n` is `0`; `i` is `1`.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: -k + 1 1 (where k is a value such that h >= k)
    #State: `costs` is `[n - k + 1, 1]`; `curr` is `n`; `h` is `h + n`; `n` is `0`; `i` is `1`. Additionally, `h` is either less than `k` or greater than or equal to `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `n` and `k` (where 1 ≤ n, k ≤ 10^{18}). It prints "YES" followed by 1 three times if `n` equals `k`. If `n` is less than `k`, it prints "NO". Otherwise, it calculates a series of values and prints "NO" if a certain condition is not met; otherwise, it prints "2", "YES", and two specific values derived from `n` and `k`. The function does not return any value in any case.

