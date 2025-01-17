#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each test case contains an integer n such that 1 ≤ n ≤ 50, and a list of n integers k_1, k_2, ..., k_n such that 2 ≤ k_i ≤ 20. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 10^4\), `N` is an integer such that \(1 \leq N \leq 50\), `vals` is a list of \(N\) integers such that \(2 \leq k_i \leq 20\), `prod` is the product of all elements in `vals`, `r` is the last element of `vals`
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        return
        #-1
    #State of the program after the if block has been executed: `t` is an integer such that \(1 \leq t \leq 10^4\), `N` is an integer such that \(1 \leq N \leq 50\), `vals` is a list of \(N\) integers such that \(2 \leq k_i \leq 20\), `prod` is the product of all elements in `vals`, `r` is the last element of `vals`, `vprod` is a list of length \(N\) where `vprod[i]` is `prod // vals[i]` for each `i` in range \(0, N\), and `den` is `prod - sum(vprod)`. The difference `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
#Overall this is what the function does:The function `func_1` accepts an integer `t` such that \(1 \leq t \leq 10^4\) as input. For each test case within `t`, it reads an integer `N` such that \(1 \leq N \leq 50\) and a list of `N` integers `vals` where each integer \(k_i\) satisfies \(2 \leq k_i \leq 20\). The function calculates the product of all elements in `vals` and stores it in `prod`. It then computes a list `vprod` where each element `vprod[i]` is `prod // vals[i]`. After that, it calculates `den` as `prod - sum(vprod)` and checks if `den` is less than or equal to 0. If `den` is less than or equal to 0, the function prints `-1` and returns immediately. Otherwise, it prints the elements of `vprod` as a space-separated string.

