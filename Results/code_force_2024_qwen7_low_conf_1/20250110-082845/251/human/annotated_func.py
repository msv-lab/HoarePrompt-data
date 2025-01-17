#State of the program right berfore the function call: t, n, m, and k are integers such that 1 <= t <= 57000, 1 <= n, m <= 10^6, and 2 <= k <= 10^12. The value of n * m >= k after each cut, and the sum of n and m over all test cases does not exceed 10^6.
def func_1():
    input = sys.stdin.read
    data = input().split()
    MOD = 1000000007
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        m = int(data[idx + 1])
        
        k = int(data[idx + 2])
        
        idx += 3
        
        low, high = 0, max(n, m) * 20
        
        answer = high
        
        while low <= high:
            mid = (low + high) // 2
            if func_2(n, m, k, mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        p = answer
        
        q = 1
        
        q_inv = pow(q, MOD - 2, MOD)
        
        result = p * q_inv % MOD
        
        results.append(result)
        
    #State of the program after the  for loop has been executed: 
    for res in results:
        print(res)
        
    #State of the program after the  for loop has been executed: `results` is a non-empty iterable, and all elements of `results` have been printed.
#Overall this is what the function does:- If \(n\) or \(m\) is zero, the function should handle these cases appropriately since the initial conditions assume \(1 \leq n, m \leq 10^6\).
- If \(k\) is less than or equal to \(0\), the function should handle these cases as well, although the problem constraints specify \(2 \leq k \leq 10^{12}\), so this scenario is unlikely.
- The binary search is set up to search within the range \([0, \max(n, m) \times 20]\), which might not cover all possible values of \(p\) for very large \(n\) and \(m\). However, given the constraints, this range is likely sufficient.
- The function does not explicitly handle the case where \(n\) or \(m\) is equal to zero, which could lead to undefined behavior in the calculation of \(p\). This should be addressed to ensure robustness.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 10^6, k is a positive integer such that 2 <= k <= 10^12, and steps is a non-negative integer.
def func_2(n, m, k, steps):
    h, w = n, m
    for _ in range(steps):
        if h > w:
            h = max(h // 2, 1)
        else:
            w = max(w // 2, 1)
        
        if h * w < k:
            return True
        
    #State of the program after the  for loop has been executed: `steps` is a non-negative integer, `h` is either the result of repeatedly applying `h //= 2` until `h <= w` and then setting it to `max(h, 1)`, or remains the original value `n` if the loop does not execute, and `w` is either the result of repeatedly applying `w //= 2` until `w >= h` and then setting it to `max(w, 1)`, or remains the original value `m` if the loop does not execute, and if `h * w < k`, the function returns True, otherwise it returns nothing.
    return h * w < k
    #`The program returns True if h * w < k, otherwise it returns nothing`
#Overall this is what the function does:The function `func_2` accepts four parameters: `n`, `m`, `k`, and `steps`. All of `n`, `m`, and `k` are positive integers with specific constraints (1 ≤ n, m, k ≤ 10^6 and 2 ≤ k ≤ 10^12), and `steps` is a non-negative integer.

- The function iterates `steps` times, halving `h` when it is greater than `w` and halving `w` when it is less than or equal to `h`. Both `h` and `w` are ensured to be at least 1 after each iteration.
- After the loop, the function checks if the product of `h` and `w` is less than `k`. If it is, the function returns `True`; otherwise, it returns `None`.

This means the function returns `True` if, after performing the specified operations for `steps` iterations, the product of `h` and `w` is still less than `k`. Otherwise, it returns `None`.

