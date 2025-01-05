#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ a + b, a is an integer representing the number of pieces of the first cake (1 ≤ a ≤ 100), and b is an integer representing the number of pieces of the second cake (1 ≤ b ≤ 100).
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts three integers `n`, `b`, and `c`. It calculates the ratio of the maximum of `b` and `c` to the minimum of `b` and `c`, then computes the required number of pieces based on `n` and prints the ceiling of that result. However, the function does not return any value; it only prints the result. The function assumes that the input values for `n`, `b`, and `c` are provided correctly, but there are no checks for input validity or edge cases such as division by zero, as `min(b, c)` will always be non-zero given the constraints.

