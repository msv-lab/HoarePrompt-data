#State of the program right berfore the function call: n is a non-negative integer, q is a positive integer greater than 1 and is used as the modulus in the calculations.
def func_1(n, q):
    fact = [(1) for _ in range(n + 1)]
    inv = [(1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % q
        
        inv[i] = pow(fact[i], q - 2, q)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `q` is a positive integer greater than 1, `fact` is a list of length `n + 1` where `fact[i]` is equal to the factorial of `i` modulo `q` for each `i` in the range `[0, n]`, `inv` is a list of length `n + 1` where `inv[i]` is the modular multiplicative inverse of `fact[i]` modulo `q` for each `i` in the range `[1, n]`, and all other elements are equal to 1.
    return fact, inv
    #The program returns `fact` and `inv`. `fact` is a list of length `n + 1` where each element `fact[i]` is equal to the factorial of `i` modulo `q`. `inv` is a list of length `n + 1` where each element `inv[i]` is the modular multiplicative inverse of `fact[i]` modulo `q` for each `i` in the range `[1, n]`, and all other elements are equal to 1.
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` (a non-negative integer) and `q` (a positive integer greater than 1). It computes and returns two lists, `fact` and `inv`. `fact` is a list of length `n + 1` where each element `fact[i]` is the factorial of `i` modulo `q`. `inv` is a list of length `n + 1` where each element `inv[i]` is the modular multiplicative inverse of `fact[i]` modulo `q` for each `i` in the range `[1, n]`, and `inv[0]` is always 1. The function handles the edge case where `n` is 0 by returning `[1]` for both `fact` and `inv`.

#State of the program right berfore the function call: n, k are non-negative integers such that 0 <= k <= n, q is a positive integer, F and I are lists of integers where F[n] and I[k] are defined and non-negative, and I[n - k] is defined and non-negative.
def func_2(n, k, q, F, I):
    return F[n] * (I[k] * I[n - k] % q) % q
    #The program returns (F[n] * (I[k] * I[n - k] % q)) % q, where F[n], I[k], and I[n - k] are non-negative integers from the lists F and I, and q is a positive integer.
#Overall this is what the function does:The function `func_2` takes five parameters: `n`, `k`, `q`, `F`, and `I`. `n` and `k` are non-negative integers with the constraint `0 <= k <= n`. `q` is a positive integer. `F` and `I` are lists of integers where `F[n]`, `I[k]`, and `I[n - k]` are defined and non-negative. The function returns the result of the expression `(F[n] * (I[k] * I[n - k] % q)) % q`.

Potential Edge Cases and Missing Functionality:
- If `n` is less than `k`, the function will still execute, but it will access `I[n - k]`, which might be out of bounds if `n < k`. This should be handled to avoid index errors.
- If `F` or `I` do not have the required indices defined, the function will raise an `IndexError`.
- The function assumes that `F[n]`, `I[k]`, and `I[n - k]` are non-negative integers, but this is not enforced by the function itself. If these values are not non-negative, the behavior of the function may be undefined or incorrect.

#State of the program right berfore the function call: n, m, and k are integers such that 1 <= n, m <= 2 * 10^5 and 0 <= k <= n - 1.
def func_3():
    MOD = 998244353
    n, m, k = rli()
    F, I = func_1(n, MOD)
    ans = 0
    for i in range(n - k, n + 1):
        ans += func_2(n - 1, i - 1, MOD, F, I) * m * pow(m - 1, i - 1, MOD) % MOD
        
    #State of the program after the  for loop has been executed: `n`, `m`, and `k` are integers such that \(1 \leq n, m \leq 2 \times 10^5\) and \(0 \leq k \leq n - 1\); `MOD` is 998244353; `F` and `I` are the values returned by `func_1(n, MOD)`, `ans` is the sum of `func_2(n - 1, i - 1, MOD, F, I) * m * pow(m - 1, i - 1, MOD) % MOD` for `i` from `n - k` to `n`.
    print(ans % MOD)
#Overall this is what the function does:The function `func_3` accepts three parameters `n`, `m`, and `k`, where `n` and `m` are integers such that \(1 \leq n, m \leq 2 \times 10^5\), and `k` is an integer such that \(0 \leq k \leq n - 1\). It computes a result using a combination of precomputed values from `func_1` and iterative calculations involving `func_2`. The final result is printed modulo 998244353. The state of the program after the function concludes is that `n`, `m`, and `k` remain unchanged, and the computed result is printed. The function does not return any value. Potential edge cases include when `k` is 0 or `n-1`, which may affect the range of the loop and thus the final result.

