#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^18 and k ≤ n.
def func():
    n, k = map(int, input().split())
    if ((n - 1) // k > n // k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` and `k` are positive integers such that \(1 \leq n, k \leq 10^{18}\) and \(k \leq n\). If \((n - 1) // k > n // k\), the program prints 'YES'. Otherwise, the program does not print anything specific but maintains the same preconditions.
#Overall this is what the function does:The function accepts no parameters directly but relies on user input for two positive integers \(n\) and \(k\) where \(1 \leq n, k \leq 10^{18}\) and \(k \leq n\). It then checks whether \(\left\lfloor \frac{n-1}{k} \right\rfloor > \left\lfloor \frac{n}{k} \right\rfloor\). If the condition is true, it prints 'YES'; otherwise, it prints 'NO'. There are no explicit return values, but the printed output ('YES' or 'NO') indicates the result of the comparison. Potential edge cases include when \(n = k\), which would result in both floor divisions being equal, leading to a 'NO' output. The function does not handle invalid inputs such as non-integer or out-of-range values for \(n\) and \(k\).

