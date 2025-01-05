#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 10^9.
def func():
    a, b, c = map(int, raw_input().split())
    print(a + b) + 2 * c
#Overall this is what the function does:The function accepts three positive integers `a`, `b`, and `c`, reads them from input, and calculates the result as `a + b + 2 * c`, but does not return any value; instead, it prints the result directly.

