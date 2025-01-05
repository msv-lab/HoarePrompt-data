#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 10^9.
def func():
    a, b, c = map(int, raw_input().split())
    print(a + b) + 2 * c
#Overall this is what the function does:The function reads three positive integers `a`, `b`, and `c` from input, computes the value of `a + b + 2 * c`, and prints the result. It does not return any value.

