#State of the program right berfore the function call: n and k are non-negative integers such that 1 ≤ n, k ≤ 10^18 and k ≤ n.
def func():
    n, k = map(int, input().split())
    if ((n - 1) // k > n // k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is an integer between 1 and \(10^{18}\) inclusive, `k` is an integer between 1 and \(10^{18}\) inclusive, and \(k \leq n\). If \((n - 1) // k > n // k\), the output is 'YES'. Otherwise, there is no specific output change, but the condition \((n - 1) // k \leq n // k\) holds true.
#Overall this is what the function does:The function accepts two parameters \(n\) and \(k\), both non-negative integers such that \(1 \leq n, k \leq 10^{18}\) and \(k \leq n\). It checks whether the inequality \(\left\lfloor \frac{n-1}{k} \right\rfloor > \left\lfloor \frac{n}{k} \right\rfloor\) holds true. If the condition is met, the function prints 'YES'; otherwise, it prints 'NO'. There are no additional changes to the variables \(n\) and \(k\) after the function executes. The function handles the edge case where the values of \(n\) and \(k\) are within the specified range but does not handle cases where \(n\) or \(k\) are outside this range, which would result in an invalid input scenario.

