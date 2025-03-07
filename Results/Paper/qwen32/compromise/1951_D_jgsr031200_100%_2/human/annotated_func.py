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
        #The program returns nothing.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value
    #State: `n` and `k` are positive integers such that 1 ≤ n, k ≤ 10^{18}, and `n` is not equal to `k`. Additionally, `n` is greater than or equal to `k`.
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: n is 0, k remains unchanged, costs remains [n - k + 1, 1], h is k + 1.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: 1 - k, 1 (where k is the unchanged value of k)
    #State: `n` is 0, `k` remains unchanged, `costs` remains [n - k + 1, 1], `h` is `k + 1`. If `h` is less than `k`, then the condition `h < k` holds. Otherwise, `h` is not less than `k`.
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `n` and `k` (where 1 ≤ n, k ≤ 10^{18}). It prints 'YES' followed by 1 and 1 if `n` equals `k`. If `n` is less than `k`, it prints 'NO'. Otherwise, it performs a series of calculations and prints 'YES' followed by 2 and two integers `[n - k + 1, 1]` if a certain condition is met; otherwise, it prints 'NO'. The function does not return any value.

