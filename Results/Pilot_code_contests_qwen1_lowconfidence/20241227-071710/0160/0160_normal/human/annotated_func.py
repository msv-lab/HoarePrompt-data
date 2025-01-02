#State of the program right berfore the function call: N is an integer such that 2 ≦ N ≦ 10^{12} and X is an integer such that 1 ≦ X ≦ N-1.
def func():
    L = map(int, raw_input().split())
    n = L[0]
    x = L[1]
    res = n
    a = x
    b = n - x
    flag = True
    while flag:
        if a > b:
            q = a // b
            a -= q * b
            res += 2 * q * b
        elif b > a:
            q = b // a
            b -= q * a
            res += 2 * a * q
        else:
            res += a
            flag = False
        
    #State of the program after the loop has been executed: `N` is an integer such that \(2 \leq N \leq 10^{12}\); `X` is an integer such that \(1 \leq X \leq N-1\); `L` is a list of integers; `n` is the first element of `L`; `x` is the second element of `L`; `res` is the final result of the loop calculations; `a` is the final value of the second element of `L` (`x`); `b` is the final value of `n - x`; `flag` is `False`.
    print(res)
#Overall this is what the function does:The function reads two integers \(N\) and \(X\) from the standard input, where \(2 \leq N \leq 10^{12}\) and \(1 \leq X \leq N-1\). It then calculates a result based on a series of operations involving \(N\), \(X\), and their differences. Specifically, it repeatedly reduces \(N\) and \(X\) using division and subtraction until they become equal, updating the result accordingly. The final result is printed to the standard output. The function does not accept any parameters and returns nothing. Potential edge cases include when \(N\) and \(X\) are equal initially, in which case the result is simply \(N\). The function also handles the case where \(N\) and \(X\) are such that one is always larger than the other during the iterations.

