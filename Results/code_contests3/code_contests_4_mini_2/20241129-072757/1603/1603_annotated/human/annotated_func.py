#State of the program right berfore the function call: n is a positive integer representing the number of flowers, m is a positive integer representing the number of visitors, and each visitor's range (l_i, r_i) consists of two integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function accepts two positive integers, `n` (number of flowers) and `m` (number of visitors), but it only processes the input for `n` to generate a string that consists of the digit '10' repeated `n // 2` times, and potentially a single '1' if `n` is odd. The parameter `m` and the ranges `(l_i, r_i)` for each visitor are provided as input but are not utilized in the function, indicating missing functionality related to visitor processing.

