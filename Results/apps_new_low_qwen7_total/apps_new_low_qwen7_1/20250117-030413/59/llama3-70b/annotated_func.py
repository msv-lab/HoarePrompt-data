#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, a is an integer such that 1 ≤ a ≤ n, and b is an integer such that 1 ≤ b ≤ n.
def func():
    n = int(input())

a = int(input())

b = int(input())

total_length = 2 * (a * 2 + b)
    if (total_length <= n) :
        print(1)
    else :
        print(-(-total_length // n))
    #State of the program after the if-else block has been executed: `n` is an integer such that \(1 \leq n \leq 1000\), `a` is an integer such that \(1 \leq a \leq n\), `b` is an integer such that \(1 \leq b \leq n\), `total_length` is \(2 \times (a \times 2 + b)\). If `total_length` is less than or equal to `n`, the function does not change `total_length`. Otherwise, `total_length` is set to \(\left\lfloor \frac{2 \times (2a + b)}{n} \right\rfloor\).
#Overall this is what the function does:The function accepts three integer inputs `n`, `a`, and `b`, where \(1 \leq n \leq 1000\) and \(1 \leq a, b \leq n\). It calculates the total length as \(2 \times (a \times 2 + b)\). Depending on whether `total_length` is less than or equal to `n`, it prints either `1` or the result of \(-(-\text{total_length} // n)\). The final state of the program is that it prints either `1` or \(\left\lfloor \frac{2 \times (2a + b)}{n} \right\rfloor\) based on the condition. The function does not return anything explicitly; instead, it outputs the result directly.

