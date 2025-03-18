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
        #The program returns nothing
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is not equal to k.
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, n is not equal to k, and n is greater than or equal to k.
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: n: 0, k: k, costs: [n - k + 1, 1], h: n // (n - k + 1) + k - 1.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: 1 - k 1 (where k is the value of k)
    #State: `n` is 0, `k` is `k`, `costs` is either `[1, 1]` if `h < k` or `[n - k + 1, 1]` if `h >= k`, and `h` is `n // (n - k + 1) + k - 1`, which simplifies to `k - 1` if `h < k` or remains as `n // (n - k + 1) + k - 1` if `h >= k`.
#Overall this is what the function does:The function `func_1` takes two positive integer parameters `n` and `k` (where 1 ≤ n, k ≤ 10^{18}). It prints "YES" and additional information if it's possible to make `n` equal to `k` through a series of operations, otherwise it prints "NO". The function does not return any value.

