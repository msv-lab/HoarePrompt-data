#State of the program right berfore the function call: a, b, and n are integers such that 1 ≤ a, b ≤ 100, 2 ≤ n ≤ a + b.**
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function `func` reads three integer inputs `n`, `b`, and `c`, calculates a value `x` based on the ratio of the maximum and minimum of `b` and `c`, and then prints an integer result based on a formula involving `n`, `b`, `c`, and `x`. The function does not accept any parameters explicitly, instead, it reads inputs from the user. The return value of the function depends on the calculated result and the constraints on `a`, `b`, and `n`. The function does not handle cases where the inputs violate the specified constraints or if there are any potential division by zero errors.

