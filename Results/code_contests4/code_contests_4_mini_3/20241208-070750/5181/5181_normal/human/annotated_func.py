#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 10^9.
def func():
    a, b, c = map(int, raw_input().split())
    print(a + b) + 2 * c
#Overall this is what the function does:The function reads three positive integers `a`, `b`, and `c` from input, calculates the sum of `a` and `b`, and then adds twice the value of `c` to that sum. The function does not return a value but instead prints the result of this calculation.

