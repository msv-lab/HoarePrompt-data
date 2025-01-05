#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ a + b, a is an integer representing the number of pieces of the first cake (1 ≤ a ≤ 100), and b is an integer representing the number of pieces of the second cake (1 ≤ b ≤ 100).
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts three integers `n`, `b`, and `c`, computes a scaled ratio of the maximum to minimum of `b` and `c`, and prints the ceiling of the result. It does not return any value and lacks error handling for invalid inputs.

