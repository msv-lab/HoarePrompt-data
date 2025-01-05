#State of the program right berfore the function call: n and m are integers such that 1 <= n, m <= 10^3. Each segment [l_i, r_i] is valid, where 1 <= l_i <= r_i <= n.**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from the user input, and then prints a string composed of '10' repeated `n // 2` times, and adds '1' at the end if `n` is odd. The function does not explicitly return any value.

