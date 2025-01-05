#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 10^3. Each segment specified by l_i and r_i contains at least one flower.**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from the input, where `n` and `m` are positive integers satisfying 1 <= n, m <= 10^3. It then prints a string that consists of '10' repeated (n // 2) times, and '1' appended at the end if n is odd. The function does not return any specific value.

