#State of the program right berfore the function call: x and y are integers such that 3 <= y < x <= 100,000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function accepts two integer parameters `x` and `y`, where `3 <= y < x <= 100,000`. It calculates and prints the result of \(\frac{(x - y)}{2} + \frac{(x - y) \mod 2}{1}\), which effectively rounds down the difference between `x` and `y` to the nearest even number. This means if `(x - y)` is even, it simply prints \(\frac{(x - y)}{2}\); if `(x - y)` is odd, it prints \(\frac{(x - y) + 1}{2}\). The function reads the values of `x` and `y` from standard input, splits them by space, and converts them to integers before performing the calculation. There are no return values; instead, the result is printed to the console. The function handles the specified range for `x` and `y`, ensuring that `x` and `y` are within the bounds provided. No additional edge cases or missing functionality exist based on the given code.

