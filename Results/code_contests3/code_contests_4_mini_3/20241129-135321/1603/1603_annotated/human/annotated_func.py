#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 1000; for each visitor i, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function accepts two integers `n` and `m` (both within the range of 1 to 1000) and prints a string comprised of '10' repeated `n // 2` times, followed by '1' if `n` is odd. The function does not return any value and does not utilize the variable `m` or any pairs of integers `l_i` and `r_i`.

