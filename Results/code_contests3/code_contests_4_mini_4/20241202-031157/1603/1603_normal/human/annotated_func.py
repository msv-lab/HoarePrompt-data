#State of the program right berfore the function call: n is a positive integer representing the number of flowers (1 ≤ n ≤ 1000), m is a positive integer representing the number of visitors (1 ≤ m ≤ 1000), and each visitor's range (l_i, r_i) is such that 1 ≤ l_i ≤ r_i ≤ n.
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function accepts two positive integers `n` (the number of flowers) and `m` (the number of visitors), but it does not utilize the number of visitors or their ranges. It generates and prints a string consisting of '10' repeated `n // 2` times, followed by '1' if `n` is odd. Thus, it only outputs a specific pattern based on the number of flowers and ignores the visitor-related input entirely.

