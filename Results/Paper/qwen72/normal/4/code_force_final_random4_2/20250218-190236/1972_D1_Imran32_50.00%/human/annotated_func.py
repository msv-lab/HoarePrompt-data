#State of the program right berfore the function call: The function should take two parameters, n and m, which are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: `n` is at least 1, `k` is an input integer, `m` is a positive integer such that 1 <= m <= 2 * 10^6, `ans` is equal to `n` + Σ((`n` + i) // (i * i)) for i from 2 to `root`, `root` is equal to the integer part of the square root of `n` plus 1, `i` is `root` + 1, `cnt` is (`root` + 1) * (`root` + 1).
    print(ans)
    #This is printed: ans (where ans is \( n + \sum_{i=2}^{\text{root}} \left( \frac{n + i}{i^2} \right) \) and root is the integer part of the square root of n plus 1)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the user input, where `n` is a positive integer. It then calculates a value `ans` which is the sum of `n` and a series of terms derived from `n` and its square root. Specifically, `ans` is computed as `n` plus the sum of \((n + i) // (i * i)\) for each integer `i` from 2 to the integer part of the square root of `n` plus 1. Finally, the function prints the value of `ans`. The function does not return any value.

