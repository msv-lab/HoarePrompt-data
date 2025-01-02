#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 150 000, and a is a list of 2n integers where 1 ≤ a_i ≤ 10^9.
def func():
    n = input()
    a = map(int, raw_input().split())
    mod = 998244353
    a.sort()
    firsum = 0
    secsum = 0
    for i in range(len(a)):
        if i < n:
            firsum += a[i]
        else:
            secsum += a[i]
        
    #State of the program after the  for loop has been executed: `n` is an input integer (1 ≤ n ≤ 150,000), `a` is a sorted list of 2n integers where 1 ≤ a_i ≤ 10^9, `mod` is 998244353, `firsum` is the sum of the first `n` elements of `a`, `secsum` is the sum of the last `n` elements of `a`.
    k = abs(secsum - firsum) % mod
    fac = [1, 1]
    for i in range(2, 2 * n + 1):
        fac.append(fac[-1] * i % mod)
        
    #State of the program after the  for loop has been executed: `n` is an input integer (1 ≤ n ≤ 150,000), `a` is a sorted list of 2n integers where 1 ≤ a_i ≤ 10^9, `mod` is 998244353, `firsum` is the sum of the first `n` elements of `a`, `secsum` is the sum of the last `n` elements of `a`, `k` is `abs(secsum - firsum) % mod`, `fac` is a list of length `2 * n + 1` where each element is the factorial of its index modulo `mod`, `i` is `2 * n + 1`.
    rr = fac[n] ** 2 % mod
    g = pow(rr, mod - 2, mod)
    print(k * (fac[2 * n] * g % mod) % mod)
#Overall this is what the function does:The function reads a positive integer `n` (1 ≤ n ≤ 150,000) and a list `a` of 2n integers (1 ≤ a_i ≤ 10^9) from standard input. It then sorts the list `a`, calculates the sum of the first `n` elements (`firsum`) and the sum of the last `n` elements (`secsum`). The function computes the absolute difference between `secsum` and `firsum`, takes the result modulo 998244353, and stores it in `k`. It also computes the factorial of each number from 0 to 2n (modulo 998244353) and stores these values in a list `fac`. The function then calculates the square of the factorial of `n` (modulo 998244353), finds its modular inverse, and uses these values to compute a final result which is printed to standard output. The function does not return any value. Edge cases include handling very large inputs efficiently to avoid performance issues.

