#State of the program right berfore the function call: **Precondition**: **n and m are integers such that 1 <= n, m <= 10^3. Each l_i and r_i are integers such that 1 <= l_i <= r_i <= n.**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from the input, then prints a string consisting of '10' repeated `n/2` times followed by '1' if `n` is odd. The function does not return any value.

