#State of the program right berfore the function call: n and a are integers such that 1 ≤ a ≤ n ≤ 100 000 and n is even.
def func():
    n, a = map(int, input().split())
    if (a <= n // 2) :
        print(a // 2 + a % 2)
    else :
        print((n - a + 1) // 2 + (n - a + 1) % 2)
    #State of the program after the if-else block has been executed: *`n` is an even integer between 1 and 100,000 inclusive, and `a` is an integer such that \(1 \leq a \leq n \leq 100,000\). If \(a \leq \frac{n}{2}\), the printed value is either `a // 2` if `a` is even or `a // 2 + 1` if `a` is odd. If \(a > \frac{n}{2}\), the printed value is 0.
#Overall this is what the function does:The function processes two integers, \(n\) and \(a\), where \(1 \leq a \leq n \leq 100,000\) and \(n\) is even. It prints a value based on the relationship between \(a\) and \(n\). Specifically, if \(a \leq \frac{n}{2}\), it prints either \(a // 2\) if \(a\) is even, or \(a // 2 + 1\) if \(a\) is odd. If \(a > \frac{n}{2}\), it prints \(0\). The function does not return a value but modifies the output stream by printing the calculated value. There are no explicit edge cases mentioned in the code that need to be handled separately, but the code correctly handles the boundary condition where \(a = \frac{n}{2}\) by ensuring the correct value is printed based on whether \(a\) is even or odd.

