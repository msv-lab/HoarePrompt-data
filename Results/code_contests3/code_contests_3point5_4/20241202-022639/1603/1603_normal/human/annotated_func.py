#State of the program right berfore the function call: n and m are integers such that 1 <= n, m <= 10^3. Each segment [l_i, r_i] is valid with 1 <= l_i <= r_i <= n.**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from the input, then prints a string based on the values of `n` and whether it is odd or even. It constructs the string by repeating '10' a number of times equal to half of `n`, and adding '1' at the end if `n` is odd. The function does not accept any parameters explicitly.

