#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    for t in range(int(input())):
        n, k = map(int, input().split())
        
        r = n
        
        if k >= n - 1:
            r = 1
        
        print(r)
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer such that \(1 \leq t \leq 10^3\), `r` is always 1, `n` is an input integer, `k` is an input integer.
#Overall this is what the function does:The function `func` accepts a positive integer `t` such that \(1 \leq t \leq 10^3\). For each test case within `t`, it reads two integers `n` and `k` where \(1 \leq n \leq 100\) and \(0 \leq k \leq \frac{n \times (n - 1)}{2}\). It then determines whether `k` can represent a unique combination of two elements from a set of `n` elements. If `k` is within the valid range for the given `n`, it prints the value of `n` (which is always 1 in this case). If `k` is out of range, it prints 1. There is no explicit error message for out-of-range `k`; instead, it simply prints 1 for such cases. The function does not return anything explicitly but modifies the print statements based on the conditions checked.

