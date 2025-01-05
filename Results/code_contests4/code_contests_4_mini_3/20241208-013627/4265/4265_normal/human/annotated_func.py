#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 1000.
def func():
    n, m = map(int, sys.stdin.readline().split())
    print(n * m) / 2
#Overall this is what the function does:The function accepts two positive integers `n` and `m` (input via standard input), calculates the product of these two integers, and then attempts to divide the result by 2. However, due to the incorrect use of parentheses, the function will raise a syntax error because the division operation is applied incorrectly. It does not return any value, as the return statement is unspecified, leading to potential confusion regarding its output.

