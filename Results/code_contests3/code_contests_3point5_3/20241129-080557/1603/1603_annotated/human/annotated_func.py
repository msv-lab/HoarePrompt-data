#State of the program right berfore the function call: n and m are non-negative integers such that 1 <= n, m <= 10^3. Each segment defined by l_i and r_i contains only valid indices within the range of flowers (1 <= l_i <= r_i <= n).**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function `func` reads two non-negative integers `n` and `m` from the input and prints a string based on the value of `n`. It constructs a string by repeating '10' `(n // 2)` times and appending '1' if `n` is odd. The function does not explicitly return any value.

