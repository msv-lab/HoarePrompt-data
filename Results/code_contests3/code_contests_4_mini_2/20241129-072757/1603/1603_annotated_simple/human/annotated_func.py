#State of the program right berfore the function call: n is a positive integer representing the number of flowers, m is a positive integer representing the number of visitors, and for each visitor i, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function accepts two positive integers, `n` (the number of flowers) and `m` (the number of visitors), and prints a string consisting of '10' repeated for each pair of flowers (for even `n`), and adds a '1' if `n` is odd. However, it does not actually count or track unique flowers visited by the visitors; instead, it only prints a pattern based on the value of `n`. Therefore, the function does not fulfill the stated goal regarding the visitors and unique flowers.

