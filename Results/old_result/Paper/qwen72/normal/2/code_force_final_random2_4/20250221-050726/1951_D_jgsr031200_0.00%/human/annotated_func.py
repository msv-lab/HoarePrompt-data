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
        #The program does not return any value.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^18, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value.
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^18, n is not equal to k, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: `n` is `0`, `k` is a positive integer such that 1 ≤ k ≤ 10^18, `n` is not equal to `k`, `n` is less than `k`, `costs` is `[n - k + 1, 1]`, `h` is `n // (n - k + 1) + n + 0`, `i` is `1`, `curr` is `0`.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: -k + 1, 1 (where k is a positive integer such that 1 ≤ k ≤ 10^18)
    #State: *`n` is `0`, `k` is a positive integer such that 1 ≤ k ≤ 10^18, `n` is not equal to `k`, `n` is less than `k`, `costs` is `[n - k + 1, 1]`, `h` is `n // (n - k + 1) + n + 0`, `i` is `1`, `curr` is `0`. If `h` is less than `k`, the condition `h < k` holds true. If `h` is greater than or equal to `k`, the condition `h >= k` holds true.
#Overall this is what the function does:The function `func_1` takes two positive integers `n` and `k` (where 1 ≤ n, k ≤ 10^18) and performs the following actions based on their values: If `n` equals `k`, it prints "YES" followed by two "1"s. If `n` is less than `k`, it prints "NO". If `n` is greater than `k`, it calculates a series of values and prints either "NO" or "2", "YES", and the values `-k + 1` and `1`. In all cases, the function does not return any value.

