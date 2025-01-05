#State of the program right berfore the function call: n is a positive integer representing the number of flowers, m is a positive integer representing the number of visitors, and each visitor is represented by a pair of integers (l_i, r_i) such that 1 ≤ l_i ≤ r_i ≤ n.
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function accepts two positive integers, `n` (the number of flowers) and `m` (the number of visitors), but it does not utilize the `m` parameter in its operations. It generates and prints a string of '10's for every pair of flowers (i.e., half of `n`), followed by '1' if `n` is odd. Therefore, the function outputs a string representing the arrangement of flowers based solely on the integer `n`, ignoring the visitor assignments entirely.

