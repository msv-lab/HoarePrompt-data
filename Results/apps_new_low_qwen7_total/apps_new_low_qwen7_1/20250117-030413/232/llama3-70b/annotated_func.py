#State of the program right berfore the function call: n and a are integers such that 1 ≤ a ≤ n ≤ 100 000 and n is even.
def func():
    n, a = map(int, input().split())
    if (a <= n // 2) :
        print(a // 2 + a % 2)
    else :
        print((n - a + 1) // 2 + (n - a + 1) % 2)
    #State of the program after the if-else block has been executed: *`a` is an integer where \(1 \leq a \leq \frac{n}{2}\). If `a` is even, the output is `a // 2`; if `a` is odd, the output is `a // 2 + 1`. If `a` is greater than \(\frac{n}{2}\), the output is `1`.
#Overall this is what the function does:The function takes no explicit parameters and reads two integers `n` and `a` from user input, where \(1 \leq a \leq n \leq 100,000\) and \(n\) is even. It then calculates and prints a value based on the relationship between `a` and `n`. Specifically, if `a` is less than or equal to \(\frac{n}{2}\), it prints \(\frac{a}{2} + a \% 2\). If `a` is greater than \(\frac{n}{2}\), it prints \(\frac{n - a + 1}{2} + (n - a + 1) \% 2\). The function ensures that the output is always an integer. This covers all possible cases where `a` can be within the range \(1 \leq a \leq n \leq 100,000\) and `n` is even.

