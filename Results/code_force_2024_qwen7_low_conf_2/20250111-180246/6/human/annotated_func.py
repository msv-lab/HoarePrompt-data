#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    for t in range(int(input())):
        n, k = map(int, input().split())
        
        r = n
        
        if k >= n - 1:
            r = 1
        
        print(r)
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer such that \(1 \leq t \leq 10^3\), `n` is the last input integer, `k` is the last input integer, and `r` is equal to `n` if `k` is less than `n-1`, otherwise `r` is equal to `1`, and the printed value is either `n` or `1`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers \(n\) and \(k\), where \(1 \leq n \leq 100\) and \(0 \leq k \leq \frac{n(n-1)}{2}\). For each test case, it calculates an integer \(r\) based on the value of \(k\):

- If \(k < n - 1\), then \(r = n\).
- If \(k \geq n - 1\), then \(r = 1\).

The function prints the value of \(r\) for each test case. After processing all test cases, the function does not return anything explicitly, but the final state of the program is that it has processed all test cases and printed the corresponding values of \(r\). The function handles the following edge cases:
- If \(k = 0\), \(r\) is calculated correctly as \(n\).
- If \(k = n - 1\), \(r\) is set to \(1\).
- If \(n = 1\), \(k\) can only be \(0\) and \(r\) will be \(1\).

There is no explicit error handling for invalid inputs; the function assumes that the input values are within the specified ranges.

