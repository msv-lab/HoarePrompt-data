#State of the program right berfore the function call: n is an integer between 2 and a + b (inclusive), a and b are integers representing the number of pieces of the first and second cake respectively, where 1 ≤ a, b ≤ 100.
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts no parameters directly but reads three integers from input: `n`, `b`, and `c`. It calculates the ratio of the maximum of `b` and `c` to the minimum of `b` and `c`, then computes the ceiling of the product of one of the pieces (`min(b, c)`) divided by `n` multiplied by the previously calculated ratio. The result is printed as an integer. The function does not directly handle any edge cases regarding invalid or out-of-bound inputs.

