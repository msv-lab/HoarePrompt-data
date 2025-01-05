#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 1000, and each l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n for i from 1 to m.
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function accepts two integers `n` and `m`, where both are constrained to be between 1 and 1000. It generates and prints a string composed of '10' repeated `(n // 2)` times, and appends '1' if `n` is odd. The function does not return any value and does not utilize the variable `m` or any ranges `l_i` and `r_i` as mentioned in the annotations, making those comments irrelevant.

