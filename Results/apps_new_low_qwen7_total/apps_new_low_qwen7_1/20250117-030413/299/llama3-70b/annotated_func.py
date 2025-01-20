#State of the program right berfore the function call: n and k are non-negative integers such that 1 ≤ n, k ≤ 10^18 and k ≤ n.
def func():
    n, k = map(int, input().split())
    if ((n - 1) // k > n // k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is an integer between 1 and \(10^{18}\) inclusive, `k` is an integer between 1 and \(10^{18}\) inclusive, and `k` is less than or equal to `n`. If \((n - 1) // k\) is greater than \(n // k\), the program prints 'YES'. Otherwise, the program prints 'NO'
#Overall this is what the function does:The function reads two non-negative integers \(n\) and \(k\) from standard input, where \(1 \leq n, k \leq 10^{18}\) and \(k \leq n\). It then checks whether \(\left\lfloor \frac{n-1}{k} \right\rfloor\) is greater than \(\left\lfloor \frac{n}{k} \right\rfloor\). If true, it prints 'YES'; otherwise, it prints 'NO'. The function handles all valid inputs within the specified range and outputs one of the two possible strings based on the condition. If the inputs do not meet the specified constraints (i.e., \(n\) or \(k\) are outside the allowed range or \(k\) is greater than \(n\)), the function will not execute properly and will likely produce an error, although no specific error handling is provided in the code.

